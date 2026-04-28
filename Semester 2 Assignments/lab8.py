def loadBoard(filename):
    pass

        
def switchPlayer(current_player):
    if current_player == "W":
         return "B"
    elif current_player == "B":
         return "W"

def find_inside(board):
       pass



    
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
    pass

def printBoard(board):
    for row in board: 
        for space in row: 
            print(space, end=" ")
        print()

def main():
   pass
    
if __name__ == "__main__":
    main()
