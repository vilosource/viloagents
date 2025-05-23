from fastapi import FastAPI, WebSocket

from ..router.router_agent import RouterAgent

app = FastAPI()
router_agent = RouterAgent()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        msg = await websocket.receive_text()
        response = router_agent.generate_response(msg)
        await websocket.send_text(response)
