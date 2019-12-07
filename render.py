class RenderEngine:
    def __init__(self, canvas, pygame, width, heigth):
        self.pygame = pygame
        self.canvas = canvas
        self.width = width
        self.heigth = heigth
        self.car = self.pygame.image.load('car.png')
        self.car = pygame.transform.scale(self.car, (45, 20))

    def drawVeichle(self, x, y, width, heigth, color, rotation):
        surf = self.pygame.transform.rotate(self.car, rotation)
        self.canvas.blit(surf, (x, y))
        # s = self.pygame.draw.rect(self.canvas, (0, 137, 238), (x, y, width, heigth))
        # self.pygame.transform.rotate(s, 10)

    def drawRect(self, x, y, width, heigth, color):
        self.pygame.draw.rect(self.canvas, color, (x, y, width, heigth))

    def move(self, element, x = 0, y = 0):
        self.canvas.move(element, x, y)
