board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for row in board:
    for space in row:
        print(space, end = " ")
    print()

row = int(input("Row (0-2): "))
column = int(input("Column (0-2): "))

player1 = "X"
player2 = "O"
moves = 0

if board[row][column] == player1 or board[row][column] == player2:
    print("That space is already taken. Try again.")

if moves < 9:
    # print board
    for row in board:
        print(row)
    print()
elif moves == 9:
    print("Tie!")

def winner(player1):
    for i in range(len(board[0])):
#Collum Win
        if board[i][0] == board[i][1] == board[i][2] == player1:
            return
#Row Win
        if board[0][i] == board[1][i] == board[2][i] == player1:
            return
#Diagonal Win       
        if board[0][0] == board[1][1] == board[2][2] == player1:
            return
        if board[0][2] == board[1][1] == board[2][0] == player1:
            return
    print(f"Player {player1} wins")
    
def winner(player2):
    for i in range(len(board[0])):
#Collum Win
        if board[i][0] == board[i][1] == board[i][2] == player2:
            return
#Row Win
        if board[0][i] == board[1][i] == board[2][i] == player2:
            return
#Diagonal Win       
        if board[0][0] == board[1][1] == board[2][2] == player2:
            return
        if board[0][2] == board[1][1] == board[2][0] == player2:
            return
    print(f"Player {player2} wins")