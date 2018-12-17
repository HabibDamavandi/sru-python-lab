import numpy as np

def checkBoard(board, row):
    if np.count_nonzero(board == board[row])>1:
        return False
    for i in range(row):
        if abs(board[i]-board[row])==abs(row-i):
            return False
    return True
    
def printBoard(board):
    for i in range(8):
        print(". "*(board[i])+"X "+". "*(7-board[i]))
    


board = np.ones(8,dtype=int)*-1
case = 0
row = 0

while row >= 0:
    board[row] += 1
    if board[row]>7:
        board[row]=-1
        row -= 1
        continue    
    if checkBoard(board, row):
        if row == 7:
            printBoard(board)
            case += 1
            print("Case:", case)
            input()
        else:
            row += 1
