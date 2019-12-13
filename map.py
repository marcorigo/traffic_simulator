from car import Car
from roads import roadBuilder

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

    def createRoads(self, road_map):
        for x in range(len(road_map)):
            for y in range(len(road_map[0])):
                road_type = road_map[x][y]
                road = roadBuilder(road_type, x, y, self.cell_width, self.side_walk, rotation = road_type)
                self.map[x][y] = road

    def addVeichle(self, path, facing):
        if facing == 1:
            x = path[0][0] * self.cell_width + self.side_walk + self.road_way * 2 - self.car_width
            y = path[0][1] * self.cell_width + self.cell_width - self.car_height
            angle = 90
        if facing == 2:
            x = path[0][0] * self.cell_width
            y = path[0][1] * self.cell_width + self.side_walk + self.road_way - self.car_width
            angle = 0
        if facing == 3:
            x = path[0][0] * self.cell_width + self.side_walk + self.road_way - self.car_width
            y = path[0][1] * self.cell_width
            angle = 270
        if facing == 4:
            x = path[0][0] * self.cell_width + self.cell_width - self.car_width
            y = path[0][1] * self.cell_width + self.side_walk + self.road_way * 2 - self.car_width
            angle = 180
        
        veichle = Car(self.car_width, self.car_height, path, x, y, angle)
        self.veichles.append(veichle)
        return veichle

    def update(self):
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                road = self.map[x][y]
                if road:
                    road.draw(self.renderEngine)
        for veichle in self.veichles:
            veichle.controls["up"] = True
            veichle.move()
            veichle.update()
            veichle.draw(self.renderEngine)
