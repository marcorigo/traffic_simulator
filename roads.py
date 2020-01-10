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
        self.traffic_light_border_size = 1
        self.traffic_light_border_color = (96, 96, 96)
    
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

    def topTrafficLight(self, renderEngine, color, radious):
        renderEngine.drawCircle(self.x + self.cell_width / 2, self.y + self.traffic_light_border_size, radious, color, self.traffic_light_border_size, self.traffic_light_border_color)

    def bottomTrafficLight(self, renderEngine, color, radious):
        renderEngine.drawCircle(self.x + self.cell_width / 2, self.y + self.cell_width - radious - self.traffic_light_border_size, radious, color, self.traffic_light_border_size, self.traffic_light_border_color)

    def leftTrafficLight(self, renderEngine, color, radious):
        renderEngine.drawCircle(int(self.x + self.traffic_light_border_size), int(self.y + self.cell_width / 2), radious, color, self.traffic_light_border_size, self.traffic_light_border_color)

    def rightTrafficLight(self, renderEngine, color, radious):
        renderEngine.drawCircle(int(self.x + self.cell_width - radious - self.traffic_light_border_size), int(self.y + self.cell_width / 2), radious, color, self.traffic_light_border_size, self.traffic_light_border_color)

class StraightRoad(Road):
    def __init__(self, cellX, cellY, cell_width, border, road_type, rotation = True):
        super().__init__(cellX, cellY, cell_width, border, road_type)
        self.rotation = rotation

    def draw(self, renderEngine):

        #Background
        renderEngine.drawRect(self.x, self.y, self.cell_width, self.cell_width, (170, 170, 170))

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
        self.change_time = random.randint(15, 30)
        self.last_change = int(time.time())
        self.yellow_light_time = 2
        self.x_light = 'green'
        self.y_light = 'red'
        self.changing = 1
        self.road_allowed = [1, 3]

    def can(self, veichle):
        if veichle.facing in self.road_allowed:
            return True
        return False

    def checkTrafficLight(self):
        now = int(time.time())

        if self.last_change + self.change_time < now:
            self.last_change = now

            if self.changing == 1:
                self.x_light = 'yellow'
                self.changing = 2
                self.road_allowed = [0]
            else:
                self.y_light = 'yellow'
                self.changing = 1
                self.road_allowed = [0]
        
        if self.last_change + self.yellow_light_time < now:
            if self.changing == 1:
                self.y_light = 'red'
                self.x_light = 'green'
                self.road_allowed = [2, 4]
            else:
                self.x_light = 'red'
                self.y_light = 'green'
                self.road_allowed = [1, 3]

    def draw(self, renderEngine):
        self.checkTrafficLight()

        #Background
        renderEngine.drawRect(self.x, self.y, self.cell_width, self.cell_width, (170, 170, 170))

        self.topLeftSideWalk(renderEngine)
        self.topRightSideWalk(renderEngine)
        self.bottomLeftSideWalk(renderEngine)
        self.bottomRightSideWalk(renderEngine)

        # Draw traffic light
        self.topTrafficLight(renderEngine, self.colors[self.y_light], self.light_radious)
        self.bottomTrafficLight(renderEngine, self.colors[self.y_light], self.light_radious)
        self.leftTrafficLight(renderEngine, self.colors[self.x_light], self.light_radious)
        self.rightTrafficLight(renderEngine, self.colors[self.x_light], self.light_radious)

