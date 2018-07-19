import logging
logging.basicConfig(level=logging.INFO)
import asyncio

from aiohttp import web

# 处理 http 响应


def index(request):
    return web.Response(body=b'<h3> woshimiaojian wo hen kaixin </h3>', content_type='text/html')

# 接口响应并路由


@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', '9999')
    logging.info('start request 127.0.0.1:9999  ....')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
