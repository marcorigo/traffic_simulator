from veichle import Veichle

class Car(Veichle):
    def __init__(self, cell_width, path, posx, posy, angle, field_vision_width = 50, field_vision_height = 50):
        super().__init__(path, posx, posy, angle)
        self.cell_width = cell_width
        self.field_vision_width = field_vision_width
        self.field_vision_height = field_vision_height
        self.width = int(self.cell_width / 3)
        self.heigth = int(self.cell_width / 5)

    def draw(self, renderEngine):
        renderEngine.drawVeichle(self.position, self.width, self.heigth, self.angle, self.field_vision_width, self.field_vision_height)