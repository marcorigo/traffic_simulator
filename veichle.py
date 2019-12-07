from tkinter import Canvas
from random import Random
import math

class Veichle:
    def __init__(self, posx = 0, posy = 0):
        self.x = posx
        self.y = posy
        self.model = None
        self.speed = 1
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0
        self.rv = 0
        self.angle = 0
        self.accelerationAmount = 0.005
        self.decelerationAmount = 0.005
        self.friction = 0.97
        self.rotation = 2
        self.controls = { "up": False, "down": False, "left": False, "rigth": False }
    
    def move(self):
        print(self.angle)
        if self.controls["up"]:
            self.accelerate(False)
        if self.controls["down"]:
            self.accelerate(True)
        if self.controls["left"]:
            self.rotate('left')
        if self.controls["rigth"]:
            self.rotate('rigth')

    def accelerate(self, backwards):
        if backwards:
            self.ax -= math.cos(math.radians(self.angle)) * self.decelerationAmount
            self.ay -= math.sin(math.radians(self.angle)) * self.decelerationAmount
        else:
            self.ax += math.cos(math.radians(self.angle)) * self.accelerationAmount
            self.ay += math.sin(math.radians(self.angle)) * self.accelerationAmount

    def updatePosition(self):
        self.vx += self.ax
        self.vy += self.ay

        # if(self.x + 20 + self.vx > width):
        #   self.x = width - 20
        #   self.vx = 0
        #   self.ax = 0

        # if(self.x + self.vx < 0):
        #   self.x = 0
        #   self.vx = 0
        #   self.ax = 0

        # if(self.y + self.vy < 0):
        #   self.y = 0
        #   self.vy = 0
        #   self.ay = 0

        # if(self.y + 20 + self.vy > height):
        #   self.y = height - 20
        #   self.vy = 0
        #   self.ay = 0

        #Update position
        self.x += self.vx
        self.y += self.vy
        self.applyFriction()

    def applyFriction(self):
        self.vx *= self.friction
        self.vy *= self.friction
        self.ax *= self.friction
        self.ay *= self.friction

    def rotate(self, dir):
        if(dir == 'left'): 
            self.angle += self.rotation
        else: 
            self.angle -= self.rotation