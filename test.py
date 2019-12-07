import pygame, sys
from pygame.locals import *
import math
pygame.init()
mainClock = pygame.time.Clock()
degree = 0
WHITE = 250,250,250
rect2 = pygame.rect = (100,100,50,50)
WINDOWWIDTH = 1200
WINDOWHEIGHT = 750
thing = pygame.image.load('car.png')
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Teh test')
left = False
right = False
position = (100, 100)
while True:
    rect2 = pygame.rect = (100,100,50,50)
    if right == True:
        degree -= 2
    if left == True:
        degree += 2
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == ord('a'):
                left = True
            if event.key == ord('d'):
                right = True
        if event.type == KEYUP:
            if event.key == ord('a'):
                left = False
            if event.key == ord('d'):
                right = False
    pygame.draw.rect(screen,WHITE,rect2)
    screen.fill((40, 40, 40))
    thing2 = pygame.transform.rotate(thing,degree)
    dx = math.cos(math.radians(degree))
    dy = math.sin(math.radians(degree))
    position = (position[0] + dx, position[1] - dy)
    screen.blit(thing2, position)
    pygame.display.update()
    mainClock.tick(60)