class RenderEngine:
    def __init__(self, canvas, width, heigth):
        self.canvas = canvas
        self.width = width
        self.heigth = heigth

    def drawRect(self, x, y, width, heigth, color):
        return self.canvas.create_rectangle(x, y, width, heigth, fill = color)

    def move(self, element, x = 0, y = 0):
        self.canvas.move(element, x, y)
