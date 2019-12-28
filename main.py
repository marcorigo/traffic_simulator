import sys
sys.path.insert(0, './veichles')
from tkinter import Tk, Canvas
from threading import Timer
from map import Map
from render import RenderEngine
import pygame
from veichle import Veichle

ROAD_MAP    =  [[ 0 ,  0,  '╔', '═', '═', '╗'],
                [ 0 ,  0,  '║',  0,   0,  '║'],
                ['═', '═', '╬', '═', '═', '╝'],
                [ 0 ,  0,  '║',  0,   0,   0 ],
                [ 0 ,  0,  '║',  0,   0,   0 ]]

BLOCK_SIZE = 150

WIDTH = len(ROAD_MAP[0]) * BLOCK_SIZE
HEIGHT = len(ROAD_MAP) * BLOCK_SIZE


def game():
    pygame.init()
    clock = pygame.time.Clock()
    canvas = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('A bit Racey')
    font = pygame.font.Font(None, 30)

    renderEngine = RenderEngine(canvas, pygame, WIDTH, HEIGHT)

    map = Map(renderEngine, ROAD_MAP, BLOCK_SIZE)
    
    map.createRoads(ROAD_MAP)
    
    # path = [[2,0]]
    # car1 = map.addVeichle(path, 3, False)

    #Path 1
    path = [[2,0],[2,1],[2,2],[3,2], [4, 2], [5, 2], [5, 1], [5, 0], [4, 0], [3, 0], [2, 0], [2, 1], [2, 2], [1, 2], [0, 2]]
    map.addVeichle(path)
    #Path 2
    path = [[1,2],[2,2],[2,1], [2, 0], [3, 0], [4, 0], [5, 0], [5, 1], [5, 2], [4, 2], [3, 2], [2, 2], [2, 3], [2, 4], [2, 5]]
    map.addVeichle(path)


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
                    car1.controls["right"] = True
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
                    car1.controls["right"] = False
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