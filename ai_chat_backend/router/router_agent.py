from __future__ import annotations

from typing import Dict

from ..agents.base import AGENT_REGISTRY, Agent
from .strategy import RoutingStrategy, SimpleStrategy

class RouterAgent:
    def __init__(self, strategy: RoutingStrategy | None = None) -> None:
        self.strategy = strategy or SimpleStrategy()
        self.agents: Dict[str, Agent] = {name: cls() for name, cls in AGENT_REGISTRY.items()}

    def generate_response(self, message: str) -> str:
        agent_name = self.strategy.choose_agent(message, self.agents)
        agent = self.agents[agent_name]
        return agent.generate_response(message)
