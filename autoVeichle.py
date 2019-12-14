class AutoVeichle:
    def __init__(self, veichle, path, cell_width):
        self.veichle = veichle
        self.path = path
        self.cell_width = cell_width
        self.pathStatus = 0
        self.slowing = False

    def update(self):
        self.checkPath()
        self.veichle.controls['up'] = True
        self.veichle.controls['right'] = False
        self.veichle.controls['left'] = False
        if self.pathStatus < len(self.path):
            #if next path y is the same as now
            if self.path[self.pathStatus + 1][1] == self.path[self.pathStatus][1]:
                #if next x is min
                if self.path[self.pathStatus + 1][0] < self.path[self.pathStatus][0]:
                    if int(self.veichle.angle) != 180:
                        if self.path[self.pathStatus - 1][1] > self.path[self.pathStatus][1]:
                            self.veichle.controls['left'] = True
                        else:
                            self.veichle.controls['right'] = True
                elif self.path[self.pathStatus + 1][0] > self.path[self.pathStatus][0]:
                    if int(self.veichle.angle) != 0:
                        if self.path[self.pathStatus - 1][1] > self.path[self.pathStatus][1]:
                            self.veichle.controls['right'] = True
                        else:
                            self.veichle.controls['left'] = True

            if self.path[self.pathStatus + 1][0] < self.path[self.pathStatus][0]:
                if int(self.veichle.angle) != 180:
                    if self.path[self.pathStatus - 1][1] > self.path[self.pathStatus][1]:
                        self.veichle.controls['left'] = True
                    else:
                        self.veichle.controls['right'] = True
            elif self.path[self.pathStatus + 1][0] > self.path[self.pathStatus][0]:
                if int(self.veichle.angle) != 0:
                    if self.path[self.pathStatus - 1][1] > self.path[self.pathStatus][1]:
                        self.veichle.controls['right'] = True
                    else:
                        self.veichle.controls['left'] = True

    def checkPath(self):
        x = int(self.veichle.position.x / self.cell_width)
        y = int(self.veichle.position.y / self.cell_width)
        if self.path[self.pathStatus + 1][0] == x and self.path[self.pathStatus + 1][1] == y:
            self.pathStatus += 1
        # print('Il veicolo si trova nelle celle x = {}  y = {}'.format(x, y))

            