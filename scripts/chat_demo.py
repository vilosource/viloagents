from pathlib import Path

from ai_chat_backend.router.router_agent import RouterAgent

CONFIG_PATH = Path(__file__).resolve().parents[1] / "agents.yaml"


def main() -> None:
    router = RouterAgent.from_config(str(CONFIG_PATH))
    print("Type messages (enter 'exit' to quit):")
    while True:
        msg = input('> ')
        if msg.lower() == 'exit':
            break
        print(router.generate_response(msg))


if __name__ == "__main__":
    main()
