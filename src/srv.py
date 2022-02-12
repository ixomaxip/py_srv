import logging
import asyncio
import json
from datetime import datetime
from aiohttp import web
from aiohttp.web_exceptions import HTTPException

from config import config, logger


START_TIME = datetime.now()


routes = web.RouteTableDef()

@routes.get('/ping')
async def ping(request: web.Request):
    return web.Response(text='pong')

@routes.get('/info')
@routes.post('/info')
async def info(request: web.Request):
    resp = {'hostname': config.hostname, 'up_time': str(datetime.now() - START_TIME)}
    logging.info(json.dumps(resp))

    return web.json_response(resp)

app = web.Application(logger=logger)
app.add_routes(routes)

loop = asyncio.get_event_loop()

if __name__ == '__main__':
    web.run_app(app, host=config.bind_host, port=config.bind_port)
