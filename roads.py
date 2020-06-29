#import time
#import random
import traffic_light as tf
from const import config

class Road:
    def __init__(self, cellX, cellY, cell_width, side_walk, road_type):
        self.cellX = cellX
        self.cellY = cellY
        self.cell_width = cell_width
        self.border = side_walk
        self.x = self.cellX * self.cell_width
        self.y = self.cellY * self.cell_width
        self.side_walk_color = config.SIDE_WALK_COLOR
        self.road_type = road_type
        self.road_line_quantity = config.ROAD_LINE_QUANTITY
        self.road_line_height = (self.cell_width - self.border * 2) / 15
        self.road_line_section = int(self.cell_width / self.road_line_quantity)
        self.road_line_width = int((self.cell_width / self.road_line_quantity) / 2)
        self.road_background = config.ROAD_COLOR
        self.useTextures = config.USE_TEXTURES


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
    def __init__(self, cellX, cellY, cell_width, border, road_type, rotation = True):
        super().__init__(cellX, cellY, cell_width, border, road_type)
        self.rotation = rotation

    def draw(self, renderEngine):

        if self.useTextures:
            return

        #Background
        renderEngine.drawRect(self.x, self.y, self.cell_width, self.cell_width, self.road_background)

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
        self.road_allowed = [1, 3]
        self.traffic_light = tf.TrafficLight(cell_width)



    def can(self, veichle):
        if veichle.facing in self.road_allowed:
            return True
        return False

    def checkTrafficLight(self):
        self.traffic_light.update()

    def draw(self, renderEngine):
        self.checkTrafficLight()

        if self.useTextures:
            self.drawTrafficLights(renderEngine)
            return

        #Background
        renderEngine.drawRect(self.x, self.y, self.cell_width, self.cell_width, self.road_background)

        self.topLeftSideWalk(renderEngine)
        self.topRightSideWalk(renderEngine)
        self.bottomLeftSideWalk(renderEngine)
        self.bottomRightSideWalk(renderEngine)

        # Draw traffic lights
        self.drawTrafficLights(renderEngine)

    def drawTrafficLights(self, renderEngine):
        self.traffic_light.draw(renderEngine,self)
    #     self.traffic_light.top(renderEngine, self.traffic_light.colors[self.traffic_light.y_light], self.traffic_light.radius)
    #     self.traffic_light.bottom(renderEngine, self.traffic_light.colors[self.traffic_light.y_light], self.traffic_light.radius)
    #     self.traffic_light.left(renderEngine, self.traffic_light.colors[self.traffic_light.x_light], self.traffic_light.radius)
    #     self.traffic_light.right(renderEngine, self.traffic_light.colors[self.traffic_light.x_light], self.traffic_light.radius)

class TRoad(Road):
    def __init__(self, cellX, cellY, cell_width, border, road_type, rotation = 0):
        super().__init__(cellX, cellY, cell_width, border, road_type)
        self.rotation = rotation
        self.traffic_light = tf.TrafficLight(cell_width)
        if self.rotation == 1:
            self.facing_x_axes = [2, 4]
            self.facing_y_axes = [3]
        
        if self.rotation == 2:
            self.facing_x_axes = [4]
            self.facing_y_axes = [1, 3]
        
        if self.rotation == 3:
            self.facing_x_axes = [2, 4]
            self.facing_y_axes = [1]
        
        if self.rotation == 4:
            self.facing_x_axes = [2]
            self.facing_y_axes = [1, 3]

        self.road_allowed = self.facing_y_axes

    def can(self, veichle):
        if veichle.facing in self.road_allowed:
            return True
        return False

    def checkTrafficLight(self):
        self.traffic_light.update()

    def draw(self, renderEngine):
        self.checkTrafficLight()

        if self.useTextures:
            self.drawTrafficLights(renderEngine)
            return

        # Background
        renderEngine.drawRect(self.x, self.y, self.cell_width, self.cell_width, self.road_background)

        # ╩
        if self.rotation == 1:
            self.topLeftSideWalk(renderEngine)
            self.topRightSideWalk(renderEngine)
            self.bottomSideWalk(renderEngine)
            self.orizontalRoadLines(renderEngine)

        # ╠
        if self.rotation == 2:
            self.leftSideWalk(renderEngine)
            self.topRightSideWalk(renderEngine)
            self.bottomRightSideWalk(renderEngine)
            self.verticalRoadLines(renderEngine)

        # ╦
        if self.rotation == 3:
            self.topSideWalk(renderEngine)
            self.bottomRightSideWalk(renderEngine)
            self.bottomLeftSideWalk(renderEngine)
            self.orizontalRoadLines(renderEngine)

        # ╣
        if self.rotation == 4:
            self.rightSideWalk(renderEngine)
            self.topLeftSideWalk(renderEngine)
            self.bottomLeftSideWalk(renderEngine)
            self.verticalRoadLines(renderEngine)

        self.drawTrafficLights(renderEngine)

    def drawTrafficLights(self, renderEngine):
        self.traffic_light.draw(renderEngine,self,self.rotation)

class Curve(Road):
    def __init__(self, cellX, cellY, cell_width, border, road_type, rotation = 0):
        super().__init__(cellX, cellY, cell_width, border, road_type)
        self.rotation = rotation

    def draw(self, renderEngine):

        if self.useTextures:
            return

        #Background
        renderEngine.drawRect(self.x, self.y, self.cell_width, self.cell_width, self.road_background)

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

class Grass(Road):
    def __init__(self, cellX, cellY, cell_width, border, road_type):
        super().__init__(cellX, cellY, cell_width, border, road_type)

    def draw(self, renderEngine):

        if self.useTextures:
            return
        



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
    if road_type == '╩':
        return TRoad(cellX, cellY, cell_width, border, road_type, rotation = 1 )
    if road_type == '╠':
        return TRoad(cellX, cellY, cell_width, border, road_type, rotation = 2 )
    if road_type == '╦':
        return TRoad(cellX, cellY, cell_width, border, road_type, rotation = 3 )
    if road_type == '╣':
        return TRoad(cellX, cellY, cell_width, border, road_type, rotation = 4 )
    if road_type == 0:
        return Grass(cellX, cellY, cell_width, border, road_type )
    return 0


