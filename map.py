import sys
sys.path.insert(0, './veichles')
from car import Car
from roads import roadBuilder
from bot import Bot

class Map:
    def __init__(self, renderEngine, road_map, cell_width):
        self.renderEngine = renderEngine
        self.veichles = []
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
        x = path[0][0]
        y = path[0][1]

        if facing == 1:
            x = x * self.cell_width + self.border_right
            y = y * self.cell_width + self.cell_width - self.car_height
        if facing == 2:
            x = x * self.cell_width
            y = y * self.cell_width + self.border_left
        if facing == 3:
            x = x * self.cell_width + self.border_left
            y = y * self.cell_width
        if facing == 4:
            x = x * self.cell_width + self.cell_width - self.car_width
            y = y * self.cell_width + self.border_right
        
        veichle = Car(len(self.veichles), self.car_width, self.car_height, x, y)
        # Set car degree
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
        for i in range(len(self.veichles)):
            for j in range(len(self.veichles)):
                # Test
                self.renderEngine.drawRect( x = self.veichles[i].position.x - vW/2, y = self.veichles[i].position.y - vH/2, width = vW, height = vH, color = (19, 20, 48))

                if( self.veichles[i].position.x - vW/2 < self.veichles[j].position.x + vW/2 and
                    self.veichles[i].position.x + vW/2 > self.veichles[j].position.x - vW/2 and
                    self.veichles[i].position.y - vH/2 < self.veichles[j].position.y + vH/2 and
                    self.veichles[i].position.y + vH/2 > self.veichles[j].position.y - vH/2):
                    # del self.veichles[i]    
                    # del self.veichles[j]          
                    print('collisione')
                    # return
                
    def outsideEges(self, veichle):
        if (veichle.position.x < - 100 or veichle.position.x > self.map_width * self.cell_width + 100 or
            veichle.position.y < - 100 or veichle.position.y > self.map_height * self.cell_width + 100):
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
            bot.update()
            # Test
            # self.renderEngine.drawRect( x = bot.veichle.position.x - 50, y = bot.veichle.position.y - 50, width = 100, height = 100, color = (216, 17, 17))
     
        #Update cars
        for veichle in self.veichles:
            veichle.move()
            veichle.update()
            veichle.draw(self.renderEngine)
            #Testing
            # self.checkCollision()

        #Testing deleting ents
        for i in range(len(self.veichles)):
            if self.outsideEges(self.veichles[i]):
                for index in range(len(self.bots)):
                    if self.veichles[i].id == self.bots[index].veichle.id:
                        del self.bots[index]
               
