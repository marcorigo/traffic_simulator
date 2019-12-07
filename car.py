from veichle import Veichle

class Car(Veichle):
    def __init__(self, cell_width, posx = 0, posy = 0):
        super().__init__(posx, posy,)
        self.cell_width = cell_width
        self.width = int(self.cell_width / 3)
        self.heigth = int(self.cell_width / 5)