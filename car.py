from veichle import Veichle

class Car(Veichle):
    def __init__(self, cell_width, posx = 0, posy = 0, rotation = 0, view_heigth = 30, view_width = 30):
        super().__init__(view_heigth, view_width, posx, posy, rotation)
        self.cell_width = cell_width
        self.width = self.cell_width / 7
        self.heigth = self.cell_width / 10