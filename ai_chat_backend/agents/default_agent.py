from .base import Agent

class DefaultAgent(Agent):
    """Fallback agent for general questions."""

    agent_name = "DefaultAgent"

    def generate_response(self, message: str) -> str:
        return "I'm a default agent responding to: " + message
