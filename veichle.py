from tkinter import Canvas
from random import Random
from math import sin, radians, degrees, copysign
from pygame.math import Vector2

class Veichle:
    dt = 0
<<<<<<< HEAD
    def __init__(self, posx, posy, angle=0.0, length=4, max_steering=30, max_acceleration=80.0):
=======
    def __init__(self, path, posx, posy, angle = 0.0, length=30, max_steering=30, max_acceleration=200.0):
>>>>>>> test
        self.model = None
        self.position = Vector2(posx, posy)
        self.path = path
        self.velocity = Vector2(0.0, 0.0)
        self.angle = angle
        self.length = length
        self.max_acceleration = max_acceleration
        self.max_steering = max_steering
        self.max_velocity = 150
        self.brake_deceleration = 30
        self.free_deceleration = 5
        self.acceleration = 0.0
        self.steering = 0.0
        self.controls = { "up": False, "down": False, "left": False, "rigth": False, "space": False }
    
    def move(self):
        if self.controls['up']:
            if self.velocity.x < 0:
                self.acceleration = self.brake_deceleration
            else:
                self.acceleration += 1 * self.dt
        elif self.controls['down']:
            if self.velocity.x > 0:
                self.acceleration = -self.brake_deceleration
            else:
                self.acceleration -= 1 * self.dt
        elif self.controls['space']:
            if abs(self.velocity.x) > self.dt * self.brake_deceleration:
                self.acceleration = -copysign(self.brake_deceleration, self.velocity.x)
            else:
                self.acceleration = -self.velocity.x / self.dt
        else:
            if abs(self.velocity.x) > self.dt * self.free_deceleration:
                self.acceleration = -copysign(self.free_deceleration, self.velocity.x)
            else:
                if self.dt != 0:
                    self.acceleration = -self.velocity.x / self.dt
        self.acceleration = max(-self.max_acceleration, min(self.acceleration, self.max_acceleration))
        if self.controls['left']:
            self.steering += 30 * self.dt
        elif self.controls['rigth']:
            self.steering -= 30 * self.dt
        else:
            self.steering = 0

        self.steering = max(-self.max_steering, min(self.steering, self.max_steering))

    def update(self):
        self.velocity += (self.acceleration * self.dt, 0)
        self.velocity.x = max(-self.max_velocity, min(self.velocity.x, self.max_velocity))

        if self.steering:
            turning_radius = self.length / sin(radians(self.steering))
            angular_velocity = self.velocity.x / turning_radius
        else:
            angular_velocity = 0

        self.position += self.velocity.rotate(-self.angle) * self.dt
        self.angle += degrees(angular_velocity) * self.dt