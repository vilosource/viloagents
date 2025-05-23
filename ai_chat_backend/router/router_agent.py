from __future__ import annotations

from typing import Dict

from ..agents.base import AGENT_REGISTRY, Agent
from ..config.loader import ConfigManager

from .strategy import RoutingStrategy, KeywordRoutingStrategy

class RouterAgent:
    """Select the appropriate agent to handle a user message."""

    def __init__(self, agents: Dict[str, Agent] | None = None, strategy: RoutingStrategy | None = None) -> None:
        # Dependency injection of collaborators keeps the router flexible and
        # testable. When ``agents`` is ``None`` we fall back to the registry of
        # statically defined agents, preserving backward compatibility.

        # Use a keyword-based routing strategy by default to better match user
        # intent.  The *Strategy* pattern allows swapping this out for a more
        # advanced LLM-driven strategy without modifying this class.
        self.strategy = strategy or KeywordRoutingStrategy()
        if agents is None:
            agents = {name: cls() for name, cls in AGENT_REGISTRY.items()}
        self.agents = agents

    @classmethod
    def from_config(cls, config_path: str, strategy: RoutingStrategy | None = None) -> "RouterAgent":
        """Factory method to construct a router from a YAML configuration."""
        manager = ConfigManager(config_path)
        agents = manager.instantiate_agents()
        return cls(agents=agents, strategy=strategy)

    def generate_response(self, message: str) -> str:
        """Route the user message to the chosen agent and return its response."""
        agent_name = self.strategy.choose_agent(message, self.agents)
        agent = self.agents[agent_name]
        return agent.generate_response(message)
