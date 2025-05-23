from __future__ import annotations

from typing import Dict

from ..agents.base import Agent


class RoutingStrategy:
    """Strategy interface for choosing an agent."""

    def choose_agent(self, user_message: str, agents: Dict[str, Agent]) -> str:
        raise NotImplementedError


class SimpleStrategy(RoutingStrategy):
    """Trivial strategy that always selects the first agent."""

    def choose_agent(self, user_message: str, agents: Dict[str, Agent]) -> str:
        return next(iter(agents))


class KeywordRoutingStrategy(RoutingStrategy):
    """Route messages by matching configured keywords."""

    def choose_agent(self, user_message: str, agents: Dict[str, Agent]) -> str:
        message = user_message.lower()
        for name, agent in agents.items():
            for kw in getattr(agent, "keywords", []):
                if kw.lower() in message:
                    return name
        # Fallback to default ordering when no keywords match. This reuse of
        # ``SimpleStrategy`` demonstrates the *Strategy* pattern and keeps each
        # strategy small and focused (Single Responsibility Principle).
        return SimpleStrategy().choose_agent(user_message, agents)
