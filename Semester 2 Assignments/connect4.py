""" 
Connect4.py
"""

def checkWinner(board,current_player):
    #Row Victories 
    #I think a for loop might be useful here, but I need direct access to the memory
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
    #Diagonal Victories
    #left diagonal 
    
    """
    [0][0] [1][1] [2][2] 
    000
    000
    000
    """
    for i in range(len(board)-3):
        for j in range(len(board[0])-3):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == current_player:
                print(f"{current_player} wins")
                return True
        
    #right diagonal victories
    """ 
    000 [0][2] [1][1] [2][0]
    000
    000
    000
    """
    for i in range(len(board)-3):
        for j in range(len(board[0])-3):
            if board[i][j] == board[i+1][j-1] == board[i+2][j-1] == board[i+3][j-3] == current_player:
                print(f"{current_player} wins")
                return True
    
    #Ties
    #What constitutes a tie? No empty spaces left
    #so this is the last piece of code that is executed before the function call ends. So if there's no row,col,diag, there needs to be a check for a tie
    #and if there's no tie, they need to continue playing 
    #The ONLY reason why we return a value at all is to signal to the game that we have finished playing. 
    #If there is a tie, you should return True. If all else fails, game continues -> returninng false
    for row in board:
        for space in row:
            if space == 0: #<= is this checking if this is the empty space? 
                return False

    #if the for-loop finishes, that implies there is a tiue
    return True #this flags for the game to end


def printBoard(board):
    #we want each row printed on its own line
    #we need a nested for-each loop
    for row in board: 
        #pull out every row
        for space in row: 
        #pulls out space in every row
            print(space, end=" ") #replace end with an empty string so all of the spaces in a row print on the same line
        print() #empty print function just prints \n to the terminal

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
    #are strings pass by value?
    if current_player == "O":
         return "X"
    elif current_player == "X":
         return "O"
        
def main():
    #we just need to implement the main function
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
            check = True
        curr = switchPlayer(curr)
        
    


if __name__ == "__main__":
    main()