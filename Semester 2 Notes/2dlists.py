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



#What is the data type of row? 
for row in box: 
    for num in row: #the data type of a row is a list
        print(num) #is print 1-9 on individual lines
    

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