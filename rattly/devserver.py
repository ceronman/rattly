ws = None

def start():
    console.log('starting webserver')
    ws = __new__(WebSocket("ws://127.0.0.1:8080/compiler"))
    ws.onmessage = lambda e: document.location.reload()