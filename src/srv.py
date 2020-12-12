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
from datetime import datetime

from aiohttp import web
from aiohttp.web_exceptions import HTTPException

log = utils.get_logger('srv', sys.stdout, debug_level=config.debug)

up_time = datetime.now()

routes = web.RouteTableDef()

@routes.get('/ping')
async def ping(request: web.Request):
    return web.Response(text='pong')

@routes.get('/info')
@routes.post('/info')
async def info(request: web.Request):
    resp = {'hostname': config.hostname, 'up_time': str(datetime.now() - up_time)}
    log.info(json.dumps(resp))

    return web.json_response(resp)


app = web.Application(logger=log)
app.add_routes(routes)

loop = asyncio.get_event_loop()
loop.set_debug(config.debug)

if __name__ == '__main__':
    web.run_app(app, port=config.port)
