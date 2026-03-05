""" 
Connect4.py
"""

def checkWinner(board,current_player):
    #Row Victories 
    for i in range(len(board)):
        for j in range(len(board[0])-3):
            if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == current_player:
                print(f"{current_player} wins")
                return True
    
    #Column Victories
    for i in range(len(board)-3):
        for j in range(len(board[0])):
            if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == current_player:
                print(f"{current_player} wins")
                return True

    #Left Diagonal Victories
    for i in range(len(board)-3):
        for j in range(len(board[0])-3):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == current_player:
                print(f"{current_player} wins")
                return True
        
    #Right Diagonal Victories
    for i in range(len(board)-3):
        for j in range(len(board[0])-3):
            if board[i][j] == board[i+1][j-1] == board[i+2][j-1] == board[i+3][j-3] == current_player:
                print(f"{current_player} wins")
                return True
    
    #Ties
    for row in board:
        for space in row:
            if space == 0:
                return False
    return True

def printBoard(board):
    for row in board: 
        for space in row: 
            print(space, end=" ")
        print()

def placePiece(col,board,current_player):
    if board[0][col] != 0:
        return False
    i = 0
    while i < len(board):
        curr = board[i][col]
        if curr == 0:
            i = i+1
        else:
            board[i-1][col] = current_player
            return True
    board[i-1][col] = current_player
    return True
    
def switchPlayer(current_player):
    if current_player == "O":
         return "X"
    elif current_player == "X":
         return "O"
        
def main():
    curr = "X"
    board = [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
    ]
    check = False
    while check != True:
        printBoard(board)
        y = int(input("Enter Col: ").strip())
        placePiece(y,board,curr)
        if checkWinner(board,curr):
            printBoard(board)
            check = True
        curr = switchPlayer(curr)

if __name__ == "__main__":
    main()