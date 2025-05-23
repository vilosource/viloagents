from __future__ import annotations
from typing import List
from pydantic import BaseModel

class AgentConfig(BaseModel):
    name: str
    class_path: str
    description: str = ""
    # Optional list of keywords used by routing strategies.
    keywords: List[str] = []

class Config(BaseModel):
    agents: List[AgentConfig]
