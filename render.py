class RenderEngine:
    def __init__(self, canvas, pygame, width, height):
        self.pygame = pygame
        self.canvas = canvas
        self.width = width
        self.height = height
        self.car = self.pygame.image.load('car.png').convert_alpha()

    def drawVeichle(self, position, width, height, angle):
        self.car = self.pygame.transform.scale(self.car, (width, height))
        surf = self.pygame.transform.rotate(self.car, angle)
        self.canvas.blit(surf, position * 32 - (width / 2, height / 2))
        # self.pygame.draw.rect(self.canvas, (0,100,100), (x, y, width, height))

    def drawRect(self, x, y, width, height, color):
        self.pygame.draw.rect(self.canvas, color, (x, y, width, height))

    def move(self, element, x = 0, y = 0):
        self.canvas.move(element, x, y)
