import rattly.browser as browser


class GameLoop:
    def __init__(self, selector):
        browser.start_reloader()
        canvas = browser.create_canvas(selector)
        context = canvas.getContext('2d')
        canvas.width = 640
        canvas.height = 480
        canvas.style.backgroundColor = 'grey'
        context.font = "30px Arial"
        context.fillText("Hello World!", 50, 150)
