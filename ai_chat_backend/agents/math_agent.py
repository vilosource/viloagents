from .base import Agent

class MathAgent(Agent):
    """Agent specialized in math questions."""

    agent_name = "MathAgent"
    keywords = ["math", "calculate", "addition", "subtraction", "multiply", "divide"]

    def __init__(self, description: str = "", keywords: list[str] | None = None, model: str | None = None) -> None:
        super().__init__(description, keywords, model=model)

    def generate_response(self, message: str) -> str:
        # Placeholder for actual math handling logic
        return "MathAgent received: " + message
