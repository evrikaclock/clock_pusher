from clock_pusher import app
import json
import time


@app.websocket('/')
async def sync(_, ws):
    with open(r"..\clock_pusher\state.bd", 'r') as f:
        state = json.load(f)
        current_revision = int(state["revision"])

    while True:
        with open(r"..\clock_pusher\state.bd", 'r') as f:
            try:
                state = json.load(f)
            except Exception as e:
                print(e)
                time.sleep(5)
        if int(state["revision"]) > current_revision:
            current_revision = int(state["revision"])
            s_state = json.dumps(state)
            await ws.send(s_state)
        time.sleep(1)
