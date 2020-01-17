import random
import time
from config import config
import sys
sys.path.insert(0, './veichles')
from car import Car
from truck import Truck
from roads import roadBuilder
from bot import Bot

class Map:
    def __init__(self, renderEngine, road_map, cell_width, debug):
        self.renderEngine = renderEngine
        self.map = road_map
        self.cell_width = cell_width
        self.debug = debug
        self.map_width = len(self.map[0])
        self.map_height = len(self.map)
        self.number_veichles_spawned = 0
        self.accidents = 0
        self.side_walk = config['SIDE_WALK_SIZE'] or int(self.cell_width / 10)
        self.road_way = int((self.cell_width - self.side_walk * 2) / 2)
        self.car_width = config['CAR_WIDTH'] or int(self.cell_width / 3)
        self.car_height = config['CAR_HEIGHT'] or int(self.cell_width / 5)
        self.truck_width = config['TRUCK_WIDTH'] or int(self.cell_width / 1.7)
        self.truck_height = config['TRUCK_HEIGHT'] or int(self.cell_width / 3)
        self.border_right = self.side_walk + self.road_way + self.road_way / 2
        self.border_left = self.side_walk + self.road_way / 2
        self.explosion_persitance = config['EXPLOSION_PERSISTANCE']
        self.max_veichles_on_map = config['MAX_VEICHLE_NUMBER']
        self.veichle_spawn_time = config['VEICHLES_SPAWN_INTERVAL']
        self.bots = []
        self.spawners = []
        self.explosions = []

        self.createRoads()

    def createRoads(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                road_type = self.map[y][x]

                # Check if is and create
                self.createVeichleSpawnPoint(road_type, x, y)

                road = roadBuilder(road_type, x, y, self.cell_width, self.side_walk, rotation = road_type)
                self.map[y][x] = road

    def getRoadSpawnPoints(self, facing, x, y):
        if facing == 1:
            x = x * self.cell_width + self.cell_width / 2 + self.road_way / 2
            y = y * self.cell_width + self.cell_width - self.car_height
        if facing == 2:
            x = x * self.cell_width
            y = y * self.cell_width + self.cell_width / 2 + self.road_way / 2
        if facing == 3:
            x = x * self.cell_width + self.side_walk + self.road_way / 2
            y = y * self.cell_width
        if facing == 4:
            x = x * self.cell_width + self.cell_width / 2 + self.road_way / 2
            y = y * self.cell_width + self.border_left
        return x, y

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

        x, y = self.getRoadSpawnPoints(facing, x, y)
        # veichle = Car(len(self.bots), self.car_width, self.car_height, x, y)

        num = random.randint(0, 5)
        if num <= 2:
            veichle = Car(self.number_veichles_spawned, 'car', self.car_width, self.car_height, x, y)
        if num >= 3:
            veichle = Car(self.number_veichles_spawned, 'taxi', self.car_width, self.car_height, x, y)
        # if num == 3:
        #     veichle = Truck(self.number_veichles_spawned, self.truck_width, self.truck_height, x, y)
        # Set car degree
        veichle.changeDegree(facing)

        self.bots.append( Bot(veichle, path, self.cell_width, self.road_way, self.border_right, self.border_left, self.bots, self.map, self.renderEngine, self.debug, active ))
        self.number_veichles_spawned += 1
        return veichle

    def createVeichleSpawnPoint(self, road_type, x, y):
        if road_type == '➡' or road_type == '⬅' or road_type == '⬆' or road_type == '⬇':
            spawner = {
                'x': x,
                'y': y,
                'spawned': 0,
                'last_spawned_time': 0
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
            return spawner
        return False

    def createExplosion(self, x, y):
        explosion = {
            'created_time': int(time.time()),
            'width': int(self.cell_width),
            'height': int(self.cell_width),
            'x': x - int(self.cell_width / 2),
            'y': y - int(self.cell_width / 2),
        }

        self.explosions.append(explosion)
    
    def explosionManager(self):
        for explosion in self.explosions:
            if explosion['created_time'] + self.explosion_persitance > int(time.time()):
                self.renderEngine.drawExplosion(explosion)
            else:
                self.explosions.remove(explosion)

    def checkCollision(self):
        for i in range(len(self.bots)):
            for j in range(len(self.bots)):
                bot1 = self.bots[i]
                bot2 = self.bots[j]
                if bot1.veichle.id != bot2.veichle.id:
                    if( bot1.veichle.position.x - bot1.veichle.getWidth() / 2 <= bot2.veichle.position.x + bot2.veichle.getWidth() / 2 and
                        bot1.veichle.position.x + bot1.veichle.getWidth() / 2 >= bot2.veichle.position.x - bot2.veichle.getWidth() / 2 and
                        bot1.veichle.position.y - bot1.veichle.getHeight() / 2 <= bot2.veichle.position.y + bot2.veichle.getHeight() / 2 and
                        bot1.veichle.position.y + bot1.veichle.getHeight() / 2 >= bot2.veichle.position.y - bot2.veichle.getHeight() / 2):
                        self.bots.remove(bot1)
                        self.bots.remove(bot2)
                        self.accidents += 1
                        
                        explosion_x = (bot1.veichle.position.x+bot2.veichle.position.x)/2
                        explosion_y = (bot1.veichle.position.y+bot2.veichle.position.y)/2
                        self.createExplosion(explosion_x, explosion_y)

                        # print('-----------')
                        # print(bot1.veichle.position.x - bot1.veichle.getWidth() / 2,bot1.veichle.position.x + bot1.veichle.getWidth() / 2, bot1.veichle.position.y - bot1.veichle.getHeight() / 2, bot1.veichle.position.y + bot1.veichle.getHeight() / 2)
                        # print(bot2.veichle.position.x - bot2.veichle.getWidth() / 2,bot2.veichle.position.x + bot2.veichle.getWidth() / 2, bot2.veichle.position.y - bot2.veichle.getHeight() / 2, bot2.veichle.position.y + bot2.veichle.getHeight() / 2)
                        # print('-----------')

                        return True

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
        self.checkCollision()

        self.explosionManager()

        self.renderEngine.drawText('Veicoli spawnati: ' + str(self.number_veichles_spawned), (0, 0, 0), 20, 60)
        self.renderEngine.drawText('Veicoli attivi: ' + str(len(self.bots)), (0, 0, 0), 20, 80)
        self.renderEngine.drawText('Incidenti: ' + str(self.accidents), (0, 0, 0), 20, 100)

    def outsideEdges(self, veichle):
        if (veichle.position.x < - 100 or veichle.position.x > self.map_width * self.cell_width + 100 or
            veichle.position.y < - 100 or veichle.position.y > self.map_height * self.cell_width + 100):
            return True

    def deleteBotsOutOfEdges(self):# Testing deleting ents
        for bot in self.bots:
            if self.outsideEdges(bot.veichle):
                # Todo -Eliminare quelli con path statica
                self.bots.remove(bot)
                return
    
    def checkForSpawn(self):
        for spawner in self.spawners:
            occupied = False
            for bot in self.bots:
                if (bot.veichle.facing == spawner['facing']
                    and bot.path[bot.pathStatus][0] == spawner['x']
                    and bot.path[bot.pathStatus][1] == spawner['y']):

                    occupied = True
            if not occupied and len(self.bots) < self.max_veichles_on_map and spawner['last_spawned_time'] + self.veichle_spawn_time < int(time.time()):
                path = [[spawner['x'], spawner['y']]]

                if spawner['facing'] == 1:
                    path.append([spawner['x'], spawner['y'] - 1])
                if spawner['facing'] == 2:
                    path.append([spawner['x'] + 1, spawner['y']])
                if spawner['facing'] == 3:
                    path.append([spawner['x'], spawner['y'] + 1])
                if spawner['facing'] == 4:
                    path.append([spawner['x'] - 1, spawner['y']])

                self.addVeichle(path = path, facing = spawner['facing'])
                spawner['spawned'] += 1
                spawner['last_spawned_time'] = int(time.time())