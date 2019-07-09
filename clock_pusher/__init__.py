from sanic import Sanic

app = Sanic(__name__)

import clock_pusher.controllers
