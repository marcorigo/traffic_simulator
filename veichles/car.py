from veichle import Veichle

class Car(Veichle):
    def __init__(self,id, sprite_name, width, height, posx, posy, angle = 0):
        super().__init__(id, posx, posy, angle)
        self.width = width
        self.height = height
        self.sprite_name = sprite_name

    # Get height and width on orizontal axis for easy collision detection
    def getWidth(self):
        if self.facing == 1 or self.facing == 3:
            return int(self.height)
        return int(self.width)

    def getHeight(self):
        if self.facing == 1 or self.facing == 3:
            return int(self.width)
        return int(self.height)

    def draw(self, renderEngine):
        x = self.position.x - self.width / 2
        y = self.position.y - self.height / 2
        renderEngine.drawVeichle(self.sprite_name, x, y, self.width, self.height, self.angle, self.width, self.height)