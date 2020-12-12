import config
import io
import _io
import logging
import sys
import asyncio
import aiohttp
import json
import os
import time
import numpy as np
import tools.utils as utils

from aiohttp import web
from aiohttp.web_exceptions import HTTPException

log = utils.get_logger('srv', sys.stdout, debug_level=config.debug)

routes = web.RouteTableDef()

@routes.get('/ping')
async def ping(request: web.Request)):
    return web.Response(text='pong')


app = web.Application(logger=log)
app.add_routes(routes)

loop = asyncio.get_event_loop()
loop.set_debug(config.debug)

if __name__ == '__main__':
    web.run_app(app, port=config.port)
