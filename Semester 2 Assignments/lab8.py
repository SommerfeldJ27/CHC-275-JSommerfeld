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


def find_inside(board):
    territories = []
    board_copy = [row[:] for row in board]
    for i in range(len(board_copy)):
        for j in range(len(board_copy[i])):
            if board_copy[i][j] == '.':
                region_cells = []
                floodfill(board_copy, i, j, 't', region_cells)

                area_size = 0
                border_colors = set()
                for x, y in region_cells:
                    area_size += 1
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < len(board_copy) and 0 <= ny < len(board_copy[nx]):
                            if board_copy[nx][ny] in ['w', 'b', 'W', 'B']:
                                border_colors.add(board_copy[nx][ny])
                        else:
                            border_colors.add('edge')

                if len(border_colors) == 1 and 'edge' not in border_colors:
                    territories.append((region_cells, area_size, border_colors.pop()))

                for x, y in region_cells:
                    board_copy[x][y] = 'v'
    return territories
        

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


def countScore(board, black_score, white_score):
    black_score = 0
    white_score = 0
    
    # Count stones
    for row in board:
        for cell in row:
            if cell == "B":
                black_score += 1
            elif cell == "W":
                white_score += 1
    
    return black_score, white_score

def printBoard(board):
    for row in board:
        line = ""
        for cell in row:
            line += cell + " "
        print(line)


# WORK
def main():
    curr_player = 'w'
    ques1 = input("Would you like to score an exisiting file? (y/n): ").strip().lower()
    if ques1 == 'y':
        input1 = input("What file would you like to load? (only the name not the .txt): ").strip()
        board = loadBoard(input1)
        printBoard(board)
        w_score, b_score = countScore(board)
        print(f"White Score: {w_score}")
        print(f"Black score: {b_score}")
        if w_score > b_score:
            print("White wins!")
        elif b_score > w_score:
            print("Black wins!")
        elif w_score == b_score:
            print("It's a tie!")
    
if __name__ == "__main__":
    main()