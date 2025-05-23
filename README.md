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

## LLM Integration

Agents use LangChain's `ChatOpenAI` class to call OpenRouter models. Set the
following environment variables before running the server or CLI:

```bash
export OPENAI_API_KEY="<your-openrouter-key>"
export OPENAI_API_BASE="https://openrouter.ai/api/v1"
```

Tests run without network access by patching the LLM class, so no API key is
required for running the test suite.
