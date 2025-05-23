import pathlib
import sys
from types import SimpleNamespace

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from ai_chat_backend.agents.default_agent import DefaultAgent
from ai_chat_backend.agents.base import ChatOpenAI

class DummyLLM:
    def __init__(self, *args, **kwargs):
        pass

    def invoke(self, messages):
        return SimpleNamespace(content="LLM Response")


def test_default_agent_uses_llm(monkeypatch):
    monkeypatch.setattr('ai_chat_backend.agents.base.ChatOpenAI', DummyLLM)
    agent = DefaultAgent()
    assert agent.generate_response('hi') == 'LLM Response'
