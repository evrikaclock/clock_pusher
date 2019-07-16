from clock_pusher import app
import json
import time
import datetime


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
            release_day = datetime.datetime.strptime(state["release_day"], "%d.%m.%Y %X")
            now = datetime.datetime.now()
            total_seconds = int((now - release_day).total_seconds())

            current_revision = int(state["revision"])
            s_state = json.dumps({
                "total_seconds": total_seconds,
                "last_service": state["last_service"],
                "services_count": state["services_count"]
            })
            await ws.send(s_state)
        time.sleep(1)
