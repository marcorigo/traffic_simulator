from tkinter import Canvas
from random import Random

class Veichle:
    def __init__(self, posx = 0, posy = 0, rotation = 0, view_heigth = 30, view_width = 30, max_speed = 100):
        self.posx = posx
        self.posy = posy
        self.rotation = rotation
        self.max_speed = max_speed
        self.view_width = view_width
        self.view_heigth = view_heigth
        self.model = None
        self.speed = 0.2
    
    def move(self):
        self.posx += self.speed