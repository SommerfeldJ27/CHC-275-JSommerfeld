""" 
Recursion.py


Let's talk about functions:
    - f(x) = x^2, it takes an input x and multiplies it by itself. 
    - Named procedures that we can call to perform some subtask in our program 
        - Evaluate step by step from start to finish
"""

def foo(x):
    if x % 2 == 1:
        return "Odd"
    if x % 2 == 0:
        return "Even"
    
""" 
Function ends after either the function body ends or when a value is returned. What recursion does is it allows us to have repetition in our program
without having any for-loops/while-loop 

A recursive function is a function that calls itself within the body of the function 
"""

def bar():
    print("hello") #printing hello
    bar() #calling bar again within the body of bar
    
""" 
Running this function just prints hello infinitely. This is a rabbit hole that gets very deep very quickly.

The question is: how do we make it so the program doesn't run forever? We need something called an exit condition (base case)

Every single recursive function can broken down into two pieces:
    - Base Case (This ends the function call)
    - Recursive Case (repeats until you hit the base case)
    
For a recursive function to end, your recursive case HAS to be able to reach the base case

"""

def countdown(n):
    #print every value from 10-1
    
    #base case
    if n == 0:
        return 
    
    #recursive case
    print(n)
    countdown(n-1)
    
countdown(10)

""" 
Typically every single recursive function can be implemented iteratively (for-loops), so the question is: why do we care at all about implementing procedures recurisvely

Answer: a lot of the time, procedures that are hard to implement with for-loops are much easier to implement with recursion

Factorial in math

5! = 5 * 4 * 3 * 2 * 1 <= this procedure can be easily implemented recursively, and its a little to understand iteratively


is 5! equivalent to 5 * 4!
                        4 * 3 * 2 * 1
                        
is 5! equivalent to 5 * 4 *3!
                           3 * 2 * 1

5! = 5 * 4 *3 * 2!


1! = 1

x! = x * (x-1)!

Base Case: 1! = 1

Recursive Case:  x * (x-1)!
"""

def factorial(x):
    """
    It multiplies x by every value less than x 
    """

    if x == 1:
        return 1
    
    return x * factorial(x-1)

print(factorial(5))

""" 
Fibonacci Sequence: 
    0, 1, 1, 2, 3, 5, 8, 13, 21 .....
    
The Fibonacci Sequence is defined by a function called the Fibonacci function. 

F(n) = F(n-1) + F(n-2)

Base Cases:

F(0) = 0 and F(1) = 1

Recursive Case:

F(n) = F(n-1) + F(n-2)

"""

def fibonacci(n):
    #Base Cases
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    #Recursive Case
    return fibonacci(n - 1) + fibonacci(n - 2)

print()
for i in range(11):
    print(fibonacci(i), end = " ")
    
""" 
Palindrome, we can also do it recursively

RacecaR
R     R
 a   a
  c c
   
   e
   
In terms of palindrome, what could be a good basecase? len(word) =1

RacecaR
 AcecA
  CeC
   e
   
Recursive Case could just be checking the endpoints of each subword (where a subword is the endpoints of previous subword) 
"""

def palindrome(word):
    #base case
    if len(word) == 1 or len(word) == 0: #len word == 1 for odd letters and len  word == 0 for even letters
        return True
    
    #Recursive Case
    if word[0] == word[-1]:
        return palindrome(word[1:-1])
                            #this gives second letter through second to last letter
    else: 
        return False
    
print()
print(palindrome("moom"))


word = "racecaR"
print(word[::-1])
    




""" 
Recursion Continued and maybe we'll go over algorithmic complexity

Recall recursion: It's a just a function that calls itself within the body of said function
    - Base Case: How the function passes control back to main
    - Recursive Case: The part the repeats until the base case is met
    
    - Countdown (a contrived example)
    - Factorial (which has a hidden recursive definition)
    - Fibonacci sequence (which has a very recursive structure)
    
Thinking about problems recursively works well if you can figure out what the solution is, but its hard to do that <-
this pretty much only comes with practice

Where recursion really helps: Analyzing data this is nonlinear.
    - Lists are linear
    - Dicts are kind of linear
    - Maps/2D lists/Grids/etc. can be traversed nonlinearly. (there is no real notion  of what "next" means)
        2d Lists
            - Going across the row first
            - Going down the column first <= not equivalent to the prior depending on what data is stored in that 2D List
            
        2D lists end up becoming a good candidate for recursively based problems
        
In the field of computer science
    - Sorting: Sorting a hand of cards/sorting an unsorted list/etc.
    - Searching: Information Retrieval 
    - Path finding: Finding a connected path between two points inside of an unstructured data structure
"""



