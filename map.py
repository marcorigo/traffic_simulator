from car import Car
from roads import roadBuilder
from roads import Road

class Map:
    def __init__(self, renderEngine, road_map, cell_width):
        self.renderEngine = renderEngine
        self.veichles = []
        self.map = road_map
        self.cell_width = cell_width

    def createRoads(self, road_map):
        for x in range(len(road_map)):
            for y in range(len(road_map[0])):
                road_type = road_map[x][y]
                road = roadBuilder(road_type, x, y, self.cell_width, rotation = road_type)
                self.map[x][y] = road

    def addVeichle(self):
        path = [2,5,8,11]
        veichle = Car( self.cell_width, path, path[0] * self.cell_width + Road.borderProp, 0, angle = 270)
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
            if int(veichle.position.y) == 2*self.cell_width + Road.borderProp * 2:
                veichle.angle = 180
            veichle.move()
            veichle.update()
            veichle.draw(self.renderEngine)
