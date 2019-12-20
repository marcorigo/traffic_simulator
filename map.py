from car import Car
from roads import roadBuilder
from autoVeichle import AutoVeichle

class Map:
    def __init__(self, renderEngine, road_map, cell_width):
        self.renderEngine = renderEngine
        self.veichles = []
        self.map = road_map
        self.cell_width = cell_width
        self.side_walk = int(self.cell_width / 7)
        self.road_way = (self.cell_width - self.side_walk * 2) / 2
        self.car_width = int(self.cell_width / 3)
        self.car_height = int(self.cell_width / 5)
        self.border_right = self.side_walk + self.road_way + self.road_way / 2
        self.border_left = self.side_walk + self.road_way / 2
        self.bots = []

    def createRoads(self, road_map):
        for y in range(len(road_map)):
            for x in range(len(road_map[y])):
                road_type = road_map[y][x]
                road = roadBuilder(road_type, x, y, self.cell_width, self.side_walk, rotation = road_type)
                self.map[y][x] = road

    def addVeichle(self, path, facing, autoPilot):
        if facing == 1:
            x = path[0][0] * self.cell_width + self.border_right
            y = path[0][1] * self.cell_width + self.cell_width - self.car_height
            angle = 90
        if facing == 2:
            x = path[0][0] * self.cell_width
            y = path[0][1] * self.cell_width + self.border_left
            angle = 0
        if facing == 3:
            x = path[0][0] * self.cell_width + self.border_left
            y = path[0][1] * self.cell_width
            angle = 270
        if facing == 4:
            x = path[0][0] * self.cell_width + self.cell_width - self.car_width
            y = path[0][1] * self.cell_width + self.border_right
            angle = 180
        
        veichle = Car(self.car_width, self.car_height, x, y, angle)
        self.veichles.append(veichle)
        if autoPilot:
            self.bots.append(AutoVeichle(veichle, path, self.cell_width, self.border_right, self.border_left))
        return veichle

    def update(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                road = self.map[y][x]
                if road:
                    road.draw(self.renderEngine)
        for bot in self.bots:
            bot.update()
        for veichle in self.veichles:
            veichle.move()
            veichle.update()
            veichle.draw(self.renderEngine)
