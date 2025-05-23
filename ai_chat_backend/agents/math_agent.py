from .base import Agent

class MathAgent(Agent):
    """Agent specialized in math questions."""

    agent_name = "MathAgent"

    def generate_response(self, message: str) -> str:
        # Placeholder for actual math handling logic
        return "MathAgent received: " + message
