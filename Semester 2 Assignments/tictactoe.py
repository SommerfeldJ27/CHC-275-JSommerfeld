board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Print the initial board
for row in board:
    for space in row:
        print(space, end=" ")
    print()

player1 = "X"
player2 = "O"
moves = 0

while moves < 9:
    row = int(input("Row (0-2): "))
    column = int(input("Column (0-2): "))

    if board[row][column] == player1 or board[row][column] == player2:
        print("That space is already taken. Try again.")
        continue  # ask again

    # Alternate between players based on move number
    if moves % 2 == 0:
        board[row][column] = player1
        current_player = player1
    else:
        board[row][column] = player2
        current_player = player2

    moves += 1

    # Print board after move
    for r in board:
        for s in r:
            print(s, end=" ")
        print()
    print()

    # Check for winner
    def winner(player):
        for i in range(3):
            # Row win
            if board[i][0] == board[i][1] == board[i][2] == player:
                return True
            # Column win
            if board[0][i] == board[1][i] == board[2][i] == player:
                return True
        # Diagonal win
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[0][2] == board[1][1] == board[2][0] == player:
            return True
        return False

    if winner(current_player):
        print(f"Player {current_player} wins!")
        break
else:
    print("Tie!")