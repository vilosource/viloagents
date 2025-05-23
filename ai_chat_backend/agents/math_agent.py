from .base import Agent

class MathAgent(Agent):
    """Agent specialized in math questions."""

    agent_name = "MathAgent"
    system_prompt = "You are a math expert AI that solves problems step by step."

    def generate_response(self, message: str) -> str:
        return super().generate_response(message)
