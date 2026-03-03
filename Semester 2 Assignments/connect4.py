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

def drawBoard(board):
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
    if board[column] == 0:
        board[column] = player
        return True
    else:
        return False
    
def checkWinner(board,player):
    # Row Victories 
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == player:
                print(f"{player} wins")
                return True
    
    # Column Victories
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == player:
                print(f"{player} wins")
                return True
        
    # Left Diagonal Victories
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == player:
                print(f"{player} wins")
                return True
        
    # Right diagonal victories
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3] == player:
                print(f"{player} wins")
                return True

    return False
    
def main():
    drawBoard(board)
    print(board)
    while True:
        column = int(input(f"{player}, enter the column you would like to drop your piece in: "))
        if dropPiece(board,player,column):
            drawBoard(board)
            if checkWinner(board,player):
                break
            player = switchPlayer(player)
        else:
            print("That column is full, try again")
    if __name__ == "__main__":
        main()