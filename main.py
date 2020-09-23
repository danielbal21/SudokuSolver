def isValid(board, x, y):
    for i in range(9):     #row check
        if i != x:
            if board[y][i] == board[y][x]:
                return False
    for i in range(9):     #column check
        if i != y:
            if board[i][x] == board[y][x]:
                return False
    boxSizeX = int(x/3)
    boxSizeY = int(y/3)
    for j in range(boxSizeY*3, (boxSizeY*3)+2, 1):
        for i in range(boxSizeX*3, (boxSizeX*3)+2, 1):
            if x != i and y != j:
                if board[j][i] == board[y][x]:
                    return False
    return True


def solveSudoku(board, x, y):
    while board[y][x] != 0:
        if x < 8:
            x += 1
        else:
            if y < 8:
                x = 0
                y += 1
            else:
                return True
    for n in range(1, 10):
        board[y][x] = n
        if isValid(board, x, y):
            if solveSudoku(board, x, y): return True
    board[y][x] = 0
    return False


sudokuBoard = [ [0, 0, 0, 0, 8, 0, 0, 1, 3],
                [0, 0, 0, 0, 3, 2, 9, 5, 0],
                [9, 8, 3, 0, 0, 0, 7, 2, 6],
                [8, 5, 0, 2, 0, 1, 3, 4, 7],
                [0, 0, 0, 5, 9, 8, 1, 0, 0],
                [0, 0, 6, 0, 0, 4, 0, 0, 5],
                [4, 3, 1, 7, 0, 6, 5, 8, 9],
                [0, 9, 0, 0, 1, 0, 6, 0, 4],
                [0, 7, 8, 4, 0, 0, 0, 0, 1]
                ]
solveSudoku(sudokuBoard, 0, 0)
for l in range(9):
    print(sudokuBoard[l])