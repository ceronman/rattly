from rattly import devserver


class GameLoop:
    def __init__(self, selector):
        devserver.start()
        container = document.querySelector(selector)
        canvas = document.createElement('canvas')
        context = canvas.getContext('2d')
        canvas.width = 640
        canvas.height = 480
        canvas.style.backgroundColor = 'grey'
        context.font = "30px Arial"
        context.fillText("Hello World!", 50, 50)
        container.appendChild(canvas)