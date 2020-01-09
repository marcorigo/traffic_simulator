import sys
sys.path.insert(0, './veichles')
from tkinter import Tk, Canvas
from threading import Timer
from map import Map
from render import RenderEngine
import pygame
from veichle import Veichle

# ROAD_MAP    =  [[ 0 ,  0,   0,  0,   0,  '⬇',  0 ,  0 ],
#                 [ 0 ,  0,  '╔','═', '═', '╬', '═', '╗'],
#                 [ 0 ,  0,  '║', 0,   0,  '║',  0 , '║'],
#                 ['➡', '═','╬','═', '═', '╬', '═', '╝'],
#                 [ 0 ,  0,  '║', 0  , 0,  '║',  0 ,  0 ],
#                 [ 0 ,  0,  '║', 0  , 0,  '║',  0 ,  0 ],
#                 [ 0 ,  0,  '║', 0  , 0,  '║', 0 ,  '╔'],
#                 [ 0 ,  0,  '║', 0  , 0,  '║',  0 , '║'],
#                 [ 0 ,  0,  '║', 0  , 0,  '║',  0 , '║'],
#                 ['➡', '═','╬','═' ,'═', '╬', '═', '╝'],
#                 [ 0 ,  0,  '║', 0,   0,  '║',  0 ,  0 ],
#                 [ 0 ,  0,  '║', 0,   0,  '⬆',  0 ,  0 ]]

ROAD_MAP    =  [[ 0,  0,  0,  '⬇',  0,  0,  0,  0,  0,  0,  0, '⬇',  0,  0,  0 ],
                [ 0,  0,  0,  '║',  0,  0,  0,  0,  0,  0,  0, '║',  0,  0,  0 ],
                [ 0,  0,  0,  '║',  0,  0,  0,  0,  0,  0,  0, '║',  0,  0,  0 ],
                ['➡','═','═','╬', '═','═','═','╦','═','═','═','╬', '═','═','═'],
                [ 0,  0,  0,  '║',  0,  0,  0, '║', 0,  0,  0, '║',  0,  0,  0 ],
                [ 0,  0,  0,  '║',  0,  0,  0, '║', 0,  0,  0, '║',  0,  0,  0 ],
                [ 0,  0,  0,  '║',  0,  0,  0, '║', 0,  0,  0, '║',  0,  0,  0 ],
                [ 0,  0,  0,  '╠', '═','═','═','╬','═','═','═','╣',  0,  0,  0 ],
                [ 0,  0,  0,  '║',  0,  0,  0, '║', 0,  0,  0, '║',  0,  0,  0 ],
                [ 0,  0,  0,  '║',  0,  0,  0, '║', 0,  0,  0, '║',  0,  0,  0 ],
                [ 0,  0,  0,  '║',  0,  0,  0, '║', 0,  0,  0, '║',  0,  0,  0 ],
                ['═','═','═', '╬', '═','═','═','╩','═','═','═','╬', '═','═','⬅'],
                [ 0,  0,  0,  '║',  0,  0,  0,  0,  0,  0,  0, '║',  0,  0,  0 ],
                [ 0,  0,  0,  '║',  0,  0,  0,  0,  0,  0,  0, '║',  0,  0,  0 ],
                [ 0,  0,  0,  '║',  0,  0,  0,  0,  0,  0,  0, '⬆',  0,  0,  0 ]]


BLOCK_SIZE = 50

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

    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                    
        canvas.fill((120, 226, 104))

        Veichle.dt = clock.get_time() / 1000

        map.update()

        pygame.display.update()
        clock.tick(60)
game()