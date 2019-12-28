from veichle import Veichle

class Car(Veichle):
    def __init__(self, posx = 0, posy = 0, rotation = 0, view_heigth = 30, view_width = 30, max_speed = 100):
        super().__init__(view_heigth, view_width, max_speed, posx, posy, rotation)
        self.width = 50
        self.heigth = 30