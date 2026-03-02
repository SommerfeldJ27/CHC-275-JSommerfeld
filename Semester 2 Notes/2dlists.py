"""
2dlists.py

Let's talk about everything we know about lists 

What is a list (in terms of python)
    - A sequence of objects 
    - It's mutable 
    - We can store mixed data typees
    
A list is also an object? So theoretically we could store lists inside of lists. 

"""

grid = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

""" 
When we store a 2d-list, we can really think of it one of two things:
    1) a spreadsheet
    2) a 2d gameboard 
    
When we have a list of lists, each individual inside list is called a row, and each element of each inner list corresponds
to a column 

we can access individual elements by using mylist[index] in a regular list, for a 2dlist, it would be 

grid[row][col] 
"""


""" 
How do 2dlists expand? 
"""

box = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]



print(box[0][0]) #what do we expect to print? 
#we got the top left element 

""" 
In this order, 2dlists grow top to bottom, left to right, really what this means is as the first index grows, we are traversing
DOWN the rows, and as wwe increment the second index, we are a traverse to the RIGHT of each column

We don't have to always have to use both square brackets to get objects out of the list
"""

print(box[1]) #4,5,6, this prints the second row

""" 
Do we believe there is an easy way to pull a single column? The answer is really no, we probably need to do some sort of looping statement over
all of the rows, with a fixed column. 

So let's talk about iterating over a 2d list. 

three kinds of looping statements:
    1) for each loop = easiest to use, least amount of flexibility 
    2) for-i loop = moderate difficulty to use, good amount of flexibility
    3) while loop = most difficult to use, lots of flexibility in terms of stopping conditions/breaks/etc  
    
When we are going to do a looping statement over all of the numbers in a 2d list, how many for-each loops do you think we're going to need?

3? <- 
4? <- I don't think this is good either
1? <- might not be good 


grid[row][col]

we need 2 loops, an outer loop and an inner loop 

outer loop is for rows
inner loop is for every single number in a row 
"""



box = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#What is the data type of row? 
for row in box: 
    for num in row: #the data type of a row is a list
        num += 5 #is print 1-9 on individual lines

print(box)

""" 
nested for-each loops are also easy to use, but the nomenclature is a bit different. We are pulling rows, and then pulling numbers
from each row. 

For-i loops require a few things

1) a range of values 
2) I need a length to pass into range()
"""

box2 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

for i in range(len(box2)): #0,1,2
    for j in range(len(box2[0])): #0,1,2,3
        print(f"({i},{j}) = {box2[i][j]}",end = " ") #all this is doing is replacing the newline at the end of the print statement with " "
    print()
    
""" 
Nested for-i loops:

i = 0
    j = 0
        print
    j = 1
        print
    j = 2
        print
    j = 3 
        print
        
i = 1 
    j = 0
        print
    j = 1
        print
    j = 2
        print
    j = 3 
        print
        
nested for-i,j loops, i is frozen until the inner loop finishes.
"""


""" 
first semester: we worked with lists 
    - dynamically sized containers of values
    - pass by reference when passed as an argument of a function
    - we retrieve individual values by using the square bracket operator
    - indexed at 0 (we count from 0)
    
Last time we had this class we covered lists of lists (2d-lists)
    - The same thing as a regular list except the member values are lists themselves
    - we retrieve individual values with two square bracket operators grid[row][col]
    - we can retrieve individual rows by omitting the second set of brackets: grid[row]
    
    -nested for-each loops:
        -create shallow copies of all of the objects in the 2dlist
        -drill question 3: 
            - was it going to print every individual value or value + 5
    
    -nested for-i loops:
        -allows you to modify the lists directly 
        - drill question:
            - same numbers or numbers + 10

"""
"""#drill question 2
grid = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
print(grid[4][3]) #what was the thing that was supposed to print? 
#so therefore you should get an index out of bounds error """

""" 
So the lab that's coming up is connect 4, I'm going to show you how to implement tictactoe

1)picks a coordinate
2)replaces the empty space with their character
3)we need to check if someone won
    i)end if someone wins or there is a tie
4)we swap players and start from 1
"""
print("Starting TicTacToe")



current_player = "O" #in this version of tic tac toe O is the starting player
board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

#our board is a 3x3 grid where the empty space is 0
#we need a printboard function that doesn't look terrible

def printBoard(board):
    #we want each row printed on its own line
    #we need a nested for-each loop
    for row in board: 
        #pull out every row
        for space in row: 
        #pulls out space in every row
            print(space, end="") #replace end with an empty string so all of the spaces in a row print on the same line
        print() #empty print function just prints \n to the terminal

def placePiece(row,col,board,current_player):
    #remember that when we pass control to a function we leave the global scope and enter local scope so 
    #we can't access variables declared in global scope 
    if board[row][col] == 0:
        board[row][col]=current_player #is this sufficient in the logic of tictactoe?
        return True #returning true so the program knows that the piece was actually placed
    else: 
        return False 
    
    """ 
    if we add a true and false return statement at the end, then our program knows whether or not placePiece executed
    successfully 
    """
    
print()
printBoard(board)
placePiece(1,1,board,"O")
print()
printBoard(board)
placePiece(1,1,board,"X")
print()
printBoard(board)

def switchPlayer(current_player):
    #are strings pass by value?
    if current_player == "O":
         return "X"
    elif current_player == "X":
         return "O"
        

"""print(current_player) #currently O
current_player = switchPlayer(current_player)
print(current_player) #Should be X"""

def checkWinner(board,current_player):
    #Row Victories 
    #I think a for loop might be useful here, but I need direct access to the memory
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] == current_player:
           print(f"{current_player} wins")
           return True
    
    #Column Victories
    for i in range(len(board[0])):
        if board[0][i] == board[1][i] == board[2][i] == current_player:
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
    if board[0][0] == board[1][1] == board[2][2] == current_player:
            print(f"{current_player} wins")
            return True
        
    #right diagonal victories
    """ 
    000 [0][2] [1][1] [2][0]
    000
    000
    000
    """
    if board[0][2] == board[1][1] == board[2][0] == current_player:
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

""" 
1) Check for row: return True
2) check for col: return True
3) check for adiag: return True
4) check for an open space: return False

5) if 4) fails, then return True because we are implying there is a tie. 
"""
    
    

    
    
    
    
    
    
    
    
board1 = [
    ["O","O","O"],
    [0,0,0],
    [0,0,0]
]

board2 = [
    ["O",0,0],
    ["O",0,0],
    ["O",0,0]
]

board3 = [
    ["O",0,0],
    [0,"O",0],
    [0,0,"O"]
]

checkWinner(board1,"O")
checkWinner(board2,"O")
checkWinner(board3,"O")