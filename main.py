import pygame, sys
from pygame.locals import *

from sudoku import *

# Initialize pygame modules
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((500, 400), 0, 32) 
pygame.display.set_caption("Sudoku")

# set up some basic colors in RGB Tuples
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# draw the white background onto the surface
screen.fill(WHITE)

# Set up fonts
basicFont = pygame.font.SysFont(None, 48)
numberFont = pygame.font.SysFont(None, 36)

# Initialize Sudoku
sk = Sudoku(screen, numberFont)

# set up the text
text = basicFont.render('Sudoku', True, BLACK, WHITE)
textRect = text.get_rect()
textRect.top = screen.get_rect().top 
textRect.centerx = screen.get_rect().centerx

screen.blit(text, textRect)

sk.draw(BLACK)


# draw the window onto the screen
pygame.display.update()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()