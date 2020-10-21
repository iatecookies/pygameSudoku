import random
import time

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]



def solve(board):
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



def mutate(board):
    # Swap Rows
    random.seed(time.time())
    row1 = random.randint(0, len(board[0]) - 1)
    row2 = random.randint(0, len(board[0]) - 1)
    output = f"row is {row1} and row2 is {row2}"
    #print (output)

    for i in range(len(board[0])):
        temp = board[row1][i]
        board[row1][i] = board[row2][i]
        board[row2][i] = temp

    # Swap cols
    random.seed(time.time())
    col1 = random.randint(0, len(board) - 1)
    col2 = random.randint(0, len(board) - 1)
    output = f"col is {col1} and col2 is {col2}"
    #print (output)

    for i in range(len(board)):
        temp = board[i][col1]
        board[i][col1] = board[i][col2]
        board[i][col2] = temp




def generatePuzzle(board):
    random.seed(time.time())
    row = random.randint(0, len(board[0]) - 1)
    col = random.randint(0, len(board) - 1)
    num = random.randint(1, 9)
    output = f"row is {row}, column is {col} and random number is {num}"
    print (output)

    # makes a 'random' puzzle
    board[row][col] = num
    solve(board)



    print("First board")
    printBoard(board)

    mutateTimes = 1000
    while mutateTimes > 0:
        mutate(board)
        mutateTimes = mutateTimes - 1

    print("Mutated board")
    printBoard(board)

    # Fill it with Empty Zeroes
    emptyCubes = random.randint(20, 40)
    while emptyCubes > 0:
        random.seed(time.time())
        row1 = random.randint(0, len(board[0]) - 1)
        col1 = random.randint(0, len(board) - 1)
        if board[row1][col1] != 0:
            board [row1][col1] = 0
            emptyCubes = emptyCubes - 1


    print("Empty board")
    printBoard(board)

    
generatePuzzle(board)


print("######################################################")
solve(board)
printBoard(board)
