from veichle import Veichle

class Truck(Veichle):
    def __init__(self,id, width, height, posx, posy, angle = 0):
        super().__init__(id, posx, posy, angle)
        self.width = width
        self.height = height

    # Get height and width on orizontal axis for easy collision detection
    def getWidth(self):
        if self.facing == 1 or self.facing == 2:
            return int(self.height)
        return int(self.height)

    def getHeight(self):
        if self.facing == 1 or self.facing == 2:
            return int(self.width)
        return int(self.height)

    def draw(self, renderEngine):
        x = self.position.x - self.width / 2
        y = self.position.y - self.height / 2
        renderEngine.drawVeichle('truck', x, y, self.width, self.height, self.angle, self.width, self.height)