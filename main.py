import pygame
import os
import sys
import random

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

a = [0, 0, 0, 0]

pos = -1
now = ''

font = pygame.font.Font('font/IndianPoker.ttf', 50)

# 自定义计时事件
CHANGE = pygame.USEREVENT + 1

# 每隔1秒发送一次自定义事件
pygame.time.set_timer(CHANGE, 1000)


def gg(stat):
    if stat == 1:
        text = font.render("You win!", 1, BLACK)
    else:
        text = font.render("You lose!", 1, BLACK)
    pygame.time.set_timer(CHANGE, 0)


while True:
    vis = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit()
        elif event.type == CHANGE:
            sum = 0
            for i in a:
                sum += i
            if sum % 10 == 0:
                gg(0)
            pos = (pos + 1) % 4
            a[pos] = random.randint() % 10
        elif event.type == pygame.KEYDOWN:
            sum = 0
            for i in a:
                sum += i
            if sum % 10 == 0:
                gg(1)
            else:
                gg(0)

    SCREEN.blit(font.render(a[0], 1, BLACK), (10, 10))
    SCREEN.blit(font.render(a[0], 1, BLACK), (10, 70))
    SCREEN.blit(font.render(a[0], 1, BLACK), (10, 10))
    SCREEN.blit(font.render(a[0], 1, BLACK), (10, 10))
    pygame.display.flip()
