from openai import AzureOpenAI
from config import load_config


def load_system_prompt(file_path) :
    """
    Load the system prompt from a markdown file.

    Internals:
    - The system prompt becomes the first message in the chat history.
    - It controls assistant behavior across the conversation.
    - Keeping it in a separate file makes prompt changes easier.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().strip()
    
def create_client():
    """
    Create an AzureOpenAI client using config values.

    Internals:
    - The SDK uses this client to make HTTP/API calls to Azure Foundry.
    - The deployment name is not configured here.
    - The deployment name is passed when making the chat completion request.
    """
    config = load_config()

    client = AzureOpenAI(
        azure_endpoint=config.endpoint,
        api_key=config.api_key,
        api_version=config.api_version,
    )

    return client, config.deployment

def get_assistant_reply(client, deployment: str, messages: list[dict]) -> str:
    """
    Send the current conversation history to the deployed model.

    Internals:
    - messages contains system, user, and assistant turns.
    - The model receives the whole relevant conversation each time.
    - The API response contains the assistant reply inside choices[0].
    """
    completion = client.chat.completions.create(
        model=deployment,
        messages=messages,
        temperature=0.2,
        max_tokens=500,
    )

    return completion.choices[0].message.content

def main():
    print("AI-103 Chat Completions App")
    print("Type 'exit' to stop.\n")

    system_prompt = load_system_prompt("prompts/system_prompt.md")
    client, deployment = create_client()

    messages = [
        {
            "role": "system",
            "content": system_prompt,
        }
    ]

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        if not user_input:
            print("Please enter a message.")
            continue

        messages.append(
            {
                "role": "user",
                "content": user_input,
            }
        )

        try:
            assistant_reply = get_assistant_reply(
                client=client,
                deployment=deployment,
                messages=messages,
            )

            print(f"\nAssistant: {assistant_reply}\n")

            messages.append(
                {
                    "role": "assistant",
                    "content": assistant_reply,
                }
            )

        except Exception as error:
            print("\nSomething went wrong while calling the model.")
            print("Safe error message:", str(error))
            print("The failed assistant response was not added to history.\n")

            messages.pop()


if __name__ == "__main__":
    main()

