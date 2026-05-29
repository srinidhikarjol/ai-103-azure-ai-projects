# Foundry Model Basics

## Scenario

This project demonstrates how to call a deployed Microsoft Foundry model from a Python application.

The app sends a simple prompt to a deployed `gpt-4o-mini` model and prints the assistant response.

## Architecture

```text
Python app
  ↓
Microsoft Foundry endpoint
  ↓
Deployed gpt-4o-mini model
  ↓
Assistant response
```

## Azure Services Used

- Microsoft Foundry
- Foundry project
- Deployed `gpt-4o-mini` model
- Foundry model endpoint

## Project Structure

```text
01-foundry-model-basics/
  src/
    hello_model.py
  examples/
    request.json
    response.json
  .env.example
  .gitignore
  requirements.txt
  README.md
```

## Environment Variables

Create a `.env` file using `.env.example`.

```env
AZURE_OPENAI_ENDPOINT=https://your-resource-name.services.ai.azure.com
AZURE_OPENAI_API_KEY=your-api-key-here
AZURE_OPENAI_DEPLOYMENT=gpt-4o-mini-practise
AZURE_OPENAI_API_VERSION=2024-10-21
```

Do not commit `.env` to GitHub.

## Setup

Install dependencies:

```powershell
pip install -r requirements.txt
```

Run the app:

```powershell
python src/hello_model.py
```

## Sample Prompt

```text
Explain Microsoft Foundry in one simple sentence.
```

## Sample Output

```text
Prompt:
Explain Microsoft Foundry in one simple sentence.

Assistant response:
Microsoft Foundry is a platform for building, deploying, and managing AI apps and agents on Azure.
```

## AI-103 Exam Mapping

This project demonstrates:

- Using Microsoft Foundry
- Calling a deployed model endpoint
- Sending prompts from Python
- Reading model responses
- Keeping secrets outside source code
- Understanding request and response JSON

## Cost Notes

This project sends a small number of prompts to a deployed model. Usage may incur Azure charges.

For practice:

- Use short prompts
- Avoid large loops
- Avoid provisioned throughput
- Check Azure Cost Management regularly