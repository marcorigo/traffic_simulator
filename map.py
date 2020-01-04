import sys
sys.path.insert(0, './veichles')
from car import Car
from roads import roadBuilder
from bot import Bot

class Map:
    def __init__(self, renderEngine, road_map, cell_width):
        self.renderEngine = renderEngine
        self.map = road_map
        self.cell_width = cell_width
        self.map_width = len(self.map[0])
        self.map_height = len(self.map)
        self.side_walk = int(self.cell_width / 7)
        self.road_way = (self.cell_width - self.side_walk * 2) / 2
        self.car_width = int(self.cell_width / 3)
        self.car_height = int(self.cell_width / 5)
        self.border_right = self.side_walk + self.road_way + self.road_way / 2
        self.border_left = self.side_walk + self.road_way / 2
        self.bots = []
        self.spawners = []

    def createRoads(self, road_map):
        for y in range(len(road_map)):
            for x in range(len(road_map[y])):
                road_type = road_map[y][x]

                # Check if is and create
                self.createVeichleSpawnPoint(road_type, x, y)

                road = roadBuilder(road_type, x, y, self.cell_width, self.side_walk, rotation = road_type)
                self.map[y][x] = road

    def addVeichle(self, path, facing = False, active = True):
        # Find degree
        if not facing:
            if path[0][0] < path[1][0]:
                facing = 2
            if path[0][0] > path[1][0]:
                facing = 4
            if path[0][1] < path[1][1]:
                facing = 3
            if path[0][1] > path[1][1]:
                facing = 1

        # Calc initial car position
        x = path[0][0]
        y = path[0][1]

        if facing == 1:
            x = x * self.cell_width + self.border_right
            y = y * self.cell_width + self.cell_width - self.car_height
        if facing == 2:
            x = x * self.cell_width
            y = y * self.cell_width + self.cell_width - self.car_width 
        if facing == 3:
            x = x * self.cell_width + self.border_left
            y = y * self.cell_width
        if facing == 4:
            x = x * self.cell_width + self.cell_width - self.car_width
            y = y * self.cell_width + self.border_right
        
        veichle = Car(len(self.bots), self.car_width, self.car_height, x, y)
        # Set car degree
        veichle.changeDegree(facing)

        veichle.acceleration = 10
        self.bots.append( Bot(veichle, path, self.cell_width, self.border_right, self.border_left, self.bots, self.map, self.renderEngine, active ))

        return veichle

    def createVeichleSpawnPoint(self, road_type, x, y):
        if road_type == '➡' or road_type == '⬅' or road_type == '⬆' or road_type == '⬇':
            spawner = {
                'x': x,
                'y': y,
                'spawned': 0
                }
            if road_type == '➡':
                spawner['facing'] = 2

            if road_type == '⬅':
                spawner['facing'] = 4

            if road_type == '⬆':
                spawner['facing'] = 1

            if road_type == '⬇':
                spawner['facing'] = 3

            self.spawners.append(spawner)

    def checkCollision(self):
        vW = self.car_height
        vH = self.car_height
        for i in range(len(self.bots)):
            for j in range(len(self.bots)):

                if( self.bots[i].veichle.position.x - vW/2 < self.bots[j].veichle.position.x + vW/2 and
                    self.bots[i].veichle.position.x + vW/2 > self.bots[j].veichle.position.x - vW/2 and
                    self.bots[i].veichle.position.y - vH/2 < self.bots[j].veichle.position.y + vH/2 and
                    self.bots[i].veichle.position.y + vH/2 > self.bots[j].veichle.position.y - vH/2):
                    del self.bots[i]
                    del self.bots[j]
                    return

    def update(self):
        #Drawing roads
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                road = self.map[y][x]
                if road:
                    road.draw(self.renderEngine)

        #Update bots
        for bot in self.bots:

            if bot.active:
                bot.update()
                bot.veichle.move()
                bot.veichle.update()
            bot.veichle.draw(self.renderEngine)

        # Testing deleting ents
        self.deleteBotsOutOfEdges()

        # Spawning cars
        self.checkForSpawn()

        # Delete car collided
        # self.checkCollision()

    def outsideEdges(self, veichle):
        if (veichle.position.x < - 100 or veichle.position.x > self.map_width * self.cell_width + 100 or
            veichle.position.y < - 100 or veichle.position.y > self.map_height * self.cell_width + 100):
            return True

    def deleteBotsOutOfEdges(self):# Testing deleting ents
        for i in range(len(self.bots) - 1):
            if self.outsideEdges(self.bots[i].veichle):

                # Todo -Eliminare quelli con path statica
                del self.bots[i]
                return
    
    def checkForSpawn(self):
        for spawner in self.spawners:
            occupied = False
            for bot in self.bots:
                if (bot.veichle.facing == spawner['facing']
                    and bot.path[bot.pathStatus][0] == spawner['x']
                    and bot.path[bot.pathStatus][1] == spawner['y']):

                    occupied = True
            if not occupied:
                path = [[spawner['x'], spawner['y']]]
                self.addVeichle(path = path, facing = spawner['facing'])
                spawner['spawned'] += 1