class Road:
    def __init__(self, cellX, cellY, cell_width, side_walk):
        self.cellX = cellX
        self.cellY = cellY
        self.cell_width = cell_width
        self.border = side_walk

class StraightRoad(Road):
    def __init__(self, cellX, cellY, cell_width, border, rotation = True):
        super().__init__(cellX, cellY, cell_width, border)
        self.rotation = rotation
        self.icon = '='

    def draw(self, renderEngine):
        x = self.cellX * self.cell_width
        y = self.cellY * self.cell_width
        #Background
        renderEngine.drawRect(x, y, self.cell_width, self.cell_width, (170, 170, 170))

        if self.rotation:
            renderEngine.drawRect(x, y, self.border, self.cell_width, (94, 94, 94))
            renderEngine.drawRect(x + self.cell_width - self.border, y, self.border, self.cell_width, (94, 94, 94))

        else:
            renderEngine.drawRect(x, y, self.cell_width, self.border, (94, 94, 94))
            renderEngine.drawRect(x, y + self.cell_width - self.border, self.cell_width, self.border, (94, 94, 94))

class Intersection(Road):
    def __init__(self, cellX, cellY, cell_width, border):
        super().__init__(cellX, cellY, cell_width, border)
        self.icon = '#'

    def draw(self, renderEngine):
        x = self.cellX * self.cell_width
        y = self.cellY * self.cell_width
        #Background
        renderEngine.drawRect(x, y, self.cell_width, self.cell_width, (170, 170, 170))

def roadBuilder(road_type, cellX, cellY, cell_width, border, rotation = True):
    if road_type == '=':
        return StraightRoad(cellX, cellY, cell_width, border, rotation = True )
    if road_type == '|':
        return StraightRoad(cellX, cellY, cell_width, border, rotation = False )
    if road_type == '#':
        return Intersection(cellX, cellY, cell_width, border)
    return 0


