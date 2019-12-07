class RenderEngine:
    def __init__(self, canvas, pygame, width, heigth):
        self.pygame = pygame
        self.canvas = canvas
        self.width = width
        self.heigth = heigth
        self.car = self.pygame.image.load('car.png').convert_alpha()

    def drawVeichle(self, x, y, width, heigth, angle):
        if(angle < 0):
            angle = angle * -1
        else:
            angle = -angle
        self.car = self.pygame.transform.scale(self.car, (width, heigth))
        surf = self.pygame.transform.rotate(self.car, angle)
        self.canvas.blit(surf, (x, y))
        # self.pygame.draw.rect(self.canvas, (0,100,100), (x, y, width, heigth))

    def drawRect(self, x, y, width, heigth, color):
        self.pygame.draw.rect(self.canvas, color, (x, y, width, heigth))

    def move(self, element, x = 0, y = 0):
        self.canvas.move(element, x, y)
