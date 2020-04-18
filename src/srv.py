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

from aiohttp import web
from aiohttp.web_exceptions import HTTPException

def get_logger(name: str, stdout: _io.TextIOWrapper) -> logging.Logger:
    log = logging.getLogger(name)

    h = logging.StreamHandler(stream=stdout)
    h.setFormatter(logging.Formatter('%(message)s'))
    h.flush = stdout.flush
    log.addHandler(h)
    log.setLevel(logging.INFO)
    return log

log = get_logger('srv', sys.stdout)
log.setLevel(config.debug)

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
