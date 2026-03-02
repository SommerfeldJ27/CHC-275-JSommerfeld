"""
Name: Jackson Sommerfeld
Section: 275-2
Description: Template for Lab 6
"""

"""
Scenario: We are to build a connect 4 game that runs in the terminal
"""

player = "O"
board = [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
]

def printBoard(board):
    for row in board: 
        for space in row: 
            print(space, end="")
        print()

def switchPlayer(player):
    if player == "O":
         return "X"
    elif player == "X":
         return "O"

def dropPiece(board,player,column):
    for row in range(len(board)-1, -1, -1):
        if board[row][column] == 0:
            board[row][column] = player
            return True
    return False
    
def checkWinner(board,player):

    # Row Victories 
    for i in range(len(board)):
        for j in range(len(board[0]) - 3):
            if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == player:
                print(f"{player} wins")
                return True
    
    # Column Victories
    for i in range(len(board) - 3):
        for j in range(len(board[0])):
            if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == player:
                print(f"{player} wins")
                return True
        
    # Left Diagonal Victories
    for i in range(len(board) - 3):
        for j in range(len(board[0]) - 3):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == player:
                print(f"{player} wins")
                return True
        
    # Right diagonal victories
    for i in range(len(board) - 3):
        for j in range(3, len(board[0])):
            if board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3] == player:
                print(f"{player} wins")
                return True

    return False
    
def main():
    player = "O"
    check = False

    while check == False:
        printBoard(board)
        column = int(input("Choose a column (0-6): "))
        if dropPiece(board, player, column) == True:
            if checkWinner(board, player) == True:
                printBoard(board)
                check = True
            else:
                player = switchPlayer(player)
        else:
            print("Column is full. Try again.")

if __name__ == "__main__":
    main()