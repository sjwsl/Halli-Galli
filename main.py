import pygame
import random
import os, sys

HEIGHT = 720
WIDTH = 1280

# Global constants here
BLACK = (255, 255, 255)
WHITE = (0, 0, 0)
GREY = (50, 50, 50)
RED = (207, 0, 0)


class Control:
    def __init__(self):
        self.images = {}
        self.scale = .5
        self.cardSize = (WIDTH / 7, WIDTH / 5)
        self.buffer = 50
        self.background = pygame.image.load('img/background.jpg').convert_alpha()
        self.cardBack = pygame.image.load('img/back.png').convert_alpha()
        self.cardBack = pygame.transform.scale(self.cardBack,
                                               (int(self.scale * self.cardSize[0]), int(self.scale * self.cardSize[1])))

        font = pygame.font.Font('font/CoffeeTin.ttf', 50)
        loadText = font.render("Loading...", 1, BLACK)
        loadSize = font.size("Loading...")
        loadLoc = (WIDTH / 2 - loadSize[0] / 2, HEIGHT / 2 - loadSize[1] / 2)

        self.scores = [0, 0, 0, 0]

        SCREEN.blit(self.background, (-320, -100))

        SCREEN.blit(loadText, loadLoc)

        pygame.display.flip()

        self.start_up_init()

    def main(self):
        if self.state == 0:
            self.start_up()
        elif self.state == 1:
            self.play()
        elif self.state == 2:
            self.results()
        elif self.state == 3:
            self.new_game()

    def start_up_init(self):
        # initialize items for the startup section of the game

        self.font = pygame.font.Font('font/CoffeeTin.ttf', 150)
        self.font2 = pygame.font.Font('font/IndianPoker.ttf', 75)
        self.font2.set_bold(True)

        self.startText = self.font2.render("Welcome to Poker!", 1, BLACK)
        self.startSize = self.font2.size("Welcome to Poker!")
        self.startLoc = (WIDTH / 2 - self.startSize[0] / 2, self.buffer)

        self.startButton = self.font.render(" Start ", 1, BLACK)
        self.buttonSize = self.font.size(" Start ")
        self.buttonLoc = (WIDTH / 2 - self.buttonSize[0] / 2, HEIGHT / 2 - self.buttonSize[1] / 2)

        self.buttonRect = pygame.Rect(self.buttonLoc, self.buttonSize)
        self.buttonRectOutline = pygame.Rect(self.buttonLoc, self.buttonSize)

        self.state = 0

    def start_up(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                sys.exit()

            # when the user clicks the start button, change to the playing state
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouseRect = pygame.Rect(event.pos, (1, 1))
                    if mouseRect.colliderect(self.buttonRect):
                        self.state += 1
                        self.play_init()
                        return

        # draw background
        SCREEN.blit(self.background, (-320, -100))

        # draw welcome text
        SCREEN.blit(self.startText, self.startLoc)

        # draw the start button
        pygame.draw.rect(SCREEN, RED, self.buttonRect)
        pygame.draw.rect(SCREEN, BLACK, self.buttonRectOutline, 2)
        SCREEN.blit(self.startButton, self.buttonLoc)

        pygame.display.flip()

    def play_init(self):

        self.numbers = [random.randint(0, 10) for i in range(0, 4)]

        # setup the text that will be printed to the screen
        self.font = pygame.font.Font('font/IndianPoker.ttf', 25)
        self.font.set_bold(True)
        self.font2 = pygame.font.Font('font/CoffeeTin.ttf', 60)
        self.youText = self.font.render("Your Hand", 1, BLACK)
        self.youSize = self.font.size("Your Hand")
        self.replaceButton = self.font2.render(" Replace ", 1, BLACK)
        self.buttonSize = self.font2.size(" Replace ")
        self.buttonRect = pygame.Rect(self.buttonLoc, self.buttonSize)
        self.buttonRectOutline = pygame.Rect(self.buttonLoc, self.buttonSize)

    def play(self):
        print('play!')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                sys.exit()

            # when the user clicks on a card, change its color to signify a selection has occurred
            elif event.type == pygame.KEYDOWN:
                ++self.state
                self.results_init()
                return

        # display background
        SCREEN.blit(self.background, (-320, -100))

        self.display()

        pygame.display.flip()

    def results_init(self):
        # initialize variables for the button
        # self.font = pygame.font.Font('font/IndianPoker.ttf', 25)
        self.replaceButton = self.font2.render(" New Game ", 1, BLACK)
        self.buttonSize = self.font2.size(" New Game ")

        self.buttonLoc = (self.buttonLoc[0], self.buffer + self.scale * self.cardSize[1] / 2 - self.buttonSize[1] / 2)

        self.buttonRect = pygame.Rect(self.buttonLoc, self.buttonSize)
        self.buttonRectOutline = pygame.Rect(self.buttonLoc, self.buttonSize)

    def results(self):
        print('over!')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                sys.exit()
            # when the user clicks the start button, change to the playing state
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseRect = pygame.Rect(event.pos, (1, 1))
                if mouseRect.colliderect(self.buttonRect):
                    # self.start_up_init()
                    self.state = 1
                    self.play_init()
                    return

        # display background
        SCREEN.blit(self.background, (-320, -100))

        # display a play again button
        pygame.draw.rect(SCREEN, RED, self.buttonRect)
        pygame.draw.rect(SCREEN, BLACK, self.buttonRectOutline, 2)
        SCREEN.blit(self.replaceButton, self.buttonLoc)

        pygame.display.flip()

    def display(self):
        SCREEN.blit(self.font.render(str(self.numbers[0]), 1, BLACK), (10, 10))
        SCREEN.blit(self.font.render(str(self.numbers[1]), 1, BLACK), (10, 80))
        SCREEN.blit(self.font.render(str(self.numbers[2]), 1, BLACK), (10, 150))
        SCREEN.blit(self.font.render(str(self.numbers[3]), 1, BLACK), (10, 220))


#############################################################
if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'  # center screen
    pygame.init()
    pygame.display.set_caption("Poker")
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    Runit = Control()
    Myclock = pygame.time.Clock()
    while 1:
        Runit.main()
        Myclock.tick(10)
