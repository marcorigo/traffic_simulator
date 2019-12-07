from car import Car
from roads import roadBuilder

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
                road = roadBuilder(road_type, x, y, self.cell_width, rotation = road_map[x][y])
                self.map[x][y] = road
                road.draw(self.renderEngine)

    def addVeichle(self):
        veichle = Car( cell_width = self.cell_width)
        veichle.model = self.renderEngine.drawRect(veichle.x, veichle.y, veichle.x + veichle.width, veichle.y + veichle.heigth, 'red')
        self.veichles.append(veichle)

    def update(self):
        for veichle in self.veichles:
            veichle.accelerate()
            self.renderEngine.move(veichle.model, veichle.speed, 0)