# This code solves a 9x9 sudoku game given.
import pygame

class Sudoku:

    def __init__(self, screen, font):
        # Al inicializar esto, debe escoger uno al azar, resolverlo y dibujarlo.
        self.puzzle= self.select()
        self.screen = screen
        self.font = font

    def select(self):
        # For de moment I'll just use this one as a trail.
        return "...21...5..2.46..1........9......95.4....7..6....85...9.1..2.84..8.7.1..2.6...7.."

    def draw(self, color):
        # draw the sudoku grid
        corners = [100, 50, 400, 350] #[x1, y1, x2, y2]
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
            pygame.draw.line(self.screen, color, (x , corners[1]), (x, corners[3]), gross) 
            # Horizontal line
            pygame.draw.line(self.screen, color, (corners[0], y), (corners[2], y), gross)
        self.printNumbers(self.screen, corners, x_div, y_div, color)

    def printNumbers(self, screen, corners, x_div, y_div, color):
        # Print the numbers of the sudoku in the grid

        #First: get an array with square coordinates
        sq_coord=[[0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0,0,0]]
        for i in range(9):
            y1= corners[1] + i*y_div; y2= y1 + y_div
            for j in range(9):
                x1= corners[0] + j*x_div; x2= x1 + x_div
                sq_coord[i][j]= (0.5*(x1 + x2), 0.5*(y1 + y2))

        # Write the number
        for i in range(9):
            for j in range(9):
                # set up the text
                place= i*9 + j
                if self.puzzle[place] != '.':
                    text = self.font.render(self.puzzle[place], True, color, (255,255,255))
                    textRect = text.get_rect()
                    textRect.centery = sq_coord[i][j][1]
                    textRect.centerx = sq_coord[i][j][0]

                    screen.blit(text, textRect)





def Check(sk, n):
    numRow= n//9;   numCol= n%9
    
    #Check Row
    for i in range(9):
        place= 9*numRow + i
        if (place != n) and sk[place] == sk[n]:
            return False 
    #Check Column
    for i in range(9):
        place= 9*i + numCol
        if (place != n) and sk[place] == sk[n]:
            return False
    #Check Box
    horBox= numCol//3;  verBox= numRow//3

    for i in range (3):
        for j in range(3):
            place = 9*(3*verBox + i) + (3*horBox + j)
            if (place != n) and sk[place] == sk[n]:
                return False
    return True

def sudoku_solve(sk):
    fixed = [i for i in range(len(sk)) if sk[i]!= "."]
   
    n = 0
    while n < len(sk):
        if n in fixed:
            n += 1
            continue
        else:
            while True:
                sk[n] += 1
                if sk[n] > 9:
                    sk[n] = 0
                    n -= 1
                    while n in fixed:
                        n -= 1
                    break
                else:
                    couldbe = Check(sk,n)
                    if couldbe:
                        n +=1
                        break
                    else: 
                        continue
            

            