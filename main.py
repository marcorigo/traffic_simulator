from tkinter import Tk, Canvas
from threading import Timer
from map import Map
from render import RenderEngine
import pygame

WIDTH = 500
HEIGHT = 500

def game():
    pygame.init()
    canvas = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('A bit Racey')
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)

    renderEngine = RenderEngine(canvas, pygame, WIDTH, HEIGHT)

    road_map    =  [['=', '|'],
                    [0, 0],
                    [0, 0]]

    map = Map(renderEngine, road_map, 100)
    map.createRoads(road_map)
    map.addVeichle()

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_a:
                view.move('a')
            elif ev.key == pygame.K_d:
                view.move('d')
        canvas.fill((173,216,230))
        map.update()
        # print(clock.get_fps())
        #pygame.display.flip()
        pygame.display.update()
        clock.tick(60)
    pygame.quit()
game()