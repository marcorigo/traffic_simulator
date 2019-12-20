class AutoVeichle:
    def __init__(self, veichle, path, cell_width, road_way, side_walk):
        self.veichle = veichle
        self.path = path
        self.pathLength = len(self.path) 
        self.cell_width = cell_width
        self.pathStatus = 0
        self.slowing = False
        self.movingToAngle = self.veichle.angle
        self.curve = False
        self.border_right = side_walk + road_way + road_way / 2
        self.border_left = side_walk + road_way / 2

    def update(self):
        self.checkPath()
        self.veichle.controls['up'] = True
        self.veichle.controls['right'] = False
        self.veichle.controls['left'] = False

        self.checkMove()
        self.move()
        
    def checkMove(self):
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
                    if int(self.veichle.position.y) >= int(((self.cell_width * (self.path[actualPos][1])) + self.border_right )):
                        self.veichle.angle = 0
                #top to left
                if self.path[actualPos][0] > self.path[nextPos][0]:
                    if int(self.veichle.position.y) >= int((self.cell_width * (self.path[actualPos][1]) + self.border_left )):
                        self.veichle.angle = 180
            # # Right
            if self.path[beforePos][0] > self.path[actualPos][0]:
                # Right to top
                if self.path[actualPos][1] < self.path[nextPos][1]:
                    if int(self.veichle.position.x) <= int((self.cell_width * (self.path[actualPos][0]) + self.border_left )):
                        self.veichle.angle = 270
                # Right to bottom
                if self.path[actualPos][1] > self.path[nextPos][1]:
                    if int(self.veichle.position.x) <= int((self.cell_width * (self.path[actualPos][0]) + self.border_right )):
                        self.veichle.angle = 90
            # Bottom
            if self.path[beforePos][1] > self.path[actualPos][1]:
                # Bottom to right
                if self.path[actualPos][0] < self.path[nextPos][0]:
                    if int(self.veichle.position.y) <= int(((self.cell_width * (self.path[actualPos][1])) + self.border_right )):
                        self.veichle.angle = 0
                # Bottom to left
                if self.path[actualPos][0] > self.path[nextPos][0]:
                    if int(self.veichle.position.y) <= int(((self.cell_width * (self.path[actualPos][1])) + self.border_left )):
                        self.veichle.angle = 180
            # Left   
            if self.path[beforePos][0] < self.path[actualPos][0]:
                # Left to top
                if self.path[actualPos][1] > self.path[nextPos][1]:
                    if int(self.veichle.position.x) >= int(((self.cell_width * (self.path[actualPos][0])) + self.border_right )):
                        self.veichle.angle = 90
                # Left to bottom
                if self.path[actualPos][1] < self.path[nextPos][1]:
                    if int(self.veichle.position.x) >= int(((self.cell_width * (self.path[actualPos][0])) + self.border_left )):
                        self.veichle.angle = 270


    def move(self):
        pass
        #Error precision handling
        # if int(self.veichle.angle + 1) == self.movingToAngle or int(self.veichle.angle - 1) == self.movingToAngle:
        #     self.veichle.angle = self.movingToAngle

        # if int(self.veichle.angle) != self.movingToAngle:

        #     if self.curve == 'right':
        #         self.veichle.controls['right'] = True
        #     else:
        #         self.veichle.controls['left'] = True
        
        # else:
        #     self.curve = False

    def checkPath(self):
        if self.pathStatus < self.pathLength - 1:
            x = int(self.veichle.position.x / self.cell_width)
            y = int(self.veichle.position.y / self.cell_width)
            if self.path[self.pathStatus + 1][0] == x and self.path[self.pathStatus + 1][1] == y:
                self.pathStatus += 1
        else:
            self.pathStatus = self.pathLength - 1
            # print('Il veicolo si trova nelle celle x = {}  y = {}'.format(x, y))

            