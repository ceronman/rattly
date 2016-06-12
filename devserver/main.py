import os
import os.path

import aiohttp
import asyncio

from watchdog import observers, events
from aiohttp import web


def localfile(path):
    return os.path.join(os.path.dirname(__file__), path)


async def run_transcrypt(filename):
    path = os.path.abspath(filename)
    parent = os.path.dirname(path)
    base = os.path.basename(path)
    current_dir = os.getcwd()
    os.chdir(parent)
    proc = await asyncio.create_subprocess_exec('transcrypt', '-nb', base)
    await proc.wait()
    os.chdir(current_dir)


class FileWatcher(events.PatternMatchingEventHandler):
    def __init__(self, ws):
        super().__init__(['*.py'])
        self._loop = asyncio.get_event_loop()
        self._ws = ws

    def on_any_event(self, event):
        print('EVENT:', repr(event))
        self._loop.call_soon_threadsafe(asyncio.async, self.compile())

    async def compile(self):
        print('COMPILE')
        self._ws.send_str('RELOAD')


async def root_handler(request):
    await run_transcrypt(localfile('clientside/reload.py'))
    template = open(localfile('templates/index.html'), 'rb')
    return web.Response(body=template.read())


async def compile_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    observer = observers.Observer()
    observer.schedule(FileWatcher(ws), '.', recursive=True)
    observer.start()

    async for msg in ws:
        if msg.tp == aiohttp.MsgType.text:
            if msg.data == 'close':
                await ws.close()
            else:
                ws.send_str(msg.data + '/answer')
        elif msg.tp == aiohttp.MsgType.error:
            print('ws connection closed with exception %s' % ws.exception())

    print('websocket connection closed')
    observer.stop()
    observer.join()

    return ws


app = web.Application()
app.router.add_route('GET', '/', root_handler)
app.router.add_route('GET', '/compiler', compile_handler)
app.router.add_static('/js', localfile('clientside/__javascript__'))

web.run_app(app)
