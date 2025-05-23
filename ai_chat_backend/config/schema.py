from __future__ import annotations
from typing import List
from pydantic import BaseModel

class AgentConfig(BaseModel):
    name: str
    class_path: str
    description: str = ""

class Config(BaseModel):
    agents: List[AgentConfig]
