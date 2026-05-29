import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

required_settings = {
    "AZURE_OPENAI_ENDPOINT": endpoint,
    "AZURE_OPENAI_API_KEY": api_key,
    "AZURE_OPENAI_DEPLOYMENT": deployment,
}

missing_settings = [
    name for name, value in required_settings.items() if not value
]

if missing_settings:
    raise ValueError(
        "Missing required environment variables: "
        + ", ".join(missing_settings)
    )

client = OpenAI(
    base_url=endpoint,
    api_key=api_key,
)

completion = client.chat.completions.create(
    model=deployment,
    messages=[
        {
            "role": "user",
            "content": "Explain Microsoft Foundry in one simple sentence.",
        }
    ],
)

assistant_response = completion.choices[0].message.content

print("Prompt:")
print("Explain Microsoft Foundry in one simple sentence.")
print()
print("Assistant response:")
print(assistant_response)