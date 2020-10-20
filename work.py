board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
""""
board = [
    [0, 8, 0, 4, 0, 0, 1, 2, 0],
    [0, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [0, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 0, 0, 3, 0, 0, 0, 1, 2],
    [0, 0, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
""""
def solve(board):
    print(board)
    find = findEmpty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if isValid(board, i, (row, col)):
            board[row][col] = i # add into the board
            # recursively try finish solution
            # if we cant solve board then we reset that value

            if solve(board):
                return True
            # Backtracks if the above if doesnt return True
            board[row][col] = 0

    return False

def isValid (board, num, pos):

    # For each row check columns
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # For each columns check the rows
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    xBox = pos[1] // 3
    yBox = pos[0] // 3

    for i in range(yBox*3, yBox*3 + 3):
        for j in range(xBox * 3, xBox*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True


def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, col
    return None

def printBoard(board):
    # Row of board, Length of Board is a list
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
        # Column of board, Length of each row
        for j in range(len(board[0])):
            # on every third number you will print |
            # print ( , end="") means you can on printin in same line
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            # on the last column of the row Board[i][8]. It will print new line
            if j == 8:
                print(board[i][j], end= "\n")
            else:
                print(str(board[i][j]) + " ", end="")

printBoard(board)
solve(board)
print("###########################################")
printBoard(board)
