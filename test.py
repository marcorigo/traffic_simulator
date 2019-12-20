# import pygame, sys
# from pygame.locals import *
# import math
# pygame.init()
# mainClock = pygame.time.Clock()
# degree = 0
# WHITE = 250,250,250
# rect2 = pygame.rect = (100,100,50,50)
# WINDOWWIDTH = 1200
# WINDOWHEIGHT = 750
# thing = pygame.image.load('car.png')
# screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
# pygame.display.set_caption('Teh test')
# left = False
# right = False
# position = (100, 100)
# while True:
#     rect2 = pygame.rect = (100,100,50,50)
#     if right == True:
#         degree -= 2
#     if left == True:
#         degree += 2
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == KEYDOWN:
#             if event.key == ord('a'):
#                 left = True
#             if event.key == ord('d'):
#                 right = True
#         if event.type == KEYUP:
#             if event.key == ord('a'):
#                 left = False
#             if event.key == ord('d'):
#                 right = False
#     pygame.draw.rect(screen,WHITE,rect2)
#     screen.fill((40, 40, 40))
#     thing2 = pygame.transform.rotate(thing,degree)
#     dx = math.cos(math.radians(degree))
#     dy = math.sin(math.radians(degree))
#     position = (position[0] + dx, position[1] - dy)
#     screen.blit(thing2, position)
#     pygame.display.update()
#     mainClock.tick(60)





# import pygame as py  

# # define constants  
# WIDTH = 500  
# HEIGHT = 500  
# FPS = 30  

# # define colors  
# BLACK = (0 , 0 , 0)  
# GREEN = (0 , 255 , 0)  

# # initialize pygame and create screen  
# py.init()  
# screen = py.display.set_mode((WIDTH , HEIGHT))  
# # for setting FPS  
# clock = py.time.Clock()  

# rot = 0  
# rot_speed = 2  

# # define a surface (RECTANGLE)  
# image_orig = py.Surface((100 , 100))  
# # for making transparent background while rotating an image  
# image_orig.set_colorkey(BLACK)  
# # fill the rectangle / surface with green color  
# image_orig.fill(GREEN)  
# # creating a copy of orignal image for smooth rotation  
# image = image_orig.copy()  
# image.set_colorkey(BLACK)  
# # define rect for placing the rectangle at the desired position  
# rect = image.get_rect()  
# rect.center = (WIDTH // 2 , HEIGHT // 2)  
# # keep rotating the rectangle until running is set to False  
# running = True  
# while running:  
#     # set FPS  
#     clock.tick(FPS)  
#     # clear the screen every time before drawing new objects  
#     screen.fill(BLACK)  
#     # check for the exit  
#     for event in py.event.get():  
#         if event.type == py.QUIT:  
#             running = False  

#     # making a copy of the old center of the rectangle  
#     old_center = rect.center  
#     # defining angle of the rotation  
#     rot = (rot + rot_speed) % 360  
#     # rotating the orignal image  
#     new_image = py.transform.rotate(image_orig , rot)  
#     rect = new_image.get_rect()  
#     # set the rotated rectangle to the old center  
#     rect.center = old_center  
#     # drawing the rotated rectangle to the screen  
#     screen.blit(new_image , rect)  
#     # flipping the display after drawing everything  
#     py.display.flip()  

# py.quit()  





# import sys, pygame
# from pygame.locals import *

# pygame.init()
# SCREEN = pygame.display.set_mode((200, 200))
# CLOCK  = pygame.time.Clock()

# surface = pygame.Surface((50 , 50))
# surface.fill((0, 0, 0))
# rotated_surface = surface
# rect = surface.get_rect()
# angle = 0

# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()

#     SCREEN.fill((255, 255, 255))
#     angle += 5
#     rotated_surface = pygame.transform.rotate(surface, angle)
#     rect = rotated_surface.get_rect(center = (100, 100))
#     SCREEN.blit(rotated_surface, (rect.x, rect.y))

#     pygame.display.update()
#     CLOCK.tick(30)





