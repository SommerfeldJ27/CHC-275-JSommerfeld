def loadBoard(filename):
    file = open(filename, "r")
    buffer = file.readlines()
    board = []
    for line in buffer:
        row = []
        line = line.strip()
        board.append(row)
        for character in line:
            row.append(character)
    file.close()
    return board


def switchPlayer(current_player):
    if current_player == 'w':
        current_player = 'b'
    elif current_player == 'b':
        current_player = 'w'
    return current_player


def find_inside(board,x,y,player):
    #Base Case: bottom right
    if x == len(board)-1 and y == len(board[0])-1:
        return True
    try:
        if board[x][y] == "B":
            player = "B"
        if board[x][y] == "W":
            player = "W"
        if board[x][y] == board[x][y+1] == board [x + 1][y] == player and board[x+1][y+1] == '.':
            floodfill(board,x+1,y+1,player)
            return True
        if board[x][y] == board [x][y + 1] == board[x+1][y-1] == player and board[x+1][y] == '.':
            floodfill(board,x+1,y,player)
            return True
    finally:
        if y < len(board[0])-2:    
            find_inside(board,x,y+1,player)
        if x < len(board)-2:
            find_inside(board,x+1,y,player)
        

def floodfill(matrix, x, y, color):
    if matrix[x][y] == ".":  
        matrix[x][y] = color 
        #recursively invoke flood fill on all surrounding cells:
        if x > 0:
            floodfill(matrix,x-1,y,color)
        if x < len(matrix[x]) - 1:
            floodfill(matrix,x+1,y,color)
        if y > 0:
            floodfill(matrix,x,y-1,color)
        if y < len(matrix) - 1:
            floodfill(matrix,x,y+1,color)


def countScore(board):
    black_score = 0
    white_score = 0
    
    for i in range(len(board)):
        for j in range(len(board[0])): 
            if board[i][j] == "B":
                black_score = black_score + 1
            if board[i][j] == "W":
                white_score = white_score + 1
    
    return black_score, white_score


def printBoard(board):
    for row in board: 
        for space in row: 
            print(space, end=" ")
        print()


def main():
    board = loadBoard("go_board.txt")
    printBoard(board)
    find_inside(board,0,0,"B")
    print()
    printBoard(board)
    scores = countScore(board)

    if scores[0] > scores[1]:
        print("Black Wins")
    if scores[0] < scores[1]:
        print ("White Wins")
    if scores[0] == scores[1]:
        print("Its a Tie")


if __name__ == "__main__":
    main()