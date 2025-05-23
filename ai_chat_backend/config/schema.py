from __future__ import annotations
from typing import List
from pydantic import BaseModel

class AgentConfig(BaseModel):
    name: str
    class_path: str
    description: str = ""
    # Optional list of keywords used by routing strategies.
    keywords: List[str] = []
    # Optional model name used by the agent (e.g. openrouter/gpt-4).
    model: str | None = None

class Config(BaseModel):
    agents: List[AgentConfig]
