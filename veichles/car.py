from veichle import Veichle

class Car(Veichle):
    def __init__(self,id, sprite_name, width, heigth, posx, posy, angle = 0):
        super().__init__(id, posx, posy, angle)
        self.width = width
        self.heigth = heigth
        self.sprite_name = sprite_name

    # Get heigth and width on orizontal axis for easy collision detection
    def getWidth(self):
        if self.facing == 1 or self.facing == 3:
            return int(self.heigth)
        return int(self.width)

    def getHeigth(self):
        if self.facing == 1 or self.facing == 3:
            return int(self.width)
        return int(self.heigth)

    def draw(self, renderEngine):
        x = self.position.x - self.width / 2
        y = self.position.y - self.heigth / 2
        renderEngine.drawVeichle(self.sprite_name, x, y, self.width, self.heigth, self.angle, self.width, self.heigth)