from random import randint
import time

def animate(board):
    tempboard = [0] * board.BOARDSIZE
    for y in range (0, board.BOARDSIZE):
        tempboard[y] = [0] * board.BOARDSIZE
    newcell = -1
    for y in range (0, board.BOARDSIZE):
        for x in range (0, board.BOARDSIZE):
            cell = board.board[y][x]
            neighbors = count_neighbors(board, y, x)
            if cell == 1 and neighbors < 2:
                newcell = 0
            elif cell == 1 and (2 <= neighbors <= 3):
                newcell = 1
            elif cell == 1 and neighbors > 3:
                newcell = 0
            elif cell == 0 and neighbors == 3:
                newcell = 1
            else:
                newcell = cell
            tempboard[y][x] = newcell
    time.sleep(2)
    board.board = tempboard
    return board


def count_neighbors(board, y, x):
    count = 0;
    for j in range (y - 1, y + 2):
        for i in range (x - 1, x + 2):
            if ((0 <= j < board.BOARDSIZE) and (0 <= i < board.BOARDSIZE)):
                if ((j != y) or (i != x)):
                    if board.board[j][i] == 1:
                        count += 1
    return(count)



def roll_spot():
    value = randint(0, 99)
    if value <= 30:
        return 1
    else:
        return 0