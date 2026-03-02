
current_player = "O"
board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

def printBoard(board):
    for row in board: 
        for space in row: 
            print(space, end="")
        print()

def placePiece(row,col,board,current_player):

    if board[row][col] == 0:
        board[row][col]=current_player
        return True
    else: 
        return False 
    
print()
printBoard(board)
placePiece(1,1,board,"O")
print()
printBoard(board)
placePiece(1,1,board,"X")
print()
printBoard(board)

def switchPlayer(current_player):
    if current_player == "O":
         return "X"
    elif current_player == "X":
         return "O"
        

def checkWinner(board,current_player):
    #Row Victories 
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] == current_player:
           print(f"{current_player} wins")
           return True
    
    #Column Victories
    for i in range(len(board[0])):
        if board[0][i] == board[1][i] == board[2][i] == current_player:
            print(f"{current_player} wins")
            return True
        
    #Left Diagonal Victories
    if board[0][0] == board[1][1] == board[2][2] == current_player:
            print(f"{current_player} wins")
            return True
        
    #Right diagonal victories
    if board[0][2] == board[1][1] == board[2][0] == current_player:
        print(f"{current_player} wins")
        return True
    
    #Check for tie
    for row in board:
        for space in row:
            if space == 0:
                return False

    return True