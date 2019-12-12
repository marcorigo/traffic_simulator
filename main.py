from tkinter import Tk, Canvas
from threading import Timer
from map import Map
from render import RenderEngine
import pygame
from veichle import Veichle

WIDTH = 800
HEIGHT = 800

def game():
    pygame.init()
    clock = pygame.time.Clock()
    canvas = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('A bit Racey')
    font = pygame.font.Font(None, 30)

    renderEngine = RenderEngine(canvas, pygame, WIDTH, HEIGHT)

    road_map    =  [[ 0 ,  0,  '|',  0,   0],
                    [ 0 ,  0,  '|',  0,   0],
                    ['=', '=', '#', '=', '='],
                    [ 0 ,  0,  '|',  0,   0],
                    [ 0 ,  0,  '|',  0,   0]]

    map = Map(renderEngine, road_map, 100)
    
    map.createRoads(road_map)
    car1 = map.addVeichle()

    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if ev.type == pygame.KEYDOWN:
                if ev.key == ord('w'):
                    car1.controls["up"] = True
                elif ev.key == ord('s'):
                    car1.controls["down"] = True
                elif ev.key == ord('a'):
                    car1.controls["left"] = True
                elif ev.key == ord('d'):
                    car1.controls["rigth"] = True
                elif ev.key == [pygame.K_SPACE]:
                    car1.controls["space"] = True
            if ev.type == pygame.KEYUP:
                if ev.key == ord('w'):
                    car1.controls["up"] = False
                elif ev.key == ord('s'):
                    car1.controls["down"] = False
                elif ev.key == ord('a'):
                    car1.controls["left"] = False
                elif ev.key == ord('d'):
                    car1.controls["rigth"] = False
                elif ev.key == [pygame.K_SPACE]:
                    car1.controls["space"] = False
                    
        canvas.fill((120, 226, 104))

        Veichle.dt = clock.get_time() / 1000

        map.update()

        # print(clock.get_fps())
        # pygame.display.flip()
        pygame.display.update()
        clock.tick(60)
game()