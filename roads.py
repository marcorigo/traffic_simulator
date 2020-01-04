import time
import random

class Road:
    def __init__(self, cellX, cellY, cell_width, side_walk, road_type):
        self.cellX = cellX
        self.cellY = cellY
        self.cell_width = cell_width
        self.border = side_walk
        self.x = self.cellX * self.cell_width
        self.y = self.cellY * self.cell_width
        self.side_walk_color = (94, 94, 94)
        self.road_type = road_type

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

    def topBottomTrafficLight(self, renderEngine, color, radious):
        renderEngine.drawCircle(self.x + self.cell_width / 2, self.y, radious, color)
        renderEngine.drawCircle(self.x + self.cell_width / 2, self.y + self.cell_width - radious, radious, color)

    def leftRightTrafficLight(self, renderEngine, color, radious):
        renderEngine.drawCircle(int(self.x), int(self.y + self.cell_width / 2), radious, color)
        renderEngine.drawCircle(int(self.x + self.cell_width - radious), int(self.y + self.cell_width / 2), radious, color)

class StraightRoad(Road):
    def __init__(self, cellX, cellY, cell_width, border, road_type, rotation = True):
        super().__init__(cellX, cellY, cell_width, border, road_type)
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
    def __init__(self, cellX, cellY, cell_width, border, road_type):
        super().__init__(cellX, cellY, cell_width, border, road_type)
        self.colors = {
            'red' : (255, 0, 0),
            'yellow': (247, 228, 86),
            'green': (87, 226, 40)
        }
        self.light_radious = self.cell_width / 15
        self.change_time = random.randint(5, 10)
        self.last_change = int(time.time())
        self.yellow_light_time = 2
        self.x_light = 'green'
        self.y_light = 'red'
        self.changing = 1
        self.road_allowed = [1, 3]

    def checkTrafficLight(self):
        now = int(time.time())

        if self.last_change + self.change_time < now:
            self.last_change = now

            if self.changing == 1:
                self.x_light = 'yellow'
                self.changing = 2
            else:
                self.y_light = 'yellow'
                self.changing = 1
        
        if self.last_change + self.yellow_light_time < now:
            if self.changing == 1:
                self.y_light = 'red'
                self.x_light = 'green'
                self.road_allowed = [1, 3]
            else:
                self.x_light = 'red'
                self.y_light = 'green'
                self.road_allowed = [2, 4]




    def draw(self, renderEngine):
        self.checkTrafficLight()

        x = self.cellX * self.cell_width
        y = self.cellY * self.cell_width
        #Background
        renderEngine.drawRect(x, y, self.cell_width, self.cell_width, (170, 170, 170))

        self.topLeftSideWalk(renderEngine)
        self.topRightSideWalk(renderEngine)
        self.bottomLeftSideWalk(renderEngine)
        self.bottomRightSideWalk(renderEngine)

        # Draw traffic light
        self.topBottomTrafficLight(renderEngine, self.colors[self.y_light], self.light_radious)
        self.leftRightTrafficLight(renderEngine, self.colors[self.x_light], self.light_radious)

class Curve(Road):
    def __init__(self, cellX, cellY, cell_width, border, road_type, rotation = 0):
        super().__init__(cellX, cellY, cell_width, border, road_type)
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
    if road_type == '═' or road_type == '➡' or road_type == '⬅':
        return StraightRoad(cellX, cellY, cell_width, border, road_type, rotation = True )
    if road_type == '║' or road_type == '⬆' or road_type == '⬇':
        return StraightRoad(cellX, cellY, cell_width, border, road_type, rotation = False )
    if road_type == '╬':
        return Intersection(cellX, cellY, cell_width, border, road_type)
    if road_type == '╔':
        return Curve(cellX, cellY, cell_width, border, road_type, rotation = 1 )
    if road_type == '╚':
        return Curve(cellX, cellY, cell_width, border, road_type, rotation = 2 )
    if road_type == '╗':
        return Curve(cellX, cellY, cell_width, border, road_type, rotation = 3 )
    if road_type == '╝':
        return Curve(cellX, cellY, cell_width, border, road_type, rotation = 4 )
    return 0


