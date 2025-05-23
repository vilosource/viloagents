# viloagents

A modular AI chat backend based on FastAPI and LangChain.

## Development Setup

1. Install dependencies using Poetry:
   ```bash
   poetry install
   ```
2. Run the API server:
   ```bash
   poetry run python -m ai_chat_backend.main
   ```
3. Or start the CLI:
   ```bash
   poetry run python -m ai_chat_backend.api.cli
   ```

## Using OpenRouter

The agents use LangChain's `ChatOpenAI` client which reads the following
environment variables:

* `OPENAI_API_KEY` – your OpenRouter token.
* `OPENAI_API_BASE` – the OpenRouter API endpoint
  (`https://openrouter.ai/api/v1`).

Set these variables before running the server or CLI. The selected model for
each agent is defined in `agents.yaml` under the `model` field.

### Quick test

To experiment from the command line after configuring your token, run:

```bash
export OPENAI_API_KEY=your-token
export OPENAI_API_BASE=https://openrouter.ai/api/v1
poetry run python scripts/chat_demo.py
```

Type messages at the prompt to chat with the default backend agent. Use `exit`
to quit.
