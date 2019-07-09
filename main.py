from clock_pusher import app
from sanic.websocket import WebSocketProtocol

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7676, protocol=WebSocketProtocol, debug=True)