class TRoad(Road):
    def __init__(self, cellX, cellY, cell_width, border, road_type, rotation = 0):
        super().__init__(cellX, cellY, cell_width, border, road_type)
        self.rotation = rotation
        self.colors = {
            'red' : (255, 0, 0),
            'yellow': (247, 228, 86),
            'green': (87, 226, 40)
        }
        self.light_radious = self.cell_width / 15
        self.change_time = random.randint(15, 30)
        self.last_change = int(time.time())
        self.yellow_light_time = 2
        self.x_light = 'green'
        self.y_light = 'red'
        self.changing = 1

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
        now = int(time.time())

        if self.last_change + self.change_time < now:
            self.last_change = now

            if self.changing == 1:
                self.x_light = 'yellow'
                self.changing = 2
                self.road_allowed = [0]
            else:
                self.y_light = 'yellow'
                self.changing = 1
                self.road_allowed = [0]
        
        if self.last_change + self.yellow_light_time < now:
            if self.changing == 1:
                self.y_light = 'red'
                self.x_light = 'green'
                self.road_allowed = self.facing_x_axes
            else:
                self.x_light = 'red'
                self.y_light = 'green'
                self.road_allowed = self.facing_y_axes


    def draw(self, renderEngine):
        self.checkTrafficLight()

        # Background
        renderEngine.drawRect(self.x, self.y, self.cell_width, self.cell_width, (170, 170, 170))

        # ╩
        if self.rotation == 1:
            self.topLeftSideWalk(renderEngine)
            self.topRightSideWalk(renderEngine)
            self.bottomSideWalk(renderEngine)
            self.orizontalRoadLines(renderEngine)

            # Draw traffic light
            self.topTrafficLight(renderEngine, self.colors[self.y_light], self.light_radious)
            self.leftTrafficLight(renderEngine, self.colors[self.x_light], self.light_radious)
            self.rightTrafficLight(renderEngine, self.colors[self.x_light], self.light_radious)

        # ╠
        if self.rotation == 2:
            self.leftSideWalk(renderEngine)
            self.topRightSideWalk(renderEngine)
            self.bottomRightSideWalk(renderEngine)
            self.verticalRoadLines(renderEngine)

            # Draw traffic light
            self.topTrafficLight(renderEngine, self.colors[self.y_light], self.light_radious)
            self.bottomTrafficLight(renderEngine, self.colors[self.y_light], self.light_radious)
            self.rightTrafficLight(renderEngine, self.colors[self.x_light], self.light_radious)

        # ╦
        if self.rotation == 3:
            self.topSideWalk(renderEngine)
            self.bottomRightSideWalk(renderEngine)
            self.bottomLeftSideWalk(renderEngine)
            self.orizontalRoadLines(renderEngine)

            # Draw traffic light
            self.bottomTrafficLight(renderEngine, self.colors[self.y_light], self.light_radious)
            self.leftTrafficLight(renderEngine, self.colors[self.x_light], self.light_radious)
            self.rightTrafficLight(renderEngine, self.colors[self.x_light], self.light_radious)

        # ╣
        if self.rotation == 4:
            self.rightSideWalk(renderEngine)
            self.topLeftSideWalk(renderEngine)
            self.bottomLeftSideWalk(renderEngine)
            self.verticalRoadLines(renderEngine)

            # Draw traffic light
            self.topTrafficLight(renderEngine, self.colors[self.y_light], self.light_radious)
            self.bottomTrafficLight(renderEngine, self.colors[self.y_light], self.light_radious)
            self.leftTrafficLight(renderEngine, self.colors[self.x_light], self.light_radious)

class Curve(Road):
    def __init__(self, cellX, cellY, cell_width, border, road_type, rotation = 0):
        super().__init__(cellX, cellY, cell_width, border, road_type)
        self.rotation = rotation

    def draw(self, renderEngine):

        #Background
        renderEngine.drawRect(self.x, self.y, self.cell_width, self.cell_width, (170, 170, 170))

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
    if road_type == '╩':
        return TRoad(cellX, cellY, cell_width, border, road_type, rotation = 1 )
    if road_type == '╠':
        return TRoad(cellX, cellY, cell_width, border, road_type, rotation = 2 )
    if road_type == '╦':
        return TRoad(cellX, cellY, cell_width, border, road_type, rotation = 3 )
    if road_type == '╣':
        return TRoad(cellX, cellY, cell_width, border, road_type, rotation = 4 )
    return 0


