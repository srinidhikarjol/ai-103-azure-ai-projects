import os
from dataclasses import dataclass
from dotenv import load_dotenv


@dataclass
class AzureOpenAIconfig:
    endpoint: str
    api_key: str
    deployment: str
    api_version: str


def load_config() -> AzureOpenAIconfig :
    """
    Load Azure OpenAI / Foundry configuration from environment variables.

    Important:
    - .env is used only for local development.
    - Real secrets should never be committed to Git.
    - We validate required values before making any API call.
    """
    
    load_dotenv();
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION")

    missing_values = []

    if not endpoint:
        missing_values.append("AZURE_OPENAI_ENDPOINT")

    if not api_key:
        missing_values.append("AZURE_OPENAI_API_KEY")

    if not deployment:
        missing_values.append("AZURE_OPENAI_DEPLOYMENT")

    if not api_version:
        missing_values.append("AZURE_OPENAI_API_VERSION")

    if missing_values:
        raise ValueError(
            "Missing required environment variables: "
            + ", ".join(missing_values)
        )

    return AzureOpenAIconfig(
        endpoint=endpoint,
        api_key=api_key,
        deployment=deployment,
        api_version=api_version,
    )
