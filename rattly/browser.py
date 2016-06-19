# flake8: noqa
__pragma__('skip')
__new__ = WebSocket = document = None
__pragma__('noskip')


def start_reloader():
    print('starting webserver')
    ws = __new__(WebSocket("ws://127.0.0.1:8080/compiler"))
    ws.onmessage = lambda e: browser.reload()

def create_canvas(selector):
    container = document.querySelector(selector)
    canvas = document.createElement('canvas')
    container.appendChild(canvas)
    return canvas
    