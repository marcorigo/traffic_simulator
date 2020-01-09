from render import RenderEngine
import random

class Bot:
    def __init__(self, veichle, path, cell_width, border_right, border_left, bots, map, renderEngine, active = True):
        self.veichle = veichle
        self.path = path
        self.pathLength = len(self.path) 
        self.cell_width = cell_width
        self.pathStatus = 0
        self.approaching_curve = False
        self.movingToAngle = self.veichle.angle
        self.border_right = border_right
        self.border_left = border_left
        self.vision_field_width = int(self.cell_width * 1.5)
        self.vision_field_height = self.veichle.height
        self.vision_field_x = 0
        self.vision_field_y = 0
        self.avoidAccident = False
        self.speed_to_slow_down = 10
        self.min_acceleration = 7
        self.map_bots = bots
        self.map = map
        self.renderEngine = renderEngine
        self.debug_mode = False
        self.active = active
        self.stop_for_cross = False

        # if the path has not been given
        self.auto_generate = len(self.path) <= 2
        # For initial after spawn
        self.generate_path = False

    def update(self):
        # If path need to be auto-generated
        if self.auto_generate and self.generate_path:
            self.generatePath()
        self.pathLength = len(self.path) 
        self.checkPath()
        self.checkMove()
        self.updateViewPoints()
        self.dashcam()
        self.move()
        
    def generatePath(self):
        x = self.path[self.pathStatus][0]
        y = self.path[self.pathStatus][1]

        # When a veichle exit the map no path update
        try:
            road = self.map[y][x]
            if road == 0:
                return
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
            if road.road_type == '╠':
                choice = random.choice([0, 1])
                self.path.append(actions[choice])
            if road.road_type == '╦':
                choice = random.choice([3, 1])
                self.path.append(actions[choice])
            if road.road_type == '╣':
                choice = random.choice([0, 3])
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
            if road.road_type == '╠':
                choice = random.choice([0, 2])
                self.path.append(actions[choice])
            if road.road_type == '╦':
                choice = random.choice([3, 2])
                self.path.append(actions[choice])
            if road.road_type == '╩':
                choice = random.choice([0, 3])
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
            if road.road_type == '╠':
                choice = random.choice([1, 2])
                self.path.append(actions[choice])
            if road.road_type == '╣':
                choice = random.choice([2, 3])
                self.path.append(actions[choice])
            if road.road_type == '╩':
                choice = random.choice([1, 3])
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
            if road.road_type == '╠':
                choice = random.choice([0, 2])
                self.path.append(actions[choice])
            if road.road_type == '╦':
                choice = random.choice([2, 3])
                self.path.append(actions[choice])
            if road.road_type == '╩':
                choice = random.choice([0, 3])
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
                # Top to right
                if self.path[actualPos][0] < self.path[nextPos][0]:
                    self.approaching_curve = True
                    if int(self.veichle.position.y) >= int(((self.cell_width * (self.path[actualPos][1])) + self.border_right )):
                        self.veichle.changeDegree(2)
                else:
                    self.approaching_curve = False
                #top to left
                if self.path[actualPos][0] > self.path[nextPos][0]:
                    self.approaching_curve = True
                    if int(self.veichle.position.y) >= int((self.cell_width * (self.path[actualPos][1]) + self.border_left )):
                        self.veichle.changeDegree(4)
                else:
                    self.approaching_curve = False
            # # Right
            elif self.path[beforePos][0] > self.path[actualPos][0]:
                # Right to top
                if self.path[actualPos][1] < self.path[nextPos][1]:
                    self.approaching_curve = True
                    if int(self.veichle.position.x) <= int((self.cell_width * (self.path[actualPos][0]) + self.border_left )):
                        self.veichle.changeDegree(3)
                else:
                    self.approaching_curve = False
                # Right to bottom
                if self.path[actualPos][1] > self.path[nextPos][1]:
                    self.approaching_curve = True
                    if int(self.veichle.position.x) <= int((self.cell_width * (self.path[actualPos][0]) + self.border_right )):
                        self.veichle.changeDegree(1)
                else:
                    self.approaching_curve = False
            # Bottom
            elif self.path[beforePos][1] > self.path[actualPos][1]:
                # Bottom to right
                if self.path[actualPos][0] < self.path[nextPos][0]:
                    self.approaching_curve = True
                    if int(self.veichle.position.y) <= int(((self.cell_width * (self.path[actualPos][1])) + self.border_right )):
                        self.veichle.changeDegree(2)
                else:
                    self.approaching_curve = False
                # Bottom to left
                if self.path[actualPos][0] > self.path[nextPos][0]:
                    self.approaching_curve = True
                    if int(self.veichle.position.y) <= int(((self.cell_width * (self.path[actualPos][1])) + self.border_left )):
                        self.veichle.changeDegree(4)
                else:
                    self.approaching_curve = False
            # Left   
            elif self.path[beforePos][0] < self.path[actualPos][0]:
                # Left to top
                if self.path[actualPos][1] > self.path[nextPos][1]:
                    self.approaching_curve = True
                    if int(self.veichle.position.x) >= int(((self.cell_width * (self.path[actualPos][0])) + self.border_right )):
                        self.veichle.changeDegree(1)
                else:
                    self.approaching_curve = False
                # Left to bottom
                if self.path[actualPos][1] < self.path[nextPos][1]:
                    self.approaching_curve = True
                    if int(self.veichle.position.x) >= int(((self.cell_width * (self.path[actualPos][0])) + self.border_left )):
                        self.veichle.changeDegree(3)
                else:
                    self.approaching_curve = False



    def move(self):
        # Check for cross roads
        try:
            next = self.path[self.pathStatus + 1]
            if not self.map[next[1]][next[0]].can(self.veichle):
                self.stop_for_cross = True
            else:
                self.stop_for_cross = False
        except:
            self.stop_for_cross = False

        if self.avoidAccident or self.stop_for_cross:
            self.veichle.controls['space'] = True
            self.veichle.controls['up'] = False
        # Slowing down for curves or max velocity
        elif self.approaching_curve and self.veichle.acceleration >= self.min_acceleration or self.veichle.acceleration >= self.speed_to_slow_down:
            # self.slowing = True
            self.veichle.controls['up'] = False
        else:
            # self.slowing = False
            self.veichle.controls['space'] = False
            self.veichle.controls['up'] = True

    def updateViewPoints(self):
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
            # elif self.stop_for_cross:
            #     self.renderEngine.drawRect(self.vision_field_x, self.vision_field_y, vW, vH, (255, 229, 0))
            elif self.approaching_curve:
                self.renderEngine.drawRect(self.vision_field_x, self.vision_field_y, vW, vH, (255, 144, 0))
            else:
                self.renderEngine.drawRect(self.vision_field_x, self.vision_field_y, vW, vH, (242, 242, 242))

        for bot in self.map_bots:
            if bot.veichle.id != self.veichle.id:
                check_bot_width = bot.veichle.getWidth()
                check_bot_height = bot.veichle.getHeight()          

                if( self.vision_field_x <= bot.veichle.position.x + check_bot_width / 2 and
                    self.vision_field_x + vW >= bot.veichle.position.x - check_bot_width / 2 and
                    self.vision_field_y <= bot.veichle.position.y + check_bot_height / 2 and
                    self.vision_field_y + vH >= bot.veichle.position.y - check_bot_height / 2):

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