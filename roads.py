class Road:
    def __init__(self, cellX, cellY, cell_width):
        self.cellX = cellX
        self.cellY = cellY
        self.cell_width = cell_width
        self.border = int(self.cell_width / 8)

class StraightRoad(Road):
    def __init__(self, cellX, cellY, cell_width, rotation = 1):
        super().__init__(cellX, cellY, cell_width)
        self.rotation = rotation
        self.icon = '='

    def draw(self, renderEngine):
        x = self.cellX * self.cell_width
        y = self.cellY * self.cell_width
        #Background
        renderEngine.drawRect(x, y, x + self.cell_width, y + self.cell_width, (170, 170, 170))

        if self.rotation:
            renderEngine.drawRect(x, y, x + self.border, y + self.cell_width, (94, 94, 94))
            renderEngine.drawRect(x + self.cell_width - self.border, y, self.border, self.cell_width, (94, 94, 94))

        # else:
        #     renderEngine.drawRect(x, y, x + self.cell_width, y + self.border, (94, 94, 94))
        #     renderEngine.drawRect(x, y + self.cell_width - self.border, x + self.cell_width, y + self.cell_width, (94, 94, 94))

class Intersection(Road):
    def __init__(self, cellX, cellY, cell_width):
        super().__init__(cellX, cellY, cell_width)
        self.icon = '#'

    def draw(self, renderEngine):
        x = self.cellX * self.cell_width
        y = self.cellY * self.cell_width
        #Background
        renderEngine.drawRect(x, y, x + self.cell_width, y + self.cell_width, (237, 146, 28))

def roadBuilder(road_type, cellX, cellY, cell_width, rotation = True):
    if road_type == '=':
        return StraightRoad(cellX, cellY, cell_width, rotation = True )
    if road_type == '|':
        return StraightRoad(cellX, cellY, cell_width, rotation = False )
    if road_type == '#':
        return Intersection(cellX, cellY, cell_width)
    return 0


