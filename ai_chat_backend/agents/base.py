from __future__ import annotations

import os
from typing import Dict, Type, Any, List

try:
    from langchain.chat_models import ChatOpenAI  # type: ignore
    from langchain.schema import HumanMessage, SystemMessage  # type: ignore
except Exception:  # pragma: no cover - fallback when langchain is unavailable
    ChatOpenAI = None  # type: ignore

    class _Message:  # pragma: no cover - minimal message stub
        def __init__(self, content: str) -> None:
            self.content = content

    HumanMessage = SystemMessage = _Message  # type: ignore

class _EchoLLM:
    """Fallback LLM used when LangChain is not installed."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pragma: no cover - noop
        pass

    def invoke(self, messages: list[Any]) -> Any:  # pragma: no cover - deterministic echo
        return type("LLMResult", (), {"content": f"ECHO: {messages[-1].content}"})

AGENT_REGISTRY: Dict[str, Type["Agent"]] = {}

class AgentMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        agent_name = getattr(cls, "agent_name", None)
        if agent_name:
            AGENT_REGISTRY[agent_name] = cls


class Agent(metaclass=AgentMeta):
    agent_name: str = ""
    # Each agent can specify routing keywords.  This supports the Open/Closed
    # Principle by allowing new agents to declare their own keywords without
    # modifying the router.
    keywords: List[str] = []
    system_prompt: str = "You are a helpful assistant."

    def __init__(
        self,
        description: str = "",
        model_name: str | None = None,
        keywords: List[str] | None = None,
    ) -> None:
        self.description = description
        self.model_name = model_name or "gpt-3.5-turbo"

        if keywords is not None:
            # Instances override the class-level default keywords so strategies
            # can rely on per-agent configuration.
            self.keywords = keywords

        if ChatOpenAI is not None:
            # Ensure OpenRouter endpoint is used if no base specified
            os.environ.setdefault("OPENAI_API_BASE", "https://openrouter.ai/api/v1")
            self.llm = ChatOpenAI(model_name=self.model_name, streaming=False)
        else:  # pragma: no cover - fallback when langchain missing
            self.llm = _EchoLLM()

    def generate_response(self, message: str) -> str:
        messages = [SystemMessage(content=self.system_prompt), HumanMessage(content=message)]

        if hasattr(self.llm, "invoke"):
            result = self.llm.invoke(messages)
        else:
            result = self.llm(messages)

        return getattr(result, "content", str(result))
