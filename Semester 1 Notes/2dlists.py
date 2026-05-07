"""
2DLists.py

In the first semester we only really dealt with one data structure: A kind of storage procedure that 
stores a bunch of variables under one name 
    - List
    
In the second semester we are going to work with two new data structures
    - 2D List
    - Dictionary 
    
Recall things about 1D Lists:
    - Mutable (they can change in length)
    - Yes 
    - How do we get single elements out of a list? square brackets
    mylist[i] <- i is an index 
    - what is the starting index of a list: 0
    - .append(val) <=adds things
    - .remove(val)
    - .pop(index)
    
2D lists are practically the same thing with one change: rather than storing individual values
inside the list, we are just storing lists inside of those lists. 
    
"""

grid = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]

""" 
Now instead of one list containing a bunch of numbers, I have a single list, containing multiple lists
inside of it. This is a natural thing to consider 
    - Spreadsheets are laid out in this way
    - 2D games are laid out in this way 
    
to get a single value out of a 2D list
"""

print(grid[0][0]) #pulling stuff out of a 2Dlist is the same thing as pulling something out a 1D list

""" 
the syntax is grid[row][col]
"""

grid2 = [
   [1,2,3],
   [4,5,6],
   [7,8,9]
]

print(grid2[1][2]) #prints 9

"""
 The way 2D lists grow is from:
 
    -top to bottom, then left to right.
    
Different than a regular coordinate plane because [0][0] is really the "origin". 

for-each loop
for-i loop
while loop

In terms of traversing a 1D list:
    1) for-each loop: easiest to use, the trade off was num is a going to be copies of the elements
    of the list, so we can't directly modify the list
    2) for-i loops: not as easy to use, but we can directly access the list so we have more flexibility
    3) while loops: have the most flexibility because our exit condition doesn't strictly involve the list
    but it's up to you to figure out what the exit conditions are. 
"""

"""nums = [1,2,3,4]

for num in nums: #this is a for each loop
    num = num + 2
print(nums) #still prints 1,2,3,4

for i in range(len(nums)): #this is a for-i loop
    nums[i] = nums[i] + 1
    
print(nums)

i = 0
while i < len(nums): #while loop
    i = i + 1
    pass"""
    
""" 
How many looping statements do we think we need fort a 2D list? 
    3? 
    2? = the justification for 2 is an outer loop that traverses the rows and an inner loop that traverses the columns
"""

for row in grid2: #this grabs every row in the grid
    for num in row: #this pulls out the numbers in an individual row
        print(num)
    
""" 
For-each loops are the most natural again. But it's not clear what exactly is happening under the hood. I need two counting variables

i,j
"""

for i in range(len(grid2)): #this is the amount of rows from 0-2
    for j in range(len(grid2[0])): #pull out any single row, in this case it doesn't matter because every row is the same 
        #size
        print(f"({i},{j}) = {grid2[i][j]}", end = " ") 
        #print statements are terminated by a \n <- which stands for new line. print also a second parameter called end which
        #just replaces the \n  
    print()
    
""" 
For nested loops, 
    i = 0,
        j = 0
        print
        j = 1
        print
        j = 2
    i = 1,
        j = 0
        print
        j = 1
        print
        j = 2
"""



""" 
we're going to implement tic-tac-toe over the next couple classes 

a printBoard(board) function
a placeMarker(board,player)
a checkWinner(board) 
"""




board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

current_player = "O"

def printBoard(board):
    """
    prints out a tictactoe board in a nice way
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            print("|",end = "")
            print(board[i][j], end = "|")
        print() #prints \n
    
printBoard(board)


"""
1. print the board
2. ask the current player to place their piece
3. check to see if someone won
4. switch the player and do it again  
"""

def placePiece(board,current_player,row,col):
               #board, either X or O, Y, X
    """ 
    So when I'm placing a piece on the board, I'm really doing variable assignment on a single element inside our 2D list. 
    Remember: Passing a list as an argument is pass by reference, so we don't need to return any values because when we update
    the board, we are directly modifying the memory. 
    """
    if board[row][col] == 0:
        board[row][col] = current_player #it replaces the (x,y) coordinate inside our board with the current_player's marker
        #there is a problem with our current implementation: We don't check if the (x,y) coordinate is an open square
    else:
        print("That is not a valid square")

def switchPlayer(current_player):
    """ 
    All this does is switch the character from "O" to "X" and "X" to "O"
    
    What datatype is current_player? its a string. strings are immutable in python. 
    
    immutability implies what when its passed in as an argument? 
        1) pass by reference
        2) pass by value
    
    since its by value we need to return something. It's not enough to just set current_player
    to X or O because we don't know which state its in 
    """
    if current_player == "O":
        #this is the swap
        return "X"
    elif current_player == "X":
        return "O"
     
""" 
The last part of our process is to check to see if someone won. 

