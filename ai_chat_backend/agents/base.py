from __future__ import annotations

from typing import Dict, Type, List

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
    # Default model name; subclasses can override.
    model_name: str = ""

    def __init__(
        self,
        description: str = "",
        keywords: List[str] | None = None,
        model: str | None = None,
    ) -> None:
        self.description = description
        if keywords is not None:
            # Instances override the class-level default keywords so strategies
            # can rely on per-agent configuration.
            self.keywords = keywords
        if model is not None:
            self.model_name = model

    def generate_response(self, message: str) -> str:
        raise NotImplementedError
