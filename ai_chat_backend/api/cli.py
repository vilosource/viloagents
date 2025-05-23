from pathlib import Path

from ..router.router_agent import RouterAgent

CONFIG_PATH = Path(__file__).resolve().parents[2] / "agents.yaml"
router_agent = RouterAgent.from_config(str(CONFIG_PATH))

def main():
    print("Enter text (type 'exit' to quit):")
    while True:
        text = input('> ')
        if text.lower() == 'exit':
            break
        print(router_agent.generate_response(text))

if __name__ == '__main__':
    main()