1) How many ways can you win in tictactoe 
    a) Row Victory
    b) Diagonal Victory
    c) Column 
2) When you're playing tictactoe, can your opponent win off your turn? 
    a) no 
    
1st question: informs us that we have three conditions to check
2nd question: informs us that we don't need to check both players 
"""

def checkWinner(board,current_player):
    #Row Victories
    for i in range(len(board)): #gets all of the rows
        if board[i][0] == current_player and board[i][1] == current_player and board[i][2] == current_player:
            print(f"{current_player} wins!")
            return True
    
    """ 
    [
        [x,x,x] (0,0) (0,1) (0,2)
        [0,0,0] 
        [0,0,0]
    ]
    """
    
    #Column Victories
    """
    there's a problem with columns in 2d lists. Retrieving entire columns is not a natural operation. 
    Inside of a row: every value in a row is contained inside of a single list.
    Inside of a column: EACH value is stored in a DIFFERENT list
    """
    for j in range(len(board[0])):
        if board[0][j] == current_player and board[1][j] == current_player and board[2][j] == current_player:
            print(f"{current_player} wins!")
            return True
    
    
    #Diagonal Victories
    """ 
    2 Ways, left diagonal or a right diagonal
    Left Diagonal
    [X,0,0] (0,0)
    [0,X,0] (1,1)
    [0,0,X] (2,2)
    
    Right Diagonal
    [0,0,X] (0,2)
    [0,X,0] (1,1)
    [x,0,0] (2,0)
    """
    
    #Left Diagonal First
    if board[0][0] == board[1][1] == board[2][2] == current_player:
        print(f"{current_player} wins!")
        return True #when we want to exit the while loop of the actual game, we need some sort of flag variable 
    
    #Right Diagonal
    if board[0][2] == board[1][1] == board[2][0] == current_player:
        print(f"{current_player} wins!")
        return True #when we want to exit the while loop of the actual game, we need some sort of flag variable         
    
    """ 
    There could be ties in tictactoe:
    
    What determines whether there is a tie? 
    
    A tie occurs when there are no more empty spaces (no more 0s) <= checking for a lack of zeros is hard
    
    What is a logically equivalent statement to "no more zeros?" 
    
    Checking for AT LEAST one zero is an equivalent task but easier to code. 
    
    What kind of looping statement should we use?
        1) for each
        2) for-i,j 
        
    1) we aren't changing anything about the board
    2) Knowing the current value's index doesn't really affect anything. 

    
    3) If there's a tie, what value do we want to return (True or False)? True
    4) If we find a zero, what do we return? False
    """
    for row in board:
        for space in row:
            if space == 0:
                return False #the return statement not only flags the interpreter to remember a value, they also do one other thing
                #return also terminates the function call 
    
    return True




test_board1 = [
    ["O","O","O"],
    [0,0,0],
    [0,0,0]
]
print()
printBoard(test_board1)
checkWinner(test_board1,"O")

test_board2 = [
    [0,"X",0],
    [0,"X",0],
    [0,"X",0]
]
print()
printBoard(test_board2)
checkWinner(test_board2,"X")


""" 
Q1. 

grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(grid[1][1]) = 5


Q2. 

grid = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

print(grid[4][3]) = error, index out of bounds error 

Q3. 

grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in grid:
    for num in row:
        num += 10
        
print(grid) = Stay the same because for-each loops make copies

Q4. 

grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        grid[i][j] += 5
        
print(grid) = adds 5 to every number because for-i,j loops directly modify the memory 

Q5. 

grid = [
    ["O","O","O"],
    [0,0,0],
    [0,0,0]
]

if grid[0][0] == grid[1][0] == grid[2][0] == "O": #this is a column victory
    print True
else:
    print Flase
    
    
Q6. 

grid = [
    ["O","O","O"],
    [0,0,0],
    [0,0,0]
]

if grid[0][0] == grid[0][1] == grid[0][2] == "O": #this is a row victory
    print True
else:
    print Flase


"""