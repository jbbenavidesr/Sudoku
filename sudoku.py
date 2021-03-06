# This code solves a 9x9 sudoku game given.
import pygame

class Sudoku:

    def __init__(self, screen, font):
        # Al inicializar esto, debe escoger uno al azar, resolverlo y dibujarlo.
        self.puzzle= self.sudokuArray(self.select())
        self.screen = screen
        self.font = font
        self.corners = [100, 50, 400, 350] #[x1, y1, x2, y2]
        self.x_div = (self.corners[2]-self.corners[0])/9
        self.y_div = (self.corners[3]-self.corners[1])/9
        #self.solved = self.sudoku_solve(self.sudokuArray(self.puzzle))

    def select(self):
        # For de moment I'll just use this one as a trail.
        return "...21...5..2.46..1........9......95.4....7..6....85...9.1..2.84..8.7.1..2.6...7.."

    def draw(self, color):
        # draw the sudoku grid
        # Draw the lines
        for i in range(10):
            if i%3 == 0:
                gross = 4
            else:
                gross = 1
            x= self.corners[0] + i * self.x_div
            y= self.corners[1] + i * self.y_div
            # Vertical line
            pygame.draw.line(self.screen, color, (x , self.corners[1]), (x, self.corners[3]), gross) 
            # Horizontal line
            pygame.draw.line(self.screen, color, (self.corners[0], y), (self.corners[2], y), gross)
        self.printNumbers(color)

    def printNumbers(self, color):
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
            y1= self.corners[1] + i*self.y_div; y2= y1 + self.y_div
            for j in range(9):
                x1= self.corners[0] + j*self.x_div; x2= x1 + self.x_div
                sq_coord[i][j]= (0.5*(x1 + x2), 0.5*(y1 + y2))

        # Write the number
        for i in range(9):
            for j in range(9):
                # set up the text
                place= i*9 + j
                if self.puzzle[place] != 0:
                    text = self.font.render(str(self.puzzle[place]), True, color, (255,255,255))
                    textRect = text.get_rect()
                    textRect.centery = sq_coord[i][j][1]
                    textRect.centerx = sq_coord[i][j][0]

                    self.screen.blit(text, textRect)


    def sudokuArray(self, sk):
        sudoku = []
        for i in sk: 
            if i == ".":
                sudoku.append(0)
            else: 
                sudoku.append(int(i))
        return sudoku


    def Check(self, sk, n):
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

    def sudoku_solve(self, sk):
        fixed = [i for i in range(len(sk)) if sk[i]!= 0]
   
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
                        couldbe = self.Check(sk,n)
                        if couldbe:
                            n +=1
                            break
                        else: 
                            continue
            

            