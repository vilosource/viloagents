import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from ai_chat_backend.router.strategy import KeywordRoutingStrategy
from ai_chat_backend.router.router_agent import RouterAgent
from ai_chat_backend.config.loader import ConfigManager


def get_config_path() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parents[1] / "agents.yaml"


def test_keyword_routing_strategy_selects_math_agent():
    manager = ConfigManager(str(get_config_path()))
    agents = manager.instantiate_agents()
    strategy = KeywordRoutingStrategy()
    router = RouterAgent(agents=agents, strategy=strategy)

    result = router.strategy.choose_agent("please help me with math", router.agents)
    assert result == "MathAgent"
    response = router.generate_response("calculate 2 + 2")
    assert response.startswith("ECHO:")


def test_keyword_routing_strategy_falls_back_to_default():
    manager = ConfigManager(str(get_config_path()))
    agents = manager.instantiate_agents()
    strategy = KeywordRoutingStrategy()
    router = RouterAgent(agents=agents, strategy=strategy)

    result = router.strategy.choose_agent("tell me a joke", router.agents)
    assert result == "DefaultAgent"
    response = router.generate_response("hello")
    assert response.startswith("ECHO:")
