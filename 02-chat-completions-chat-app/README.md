# 02 - Chat Completions Chat App

This project is a Python console chat app that calls a deployed model in Azure AI Foundry using the Chat Completions API.

It demonstrates how a basic generative AI chat application works internally.

## What this project demonstrates

- Calling a deployed Azure AI Foundry model from Python
- Using the Chat Completions API
- Using `system`, `user`, and `assistant` message roles
- Maintaining conversation history in the application
- Loading prompts from a separate file
- Reading configuration from environment variables
- Handling common API errors safely

## AI-103 mapping

This project maps to AI-103 skills related to:

- Developing generative AI apps with Azure AI Foundry
- Connecting application code to deployed models
- Managing prompt instructions
- Processing model responses
- Handling errors and configuration securely

## Project structure

```text
02-chat-completions-chat-app/
  README.md
  requirements.txt
  .env.example
  .gitignore
  src/
    chat_app.py
    config.py
  prompts/
    system_prompt.md
  examples/
    sample_conversation.json
    sample_response.json