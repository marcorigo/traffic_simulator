from car import Car
from roads import roadBuilder
from bot import Bot

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

    def addVeichle(self, path, facing = 1, autoPilot = True):
        # Find degree
        if autoPilot and path:
            if path[0][0] < path[1][0]:
                facing = 2
            if path[0][0] > path[1][0]:
                facing = 4
            if path[0][1] < path[1][1]:
                facing = 3
            if path[0][1] > path[1][1]:
                facing = 1

        # Calc initial car position
        if facing == 1:
            x = path[0][0] * self.cell_width + self.border_right
            y = path[0][1] * self.cell_width + self.cell_width - self.car_height
        if facing == 2:
            x = path[0][0] * self.cell_width
            y = path[0][1] * self.cell_width + self.border_left
        if facing == 3:
            x = path[0][0] * self.cell_width + self.border_left
            y = path[0][1] * self.cell_width
        if facing == 4:
            x = path[0][0] * self.cell_width + self.cell_width - self.car_width
            y = path[0][1] * self.cell_width + self.border_right
        
        veichle = Car(self.car_width, self.car_height, x, y)
        # Set cat degree
        veichle.changeDegree(facing)
        # Adding to map veichles
        self.veichles.append(veichle)
        # If is bot
        if autoPilot:
            self.bots.append( Bot(veichle, path, self.cell_width, self.border_right, self.border_left, self.bots ))

        return veichle

    def createVeichleSpawnPoint(self):
        pass

    def checkCollision(self):
        vW = self.car_height
        vH = self.car_height
        for i in self.bots:
            for j in self.bots:
                if(i.veichle.position.x - vW/2 > j.veichle.position.x - vW/2 and i.veichle.position.x - vW/2 < j.veichle.position.x - vW/2 + vW and i.veichle.position.y - vH/2 > j.veichle.position.y - vH/2 and i.veichle.position.y - vH/2 < j.veichle.position.y - vH/2 + vH):
                    del self.bots[i]
                    print('collisione')
                
            

    def update(self):
        #Drawing roads
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                road = self.map[y][x]
                if road:
                    road.draw(self.renderEngine)
        self.checkCollision()
        #Update bots
        for bot in self.bots:
            bot.update()
        #Update cars
        for veichle in self.veichles:
            veichle.move()
            veichle.update()
            veichle.draw(self.renderEngine)
