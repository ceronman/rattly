# This should be monitored by watchdog
# This should work
class GameLoop:
    def __init__(self, selector):
        container = document.querySelector(selector)
        canvas = document.createElement('canvas')
        context = canvas.getContext('2d')
        canvas.width = 640
        canvas.height = 480
        canvas.style.backgroundColor = 'black'
        container.appendChild(canvas)