from veichle import Veichle

class Car(Veichle):
    def __init__(self,id, width, heigth, posx, posy, angle = 0):
        super().__init__(id, posx, posy, angle)
        self.width = width
        self.heigth = heigth

    def draw(self, renderEngine):
        x = self.position.x - self.width / 2
        y = self.position.y - self.heigth / 2
        renderEngine.drawVeichle(x, y, self.width, self.heigth, self.angle, self.width, self.heigth)