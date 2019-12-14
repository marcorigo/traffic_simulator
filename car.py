from veichle import Veichle

class Car(Veichle):
    def __init__(self, width, heigth, posx, posy, angle, field_vision_width = 50, field_vision_height = 50):
        super().__init__(posx, posy, angle)
        self.field_vision_width = field_vision_width
        self.field_vision_height = field_vision_height
        self.width = width
        self.heigth = heigth

    def draw(self, renderEngine):
        renderEngine.drawVeichle(self.position, self.width, self.heigth, self.angle, self.field_vision_width, self.field_vision_height)