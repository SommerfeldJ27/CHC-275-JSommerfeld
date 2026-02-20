board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def check_winner(p):
    for i in range(3):
        # rows
        if board[i][0] == board[i][1] == board[i][2] == p:
            return True
        # columns
        if board[0][i] == board[1][i] == board[2][i] == p:
            return True

    # diagonals
    if board[0][0] == board[1][1] == board[2][2] == p:
        return True
    if board[0][2] == board[1][1] == board[2][0] == p:
        return True

    return False


player = "X"
moves = 0

while moves < 9:
    # print board
    for row in board:
        print(row)
    print()

    r = int(input("Row (0-2): "))
    c = int(input("Column (0-2): "))

    if board[r][c] == 0:
        board[r][c] = player
        moves += 1

        if check_winner(player):
            for row in board:
                print(row)
            print("Player", player, "wins!")
            break

        player = "O" if player == "X" else "X"
    else:
        print("Taken!")

if moves == 9:
    print("Tie!")