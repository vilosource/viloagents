from __future__ import annotations
import importlib
from .schema import Config

try:
    import yaml  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - fallback when PyYAML not installed
    yaml = None

class ConfigManager:
    """Load and instantiate agents from a YAML configuration file.

    This class follows the *Single Responsibility Principle* by handling only
    configuration parsing and object construction.  Other components can depend
    on it via its public interface, which also aligns with the *Dependency
    Inversion Principle* by exposing high-level abstractions rather than the
    details of YAML parsing.
    """

    def __init__(self, path: str) -> None:
        self.path = path
        self.config: Config | None = None

    def load(self) -> Config:
        """Parse the YAML file and return a :class:`Config` instance."""
        with open(self.path, "r", encoding="utf-8") as f:
            content = f.read()
        if yaml is not None:
            data = yaml.safe_load(content)
        else:  # very small YAML subset parser as fallback
            data = self._parse_simple_yaml(content)
        self.config = Config(**data)
        return self.config

    def _parse_simple_yaml(self, text: str) -> dict:
        """Parse a minimal YAML subset used for the default configuration."""
        result = {"agents": []}
        current = None
        for line in text.splitlines():
            line = line.rstrip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("agents:"):
                continue
            if line.lstrip().startswith("-"):
                current = {}
                result["agents"].append(current)
                line = line.lstrip()[1:].strip()
            if ":" in line:
                key, value = line.split(":", 1)
                current[key.strip()] = value.strip().strip('"')
        return result

    def instantiate_agents(self):
        """Instantiate agent objects declared in the configuration.

        The method implements a simple *Factory* pattern: it constructs agent
        instances based on their fully qualified class paths.  Consumers of this
        class do not need to know the concrete agent classes ahead of time.
        """

        if self.config is None:
            # Lazily load configuration if not already done.
            self.load()

        agents = {}
        for agent_cfg in self.config.agents:
            module_name, class_name = agent_cfg.class_path.rsplit(".", 1)
            module = importlib.import_module(module_name)
            cls = getattr(module, class_name)
            agents[agent_cfg.name] = cls(
                agent_cfg.description,
                model_name=agent_cfg.model,
            )
            if agent_cfg.system_prompt:
                agents[agent_cfg.name].system_prompt = agent_cfg.system_prompt
        return agents
