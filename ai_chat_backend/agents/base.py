from __future__ import annotations

from typing import Dict, Type

AGENT_REGISTRY: Dict[str, Type["Agent"]] = {}

class AgentMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        agent_name = getattr(cls, "agent_name", None)
        if agent_name:
            AGENT_REGISTRY[agent_name] = cls

class Agent(metaclass=AgentMeta):
    agent_name: str = ""

    def __init__(self, description: str = "") -> None:
        self.description = description

    def generate_response(self, message: str) -> str:
        raise NotImplementedError
