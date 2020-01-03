from render import RenderEngine
import random

class Bot:
    def __init__(self, veichle, path, cell_width, border_right, border_left, bots, map, renderEngine, active = True):
        self.veichle = veichle
        self.path = path
        self.pathLength = len(self.path) 
        self.cell_width = cell_width
        self.pathStatus = 0
        self.slowing = False
        self.movingToAngle = self.veichle.angle
        self.border_right = border_right
        self.border_left = border_left
        self.vision_field_width = 100
        self.vision_field_height = self.veichle.height
        self.vision_field_x = 0
        self.vision_field_y = 0
        self.avoidAccident = False
        self.speed_to_slow_down = 10
        self.map_bots = bots
        self.map = map
        self.renderEngine = renderEngine
        self.debug_mode = True
        self.active = active

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
        self.setViewPoints()
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
        
        slowing = False

        # Top
        if actualPos > 0:
            if self.path[beforePos][1] < self.path[actualPos][1]:
                slowing = True
                # Top to right
                if self.path[actualPos][0] < self.path[nextPos][0]:
                    if int(self.veichle.position.y) >= int(((self.cell_width * (self.path[actualPos][1])) + self.border_right )):
                        self.veichle.changeDegree(2)
                #top to left
                if self.path[actualPos][0] > self.path[nextPos][0]:
                    if int(self.veichle.position.y) >= int((self.cell_width * (self.path[actualPos][1]) + self.border_left )):
                        self.veichle.changeDegree(4)
            # # Right
            elif self.path[beforePos][0] > self.path[actualPos][0]:
                slowing = True
                # Right to top
                if self.path[actualPos][1] < self.path[nextPos][1]:
                    if int(self.veichle.position.x) <= int((self.cell_width * (self.path[actualPos][0]) + self.border_left )):
                        self.veichle.changeDegree(3)
                # Right to bottom
                if self.path[actualPos][1] > self.path[nextPos][1]:
                    if int(self.veichle.position.x) <= int((self.cell_width * (self.path[actualPos][0]) + self.border_right )):
                        self.veichle.changeDegree(1)
            # Bottom
            elif self.path[beforePos][1] > self.path[actualPos][1]:
                slowing = True
                # Bottom to right
                if self.path[actualPos][0] < self.path[nextPos][0]:
                    if int(self.veichle.position.y) <= int(((self.cell_width * (self.path[actualPos][1])) + self.border_right )):
                        self.veichle.changeDegree(2)
                # Bottom to left
                if self.path[actualPos][0] > self.path[nextPos][0]:
                    if int(self.veichle.position.y) <= int(((self.cell_width * (self.path[actualPos][1])) + self.border_left )):
                        self.veichle.changeDegree(4)
            # Left   
            elif self.path[beforePos][0] < self.path[actualPos][0]:
                slowing = True
                # Left to top
                if self.path[actualPos][1] > self.path[nextPos][1]:
                    if int(self.veichle.position.x) >= int(((self.cell_width * (self.path[actualPos][0])) + self.border_right )):
                        self.veichle.changeDegree(1)
                # Left to bottom
                if self.path[actualPos][1] < self.path[nextPos][1]:
                    if int(self.veichle.position.x) >= int(((self.cell_width * (self.path[actualPos][0])) + self.border_left )):
                        self.veichle.changeDegree(3)

            if slowing and self.veichle.acceleration > self.speed_to_slow_down:
                self.slowing = True
            if not slowing or slowing and self.veichle.acceleration < self.speed_to_slow_down:
                self.slowing = False


    def move(self):
        # Slowing down for curves
        if self.slowing:
            self.veichle.controls['up'] = False
        elif self.avoidAccident:
            self.veichle.controls['space'] = True
            self.veichle.controls['up'] = False
        else:
            self.veichle.controls['space'] = False
            self.veichle.controls['up'] = True

    def setViewPoints(self):
        facing = self.veichle.facing
        x = self.veichle.position.x
        y = self.veichle.position.y
        height = self.veichle.height
        width = self.veichle.width
        if facing == 1:
            x = x - height / 2
            y = y - width / 2 - self.vision_field_width
        if facing == 2:
            x = x + width / 2
            y = y - height / 2
        if facing == 3:
            x = x - height / 2
            y = y + width / 2
        if facing == 4:
            x = x - width / 2 - self.vision_field_width
            y = y - height / 2
        
        self.vision_field_x = x
        self.vision_field_y = y

    def dashcam(self):
        vW = self.vision_field_width
        vH = self.vision_field_height
        if self.veichle.facing == 1 or self.veichle.facing == 3:
            vW = self.vision_field_height
            vH = self.vision_field_width

        if self.debug_mode:
            if self.avoidAccident:
                self.renderEngine.drawRect(self.vision_field_x, self.vision_field_y, vW, vH, (226, 0, 0))
            elif self.slowing:
                self.renderEngine.drawRect(self.vision_field_x, self.vision_field_y, vW, vH, (255, 144, 0))
            else:
                self.renderEngine.drawRect(self.vision_field_x, self.vision_field_y, vW, vH, (242, 242, 242))

        for bot in self.map_bots:
            if bot.veichle.id != self.veichle.id:

                if( self.vision_field_x <= bot.veichle.position.x + bot.veichle.height / 2 and
                    self.vision_field_x + vW >= bot.veichle.position.x - bot.veichle.height / 2 and
                    self.vision_field_y <= bot.veichle.position.y + bot.veichle.height / 2 and
                    self.vision_field_y + vH >= bot.veichle.position.y - bot.veichle.height / 2):

                    self.avoidAccident = True
                    return

        self.avoidAccident = False

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