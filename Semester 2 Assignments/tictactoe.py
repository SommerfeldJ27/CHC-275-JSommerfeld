board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def print_board():
    print()
    for row in board:
        for cell in row:
            if cell == 0:
                print(".", end=" ")
            else:
                print(cell, end=" ")
        print()
    print()

def check_winner(player):
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


current_player = "X"
turns = 0

while turns < 9:
    print_board()

    row = int(input("Row (0-2): "))
    col = int(input("Col (0-2): "))

    if board[row][col] == 0:
        board[row][col] = current_player
        turns += 1

        if check_winner(current_player):
            print_board()
            print("Player", current_player, "wins!")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
    else:
        print("Spot taken!")

if turns == 9:
    print_board()
    print("It's a tie!")