class AutoVeichle:
    def __init__(self, veichle, path, cell_width):
        self.veichle = veichle
        self.path = path
        self.pathLength = len(self.path) 
        self.cell_width = cell_width
        self.pathStatus = 0
        self.slowing = False
        self.movingToAngle = self.veichle.angle
        self.curve = False

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
        next2Pos = 0
        if actualPos + 1 < self.pathLength:
            nextPos = self.pathStatus + 1
        if actualPos + 2 < self.pathLength:
            next2Pos = self.pathStatus + 2

        if next2Pos == actualPos + 2:

            if self.path[nextPos][1] < self.path[actualPos][1]:
                #Bottom to right
                if self.path[actualPos][1] > self.path[nextPos][1] and self.path[next2Pos][0] > self.path[nextPos][0]:
                    if self.veichle.position.y < ((self.cell_width * self.path[actualPos][1]) + self.cell_width / 4):
                        self.movingToAngle = 0
                        self.curve = 'right'

            if self.path[actualPos][1] < self.path[beforePos][1]:
                #Bottom to left
                if self.path[beforePos][1] > self.path[actualPos][1] and self.path[nextPos][0] < self.path[actualPos][0]:
                    if int(self.veichle.position.y) < ((self.cell_width * self.path[beforePos][1]) - self.cell_width / 6):
                        self.movingToAngle = 180
                        self.curve = 'left'
            else:
                #top to rigth
                if self.path[actualPos][1] < self.path[nextPos][1] and self.path[next2Pos][0] < self.path[nextPos][0]:
                    if self.veichle.position.y > ((self.cell_width * self.path[nextPos][1]) - self.cell_width / 2.5):
                        self.movingToAngle = 180
                        self.curve = 'right'
                
                #Bottom to left
                if self.path[beforePos][1] < self.path[actualPos][1] and self.path[nextPos][0] > self.path[actualPos][0]:
                    if int(self.veichle.position.y) > ((self.cell_width * self.path[beforePos][1]) - self.cell_width / 4):
                        self.movingToAngle = 360
                        self.curve = 'left'


    def move(self):
        #Error precision handling
        if int(self.veichle.angle + 1) == self.movingToAngle or int(self.veichle.angle - 1) == self.movingToAngle:
            self.veichle.angle = self.movingToAngle

        if int(self.veichle.angle) != self.movingToAngle:

            if self.curve == 'right':
                self.veichle.controls['right'] = True
            else:
                self.veichle.controls['left'] = True
        
        else:
            self.curve = False

    def checkPath(self):
        if self.pathStatus < self.pathLength - 1:
            x = int(self.veichle.position.x / self.cell_width)
            y = int(self.veichle.position.y / self.cell_width)
            if self.path[self.pathStatus + 1][0] == x and self.path[self.pathStatus + 1][1] == y:
                self.pathStatus += 1
            # print('Il veicolo si trova nelle celle x = {}  y = {}'.format(x, y))

            