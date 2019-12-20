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

    def draw(self, renderEngine):
        x = self.cellX * self.cell_width
        y = self.cellY * self.cell_width
        #Background
        renderEngine.drawRect(x, y, self.cell_width, self.cell_width, (170, 170, 170))

        if self.rotation:
            renderEngine.drawRect(x, y, self.cell_width, self.border, (94, 94, 94))
            renderEngine.drawRect(x, y + self.cell_width - self.border, self.cell_width, self.border, (94, 94, 94))

        else:
            renderEngine.drawRect(x, y, self.border, self.cell_width, (94, 94, 94))
            renderEngine.drawRect(x + self.cell_width - self.border, y, self.border, self.cell_width, (94, 94, 94))

class Intersection(Road):
    def __init__(self, cellX, cellY, cell_width, border):
        super().__init__(cellX, cellY, cell_width, border)

    def draw(self, renderEngine):
        x = self.cellX * self.cell_width
        y = self.cellY * self.cell_width
        #Background
        renderEngine.drawRect(x, y, self.cell_width, self.cell_width, (170, 170, 170))

class Curve(Road):
    def __init__(self, cellX, cellY, cell_width, border, rotation = 0):
        super().__init__(cellX, cellY, cell_width, border)
        self.rotation = rotation

    def draw(self, renderEngine):
        x = self.cellX * self.cell_width
        y = self.cellY * self.cell_width
        #Background
        renderEngine.drawRect(x, y, self.cell_width, self.cell_width, (170, 170, 170))

        if self.rotation == 1:
            renderEngine.drawRect(x, y, self.cell_width, self.border, (94, 94, 94))
            renderEngine.drawRect(x, y, self.border, self.cell_width, (94, 94, 94))

        if self.rotation == 2:
            renderEngine.drawRect(x, y + self.cell_width - self.border, self.cell_width, self.border, (94, 94, 94))
            renderEngine.drawRect(x, y, self.border, self.cell_width, (94, 94, 94))

        if self.rotation == 3:
            renderEngine.drawRect(x + self.cell_width - self.border, y, self.border, self.cell_width, (94, 94, 94))
            renderEngine.drawRect(x, y, self.cell_width, self.border, (94, 94, 94))
            
        if self.rotation == 4:
            renderEngine.drawRect(x + self.cell_width - self.border, y, self.border, self.cell_width, (94, 94, 94))
            renderEngine.drawRect(x, y + self.cell_width - self.border, self.cell_width, self.border, (94, 94, 94))



def roadBuilder(road_type, cellX, cellY, cell_width, border, rotation = True):
    if road_type == '═':
        return StraightRoad(cellX, cellY, cell_width, border, rotation = True )
    if road_type == '║':
        return StraightRoad(cellX, cellY, cell_width, border, rotation = False )
    if road_type == '╬':
        return Intersection(cellX, cellY, cell_width, border)
    if road_type == '╔':
        return Curve(cellX, cellY, cell_width, border, rotation = 1 )
    if road_type == '╚':
        return Curve(cellX, cellY, cell_width, border, rotation = 2 )
    if road_type == '╗':
        return Curve(cellX, cellY, cell_width, border, rotation = 3 )
    if road_type == '╝':
        return Curve(cellX, cellY, cell_width, border, rotation = 4 )
    return 0


