import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from ai_chat_backend.config.loader import ConfigManager
from ai_chat_backend.router.router_agent import RouterAgent
from ai_chat_backend.agents.default_agent import DefaultAgent
from ai_chat_backend.agents.math_agent import MathAgent


def get_config_path() -> pathlib.Path:
    """Return the path to agents.yaml in the repository root."""
    return pathlib.Path(__file__).resolve().parents[1] / "agents.yaml"


def test_config_manager_instantiates_agents():
    manager = ConfigManager(str(get_config_path()))
    cfg = manager.load()
    agents = manager.instantiate_agents()

    assert len(cfg.agents) == 2
    assert set(agents.keys()) == {"DefaultAgent", "MathAgent"}
    assert isinstance(agents["DefaultAgent"], DefaultAgent)
    assert agents["DefaultAgent"].description == "General purpose agent"
    assert isinstance(agents["MathAgent"], MathAgent)
    assert agents["MathAgent"].description == "Handles math queries"


def test_router_agent_from_config():
    router = RouterAgent.from_config(str(get_config_path()))
    assert isinstance(router.agents["DefaultAgent"], DefaultAgent)
    assert isinstance(router.agents["MathAgent"], MathAgent)
    response = router.generate_response("hello")
    assert response.startswith("I'm a default agent")
