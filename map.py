from car import Car
from roads import StraightRoad

class Map:
    def __init__(self, canvas, road_map):
        self.canvas = canvas
        self.veichles = []
        self.map = road_map

    def createRoads(self, road_map):
        for x in range(len(road_map)):
            for y in range(len(road_map)):
                road = StraightRoad(x, y, 50)
                self.map[x][y] = road
                road.draw(self.canvas)

    def addVeichle(self):
        veichle = Car()
        veichle.model = self.canvas.create_rectangle(veichle.posx, veichle.posy, veichle.posx + veichle.width, veichle.posy + veichle.heigth, fill = 'red')
        self.veichles.append(veichle)

    def update(self):
        for veichle in self.veichles:
            veichle.move()
            self.canvas.move(veichle.model, veichle.speed, 0)