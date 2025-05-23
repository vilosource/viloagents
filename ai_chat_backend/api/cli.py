from ..router.router_agent import RouterAgent

router_agent = RouterAgent()

def main():
    print("Enter text (type 'exit' to quit):")
    while True:
        text = input('> ')
        if text.lower() == 'exit':
            break
        print(router_agent.generate_response(text))

if __name__ == '__main__':
    main()
