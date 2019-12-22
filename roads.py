class Road:
    def __init__(self, cellX, cellY, cell_width, side_walk):
        self.cellX = cellX
        self.cellY = cellY
        self.cell_width = cell_width
        self.border = side_walk
        self.x = self.cellX * self.cell_width
        self.y = self.cellY * self.cell_width
        self.side_walk_color = (94, 94, 94)

        self.road_line_quantity = 5
        self.road_line_height = (self.cell_width - self.border * 2) / 15
        self.road_line_section = int(self.cell_width / self.road_line_quantity)
        self.road_line_width = int((self.cell_width / self.road_line_quantity) / 2)
    
    def leftSideWalk(self, renderEngine):
        renderEngine.drawRect(self.x, self.y, self.border, self.cell_width, self.side_walk_color)

    def rightSideWalk(self, renderEngine):
        renderEngine.drawRect(self.x + self.cell_width - self.border, self.y, self.border, self.cell_width, self.side_walk_color)

    def topSideWalk(self, renderEngine):
        renderEngine.drawRect(self.x, self.y, self.cell_width, self.border, self.side_walk_color)
    
    def bottomSideWalk(self, renderEngine):
        renderEngine.drawRect(self.x, self.y + self.cell_width - self.border, self.cell_width, self.border, self.side_walk_color)

    def topLeftSideWalk(self,renderEngine):
        renderEngine.drawRect(self.x, self.y, self.border, self.border, self.side_walk_color)

    def topRightSideWalk(self, renderEngine):
        renderEngine.drawRect(self.x + self.cell_width - self.border, self.y, self.border, self.border, self.side_walk_color)

    def bottomLeftSideWalk(self, renderEngine):
        renderEngine.drawRect(self.x, self.y + self.cell_width - self.border, self.border, self.border, self.side_walk_color)

    def bottomRightSideWalk(self, renderEngine):
        renderEngine.drawRect(self.x + self.cell_width  - self.border, self.y + self.cell_width - self.border, self.border, self.border, self.side_walk_color)

    def orizontalRoadLines(self, renderEngine):
        for i in range(self.road_line_quantity):
            renderEngine.drawRect(self.x + self.road_line_section * i, self.y + self.cell_width / 2 - self.road_line_height / 2, self.road_line_width, self.road_line_height, (242, 242, 242))
        
    def verticalRoadLines(self, renderEngine):
        for i in range(self.road_line_quantity):
            renderEngine.drawRect(self.x + self.cell_width / 2 - self.road_line_height / 2, self.y + self.road_line_section * i, self.road_line_height, self.road_line_width, (242, 242, 242))

class StraightRoad(Road):
    def __init__(self, cellX, cellY, cell_width, border, rotation = True):
        super().__init__(cellX, cellY, cell_width, border)
        self.rotation = rotation

    def draw(self, renderEngine):
        x = self.cellX * self.cell_width
        y = self.cellY * self.cell_width
        #Background
        renderEngine.drawRect(x, y, self.cell_width, self.cell_width, (170, 170, 170))

        # ═
        if self.rotation:
            self.topSideWalk(renderEngine)
            self.bottomSideWalk(renderEngine)
            self.orizontalRoadLines(renderEngine)

        # ║
        else:
            self.rightSideWalk(renderEngine)
            self.leftSideWalk(renderEngine)
            self.verticalRoadLines(renderEngine)

class Intersection(Road):
    def __init__(self, cellX, cellY, cell_width, border):
        super().__init__(cellX, cellY, cell_width, border)

    def draw(self, renderEngine):
        x = self.cellX * self.cell_width
        y = self.cellY * self.cell_width
        #Background
        renderEngine.drawRect(x, y, self.cell_width, self.cell_width, (170, 170, 170))

        self.topLeftSideWalk(renderEngine)
        self.topRightSideWalk(renderEngine)
        self.bottomLeftSideWalk(renderEngine)
        self.bottomRightSideWalk(renderEngine)

class Curve(Road):
    def __init__(self, cellX, cellY, cell_width, border, rotation = 0):
        super().__init__(cellX, cellY, cell_width, border)
        self.rotation = rotation

    def draw(self, renderEngine):
        x = self.cellX * self.cell_width
        y = self.cellY * self.cell_width
        #Background
        renderEngine.drawRect(x, y, self.cell_width, self.cell_width, (170, 170, 170))

        # ╔
        if self.rotation == 1:
            self.leftSideWalk(renderEngine)
            self.topSideWalk(renderEngine)
            self.bottomRightSideWalk(renderEngine)

        # ╚
        if self.rotation == 2:
            self.leftSideWalk(renderEngine)
            self.bottomSideWalk(renderEngine)
            self.topRightSideWalk(renderEngine)


        # ╗
        if self.rotation == 3:
            self.topSideWalk(renderEngine)
            self.rightSideWalk(renderEngine)
            self.bottomLeftSideWalk(renderEngine)

        #  ╝ 
        if self.rotation == 4:
            self.rightSideWalk(renderEngine)
            self.bottomSideWalk(renderEngine)
            self.topLeftSideWalk(renderEngine)



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


