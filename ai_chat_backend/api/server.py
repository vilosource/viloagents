from pathlib import Path

from fastapi import FastAPI, WebSocket

from ..router.router_agent import RouterAgent

app = FastAPI()
CONFIG_PATH = Path(__file__).resolve().parents[2] / "agents.yaml"
router_agent = RouterAgent.from_config(str(CONFIG_PATH))

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        msg = await websocket.receive_text()
        response = router_agent.generate_response(msg)
        await websocket.send_text(response)
