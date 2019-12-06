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
        renderEngine.drawRect(x, y, x + self.cell_width, y + self.cell_width, '#a8a8a8')

        if self.rotation:
            renderEngine.drawRect(x, y, x + self.border, y + self.cell_width, 'gray')
            renderEngine.drawRect(x + self.cell_width, y, x + self.cell_width - self.border, y + self.cell_width, 'gray')

        else:
            renderEngine.drawRect(x, y, x + self.cell_width, y + self.border, 'gray')
            renderEngine.drawRect(x, y + self.cell_width - self.border, x + self.cell_width, y + self.cell_width, 'gray')

class Intersection(Road):
    def __init__(self, cellX, cellY, cell_width):
        super().__init__(cellX, cellY, cell_width)
        self.icon = '#'

    def draw(self, renderEngine):
        x = self.cellX * self.cell_width
        y = self.cellY * self.cell_width
        #Background
        renderEngine.drawRect(x, y, x + self.cell_width, y + self.cell_width, color = 'orange')

def roadBuilder(road_type, cellX, cellY, cell_width, rotation = 1):
    if road_type == '=':
        return StraightRoad(cellX, cellY, cell_width, rotation = True )
    if road_type == '|':
        return StraightRoad(cellX, cellY, cell_width, rotation = False )
    if road_type == '#':
        return Intersection(cellX, cellY, cell_width)


