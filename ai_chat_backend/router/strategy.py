from __future__ import annotations

class RoutingStrategy:
    def choose_agent(self, user_message: str, agents: dict) -> str:
        raise NotImplementedError

class SimpleStrategy(RoutingStrategy):
    def choose_agent(self, user_message: str, agents: dict) -> str:
        return next(iter(agents))
