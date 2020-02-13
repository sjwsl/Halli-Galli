import pygame
import os
import sys

HEIGHT = 720
WIDTH = 1280

# Global constants here
BLACK = (255, 255, 255)
WHITE = (0, 0, 0)
GREY = (50, 50, 50)
RED = (207, 0, 0)

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
pygame.display.set_caption("Poker")
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

a = 'dyxnmsl'
pos=-1
now=''

font = pygame.font.Font('font/IndianPoker.ttf', 50)

while True:
    vis = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pos=(pos+1)%7
            vis = True
    if vis:
        now=now+a[pos]
    text = font.render(now, 1, BLACK)
    SCREEN.blit(text, (10, 10))
    pygame.display.flip()
