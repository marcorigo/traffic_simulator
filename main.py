from config import config

import sys
map_selected = 0
try:
    map_selected = int(sys.argv[1])
except :
    pass
from maps import maps

ROAD_MAP = maps[map_selected]

from game_map import Map
from render import RenderEngine
import pygame
from veichle import Veichle


BLOCK_SIZE = config['BLOCK_SIZE']
DEBUG = config['DEBUG']

WIDTH = len(ROAD_MAP[0]) * BLOCK_SIZE
HEIGHT = len(ROAD_MAP) * BLOCK_SIZE

BACKGROUND_COLOR = config['BACKGROUND_COLOR']

def game():
    pygame.init()
    clock = pygame.time.Clock()
    canvas = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Traffic Simulation')
    FONT = pygame.font.SysFont("Bizarre-Ass Font Sans Serif", 20)

    renderEngine = RenderEngine(canvas, pygame, BLOCK_SIZE, WIDTH, HEIGHT, FONT)

    game_map = Map(renderEngine, ROAD_MAP, BLOCK_SIZE, DEBUG)

    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

        if not config['USE_TEXTURES']:     
            canvas.fill(BACKGROUND_COLOR)

        Veichle.dt = clock.get_time() / 1000

        game_map.update()

        message = 'Time: ' + str(int(pygame.time.get_ticks() / 1000))
        renderEngine.drawText(message, 20, 20)
        renderEngine.drawText('Fps: ' + str(int(clock.get_fps())), 20, 40)

        pygame.display.update()
        pygame.display.flip()
        clock.tick(180)
game()