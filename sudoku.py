# This code solves a 9x9 sudoku game given.

sudoku43 = [1,0,8, 4,0,0, 6,0,5,
            0,2,0, 9,0,0, 0,0,0,
            0,0,0, 2,5,0, 0,0,7,
            0,5,0, 0,1,0, 0,0,0,
            7,0,0, 0,0,0, 0,0,3,
            0,0,0, 0,2,0, 0,6,0,
            3,0,0, 0,7,2, 0,0,0,
            0,0,0, 0,0,5, 0,8,0,
            6,0,2, 0,0,4, 7,0,1]

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
    fixed = []
    for i in range(len(sk)):
        if sk[i] > 0:
            fixed.append(i)
    
    n = 0
    while n < len(sk):
        numRow= n//9
        numCol= n%9
        if n in fixed:
            n += 1
            continue
        else:
            while True:
                sk[n] += 1
                if sk[n] == 9:
                    n -= 1
                    break
                else:
                    couldbe = Check(sk,n)
                    if couldbe:
                        n +=1
                        break
                    else: 
                        continue
            

sudoku_solve(sudoku43)
print(sudoku43)
            