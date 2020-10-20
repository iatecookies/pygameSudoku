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

def print_board(board):
    # Row of board
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
        # Column of board
        for j in range(len(board[0])):
            # on every third number you will print |
            # print ( , end="") means you can on printin in same line
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            # on the last column of the row Board[i][8]. It will print new line
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

print_board(board)
