"""
Name:
Section:
Description: Template for Lab 6
"""

"""
Scenario: We are to build a connect 4 game that runs in the terminal
"""

def drawBoard(board):
    for row in board: 
        for space in row: 
            print(space, end=" ")
        print()
 

def switchPlayer(player):  
    if player == "O":
         return "X"
    elif player == "X":
         return "O"

    
def dropPiece(board,player,col):
    if board[0][col] != 0:
        return False
    i = 0
    while i < len(board):
        curr = board[i][col]

        if curr == 0:
            i = i+1
        else:
            board[i-1][col] = player
            return True
    board[i-1][col] = player
    return True

    
    
def checkWinner(board,player):
    # Row Victories 
    for i in range(len(board)):
        for j in range(len(board[0])-3):
            if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == player:
                print(f"{player} wins")
                return True
    
    # Column Victories
    for i in range(len(board)-3):
        for j in range(len(board)):
            if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == player:
                print(f"{player} wins")
                return True
        
    # Left Diagonal Victories
    for i in range(len(board)-3):
        for j in range(len(board[0])-3):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == player:
                print(f"{player} wins")
                return True
        
    # Right diagonal victories
    for i in range(len(board)-3):
        for j in range(len(board[0])-3):
            if board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3] == player:
                print(f"{player} wins")
                return True

    return False

    

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
    while checkWinner(BOARD,CURRENT_PLAYER) == False:
        drawBoard(BOARD)
        column = int(input("Please Enter The Column You Would Like to Use: "))
        dropPiece(BOARD, CURRENT_PLAYER, column)
        if checkWinner(BOARD,CURRENT_PLAYER) == True:
            break
        CURRENT_PLAYER = switchPlayer(CURRENT_PLAYER)
    
if __name__ == "__main__":
    main()