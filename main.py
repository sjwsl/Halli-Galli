import pygame
import os
import sys
import random
import time

HEIGHT = 720
WIDTH = 1280

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)
RED = (207, 0, 0)

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
pygame.display.set_caption("Poker")
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

pos = -1

font = pygame.font.Font('font/IndianPoker.ttf', 50)

a = [random.randint(0, 10) for i in range(0, 4)]

def gg(stat):
    print(stat)
    if stat == 1:
        text = font.render("You win!", 1, BLACK)
    else:
        text = font.render("You lose!", 1, BLACK)

    SCREEN.blit(text, (200, 300))
    pygame.display.update()
    pygame.time.set_timer(CHANGE, 0)
    input()



# 自定义计时事件
CHANGE = pygame.USEREVENT + 1

# 每隔1秒发送一次自定义事件
pygame.time.set_timer(CHANGE, 2000)

while True:
    SCREEN.fill(WHITE)
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
                for i in a:
                    print(i)
                gg(0)
                break
            pos = (pos + 1) % 4
            a[pos] = random.randint(0, 10)
        elif event.type == pygame.KEYDOWN:
            sum = 0
            for i in a:
                sum += i
            if sum % 10 == 0:
                gg(1)
            else:
                gg(0)
    SCREEN.blit(font.render(str(a[0]), 1, BLACK), (10, 10))
    SCREEN.blit(font.render(str(a[1]), 1, BLACK), (10, 80))
    SCREEN.blit(font.render(str(a[2]), 1, BLACK), (10, 150))
    SCREEN.blit(font.render(str(a[3]), 1, BLACK), (10, 220))
    pygame.display.update()
