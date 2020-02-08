import pygame, sys
from pygame.locals import *

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

# Set up fonts
basicFont = pygame.font.SysFont(None, 48)

# draw the white background onto the surface
screen.fill(WHITE)

# draw the sudoku grid
corners = [100, 50, 400, 350]
x_div = (corners[2]-corners[0])/9
y_div = (corners[3]-corners[1])/9
# Draw the lines
for i in range(10):
    if i%3 == 0:
        gross = 4
    else:
        gross = 1
    x= corners[0] + i*x_div
    y= corners[1] + i*y_div
    # Vertical line
    pygame.draw.line(screen, BLACK, (x , corners[1]), (x, corners[3]), gross) 
    # Horizontal line
    pygame.draw.line(screen, BLACK, (corners[0], y), (corners[2], y), gross)



# draw the window onto the screen
pygame.display.update()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()