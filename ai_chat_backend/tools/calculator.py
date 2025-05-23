from .base import Tool

class CalculatorTool(Tool):
    name = "CalculatorTool"
    description = "Perform simple arithmetic evaluations."

    def run(self, query: str) -> str:
        try:
            return str(eval(query, {}, {}))
        except Exception:
            return "Error"
