import os

try:  # pragma: no cover - allow running without langchain installed
    from langchain.chat_models import ChatOpenAI
    from langchain.schema import HumanMessage, SystemMessage
except ModuleNotFoundError:  # pragma: no cover - dependency optional for tests
    ChatOpenAI = None  # type: ignore
    HumanMessage = SystemMessage = None

from .base import Agent

class DefaultAgent(Agent):
    """Fallback agent for general questions."""

    agent_name = "DefaultAgent"
    # No specific keywords; acts as a catch-all agent.
    keywords: list[str] = []

    model_name = "openrouter/gpt-3.5-turbo"

    def __init__(self, description: str = "", keywords: list[str] | None = None, model: str | None = None) -> None:
        super().__init__(description, keywords, model=model)
        self.system_prompt = self.description or "You are a helpful assistant."
        key = os.getenv("OPENAI_API_KEY")
        if key and key != "test" and ChatOpenAI is not None:
            # Only create the LLM client when we have a real API key and LangChain is available.
            self.llm = ChatOpenAI(model_name=self.model_name)
        else:
            self.llm = None

    def generate_response(self, message: str) -> str:
        if self.llm is None or HumanMessage is None:
            return "I'm a default agent responding to: " + message

        messages = [SystemMessage(content=self.system_prompt), HumanMessage(content=message)]
        response = self.llm(messages)
        return response.content
