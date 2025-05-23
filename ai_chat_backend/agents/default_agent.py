from .base import Agent

class DefaultAgent(Agent):
    """Fallback agent for general questions."""

    agent_name = "DefaultAgent"
    system_prompt = "You are a helpful general-purpose assistant."

    def generate_response(self, message: str) -> str:
        return super().generate_response(message)
