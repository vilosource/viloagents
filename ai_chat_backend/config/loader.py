from __future__ import annotations
import importlib
import yaml
from .schema import Config

class ConfigManager:
    def __init__(self, path: str) -> None:
        self.path = path
        self.config: Config | None = None

    def load(self) -> Config:
        with open(self.path, 'r') as f:
            data = yaml.safe_load(f)
        self.config = Config(**data)
        return self.config

    def instantiate_agents(self):
        agents = {}
        for agent_cfg in self.config.agents:
            module_name, class_name = agent_cfg.class_path.rsplit('.', 1)
            module = importlib.import_module(module_name)
            cls = getattr(module, class_name)
            agents[agent_cfg.name] = cls(agent_cfg.description)
        return agents
