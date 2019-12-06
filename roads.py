class Road:
    def __init__(self, cellX, cellY, cell_width):
        self.cellX = cellX
        self.cellY = cellY
        self.cell_width = cell_width

class StraightRoad(Road):
    def __init__(self, cellX, cellY, cell_width):
        super().__init__(cellX, cellY, cell_width)
        self.icon = '='

    def draw(self, canvas):
        x = self.cellX * self.cell_width
        y = self.cellY * self.cell_width
        #Background
        canvas.create_rectangle(x, y, x + self.cell_width, y + self.cell_width, fill = 'green')

