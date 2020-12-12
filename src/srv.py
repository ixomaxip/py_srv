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
async def ping(request):
    return web.Response(text='pong')

app = web.Application()
app.add_routes(routes)

handler = logging.StreamHandler(sys.stdout)
if config.debug:
    current_lvl = logging.DEBUG
else:
    current_lvl = logging.CRITICAL

for name in logging.root.manager.loggerDict:
    if 'aiohttp.' not in name:
        continue
    logger = logging.getLogger(name)
    logger.setLevel(current_lvl)
    logger.addHandler(handler)

if __name__ == '__main__':
    log.info('Running server')
    web.run_app(app, port=80)
