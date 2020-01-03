from render import RenderEngine
import random

class Bot:
    def __init__(self, veichle, path, cell_width, border_right, border_left, bots, map):
        self.veichle = veichle
        self.path = path
        self.pathLength = len(self.path) 
        self.cell_width = cell_width
        self.pathStatus = 0
        self.slowing = False
        self.movingToAngle = self.veichle.angle
        self.border_right = border_right
        self.border_left = border_left
        self.vision_field = 100
        self.map_bots = bots
        self.map = map

        # if the path has not been given
        self.auto_generate = len(self.path) <= 1
        # For initial after spawn
        self.generate_path = True

    def update(self):
        # If path need to be auto-generated
        if self.auto_generate and self.generate_path:
            self.generatePath()
        
        self.pathLength = len(self.path) 
        self.checkPath()
        self.checkMove()
        self.dashcam()
        self.move()
        
    def generatePath(self):
        x = self.path[self.pathStatus][0]
        y = self.path[self.pathStatus][1]

        # When a veichle exit the map no path update
        try:
            road = self.map[y][x]
        except:
            return

        actions = [
            [x, y - 1],
            [x + 1, y],
            [x, y + 1],
            [x - 1, y]
        ]

        if self.veichle.facing == 1:
            if road.road_type == '╔':
                self.path.append(actions[1])
            if road.road_type == '╗':
                self.path.append(actions[3])
            if road.road_type == '║' or road.road_type == '⬆':
                self.path.append(actions[0])
            if road.road_type == '╬':
                choice = random.choice([0, 1, 3])
                self.path.append(actions[choice])
        
        if self.veichle.facing == 2:
            if road.road_type == '╝':
                self.path.append(actions[0])
            if road.road_type == '╗':
                self.path.append(actions[2])
            if road.road_type == '═' or road.road_type == '➡':
                self.path.append(actions[1])
            if road.road_type == '╬':
                choice = random.choice([0, 1, 2])
                self.path.append(actions[choice])

        if self.veichle.facing == 3:
            if road.road_type == '╝':
                self.path.append(actions[3])
            if road.road_type == '╚':
                self.path.append(actions[1])
            if road.road_type == '║' or road.road_type == '⬇': 
                self.path.append(actions[2])
            if road.road_type == '╬':
                choice = random.choice([1, 2, 3])
                self.path.append(actions[choice])

        if self.veichle.facing == 4:
            if road.road_type == '╔':
                self.path.append(actions[2])
            if road.road_type == '╚':
                self.path.append(actions[0])
            if road.road_type == '═' or road.road_type == '⬅':
                self.path.append(actions[3])
            if road.road_type == '╬':
                choice = random.choice([0, 2, 3])
                self.path.append(actions[choice])

        self.generate_path = False

    def checkMove(self):
        # This function follow the path, both given or auto-generated
        beforePos = self.pathStatus - 1
        actualPos = self.pathStatus
        nextPos = 0
        if actualPos + 1 < self.pathLength:
            nextPos = self.pathStatus + 1
        else:
            nextPos = actualPos
            
        # Top
        if actualPos > 0:
            if self.path[beforePos][1] < self.path[actualPos][1]:
                self.slowing = True
                # Top to right
                if self.path[actualPos][0] < self.path[nextPos][0]:
                    if int(self.veichle.position.y) >= int(((self.cell_width * (self.path[actualPos][1])) + self.border_right )):
                        self.veichle.changeDegree(2)
                #top to left
                if self.path[actualPos][0] > self.path[nextPos][0]:
                    if int(self.veichle.position.y) >= int((self.cell_width * (self.path[actualPos][1]) + self.border_left )):
                        self.veichle.changeDegree(4)
            # # Right
            if self.path[beforePos][0] > self.path[actualPos][0]:
                self.slowing = True
                # Right to top
                if self.path[actualPos][1] < self.path[nextPos][1]:
                    if int(self.veichle.position.x) <= int((self.cell_width * (self.path[actualPos][0]) + self.border_left )):
                        self.veichle.changeDegree(3)
                # Right to bottom
                if self.path[actualPos][1] > self.path[nextPos][1]:
                    if int(self.veichle.position.x) <= int((self.cell_width * (self.path[actualPos][0]) + self.border_right )):
                        self.veichle.changeDegree(1)
            # Bottom
            if self.path[beforePos][1] > self.path[actualPos][1]:
                self.slowing = True
                # Bottom to right
                if self.path[actualPos][0] < self.path[nextPos][0]:
                    if int(self.veichle.position.y) <= int(((self.cell_width * (self.path[actualPos][1])) + self.border_right )):
                        self.veichle.changeDegree(2)
                # Bottom to left
                if self.path[actualPos][0] > self.path[nextPos][0]:
                    if int(self.veichle.position.y) <= int(((self.cell_width * (self.path[actualPos][1])) + self.border_left )):
                        self.veichle.changeDegree(4)
            # Left   
            if self.path[beforePos][0] < self.path[actualPos][0]:
                self.slowing = True
                # Left to top
                if self.path[actualPos][1] > self.path[nextPos][1]:
                    if int(self.veichle.position.x) >= int(((self.cell_width * (self.path[actualPos][0])) + self.border_right )):
                        self.veichle.changeDegree(1)
                # Left to bottom
                if self.path[actualPos][1] < self.path[nextPos][1]:
                    if int(self.veichle.position.x) >= int(((self.cell_width * (self.path[actualPos][0])) + self.border_left )):
                        self.veichle.changeDegree(3)


    def move(self):
        # Slowing down for curves
        if self.slowing and self.veichle.acceleration > 10:
            self.veichle.controls['space'] = True
            self.veichle.controls['up'] = False
        else:
            self.veichle.controls['space'] = False
            self.veichle.controls['up'] = True

    def dashcam(self):
        vW = self.vision_field
        vH = self.vision_field
        for bot in self.map_bots:
            if bot.veichle.id != self.veichle.id:
                if( self.veichle.position.x - vW/2 < bot.veichle.position.x + vW/2 and
                    self.veichle.position.x + vW/2 > bot.veichle.position.x - vW/2 and
                    self.veichle.position.y - vH/2 < bot.veichle.position.y + vH/2 and
                    self.veichle.position.y + vH/2 > bot.veichle.position.y - vH/2):
                    
                    if self.veichle.facing == bot.veichle.facing:
                        print('collisione')
                        self.veichle.controls['space']

    def checkPath(self):
        # Auto increment pathStatus in relation to x and y and previous path coords
        if self.pathStatus < self.pathLength - 1:
            x = int(self.veichle.position.x / self.cell_width)
            y = int(self.veichle.position.y / self.cell_width)
            if self.path[self.pathStatus + 1][0] == x and self.path[self.pathStatus + 1][1] == y:
                self.pathStatus += 1
                self.generate_path = True
        else:
            self.pathStatus = self.pathLength - 1
            # print('Il veicolo si trova nelle celle x = {}  y = {}'.format(x, y))

            