""" 
What is a valid path to get from the entrance to the exit? This a recursion problem:

    - Base Case
        - Whether or not the current pointer is in the bottom right 
    - Recursive 
        - Down Case: Go as far down as you can until you hit the exit or a wall
        
        - Right Case: Go as far right as you can until you hit the exit or a wall
        
        - Backtrack: Removes deadends from our path and restores the pointer back to the last possible valid move
        
    Really our algorithm can be determined with only down, right, and back moves
    
    
We need two functions:
    - Helper function that checks for a valid move
        - Return True if the current space is a valid space (is this a 0)
    - The actual path finding algorithm:
        - return a list of ordered pairs that corresponds to a valid path 
"""

def validMove(board,x,y):
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 0
           #Return True if all three cases pass, and returns false if any of them fail

def pathFind(board,x,y,path):
    #path is a list of ordered pairs corresponding to valid moves
    
    #Base Case:
    if x == len(board) -1 and y == len(board[0]) -1:
        path.append((x,y))
        return path #this return path guarantees that the pathfinding algorithm will terminate
    
    #Recursive Case:
    if validMove(board,x,y):
        path.append((x,y))
        #Down Case:
        if pathFind(board,x+1,y,path):
            return True
        
        #Right Case
        if pathFind(board,x,y+1,path):
            return True
        
        #BackTrack Case
        path.pop()
    return False


BOARD = [    #Entrance (0,0)
             [0,1,1,1,0,0,0],
             [0,1,0,1,1,0,0],
             [0,0,0,0,0,1,0],
             [0,0,1,1,0,0,1],
             [0,1,0,0,1,0,1],
             [0,1,0,0,1,0,0], #exit down here (len(board) -1, len(board[0]) -1)
    ]


def search(board):
    path = []
    if pathFind(BOARD,0,0,path):
        for pair in path:
            board[pair[0]][pair[1]] = "X"
    else:
        return "path not found"

pathtoexit = search(BOARD) #0,0 for top left corner, pass in an empty path initially
print()
for row in BOARD:
    for char in row:
        print(char, end="")
    print()
    
    
""" 
Recursion is also good for efficient searching:
    - Linear Search
    - Binary Search
    
    
"""

nums = [i for i in range(1000)] #0-999


def linearSearch(list,target):
    #it finds the index of the target
    for i in range(len(list)):
        if list[i] == target:
            return i
        
    return "not found"

""" 
How many comparisons need to be made to get to the 847th element? 847 comparisons

847 comparisons on an ordered list feels bad. If i know the numbers are in order, is there a faster routine to work this out? 
"""


nums2 = [1,5,7,11,15,17,20,25]
                        #if 20 was my target, linear search would have to go up until the second to last number
                        
                
""" 
If I just look at the middle of the list, 15, I can throw away the left half of the list. Then I a have a list of 3e numbers, 17,20,25. Then I can look in the middle
of THIS sublist, and see I get 20 on the second comparison

By using this routine, we dropped our comparisons required from 7 to 2.

This algorithm is called Binary Search and it halves the amount of numbers you need to check. 

Base Case:
    - We found the target
    
Recursive Case:
    - If Mid < Target
        - we throw away the left half of the list and perform binary search again
        
    - If Mid > Target
        - We throw away the right half of the list and perform binary sarch on the right half of the list
"""

def binarySearch(list,target,curr_iter):
    mid = len(list)//2
    #Base Case
    if list[mid] == target:
        return target, curr_iter
    
    #Recursive Case:
    if list[mid] < target:
        return binarySearch(list[mid:],target,curr_iter+1)
    
    if list[mid] > target:
        return binarySearch(list[:mid],target,curr_iter+1)
    

print(binarySearch(nums,847,0))


""" 
binary search found 847 in 7 comparisons versus linear search which took 847 comparisons. So binary search was significantly faster. 

Tomorrow we are going to do algorithmic complexity, after that we get the lab. 
"""