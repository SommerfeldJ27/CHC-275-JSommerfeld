"""
Name:
Section:
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
    for row in range(len(board)-1, -1, -1):
        if board[row][column] == 0:
            board[row][column] = player
            return True
        else:
            return False

    
    
def checkWinner(board,player):
    #Row Victories 
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] == board[i][3] == player:
           print(f"{player} wins")
           return True
    
    #Column Victories
    for i in range(len(board[0])):
        if board[0][i] == board[1][i] == board[2][i] == board[3][i] == player:
            print(f"{player} wins")
            return True
        
    #Left Diagonal Victories
    if board[0][0] == board[1][1] == board[2][2] == board[3][3] == player:
            print(f"{player} wins")
            return True
        
    #Right diagonal victories
    if board[0][3] == board[1][2] == board[2][1] == board[3][0] == player:
        print(f"{player} wins")
        return True
    

def main():
    ROWS = 6
    COLUMNS = 7
    BOARD = [ 
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],        
    ]

    CURRENT_PLAYER = "X"
    #what switch player does is checks to see if current player = x
    #if it is, return O
    #if its not, return X 
    CURRENT_PLAYER = switchPlayer()
    
if __name__ == "__main__":
    main()