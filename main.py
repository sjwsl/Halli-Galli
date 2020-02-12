import pygame
import os
import sys

HEIGHT = 720
WIDTH = 1280

# Global constants here
BLACK = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)
RED = (207, 0, 0)

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
pygame.display.set_caption("Poker")
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

a = 0

font = pygame.font.Font('font/CoffeeTin.ttf', 50)

while True:
    vis = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            a = a + 1
            vis = True
    if vis == False:
        continue
    print(a)
