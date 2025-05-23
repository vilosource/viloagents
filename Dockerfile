FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml ./
RUN pip install poetry && poetry install --no-dev --no-interaction
COPY . .
CMD ["poetry", "run", "python", "-m", "ai_chat_backend.main"]
