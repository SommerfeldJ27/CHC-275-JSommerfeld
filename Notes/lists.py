""" 
Lists.py

Recap of what we are capable of doing:

    - Create Variables, manipulate them in basic ways
        - Doing arithmetic
    - Branching Controls Structures using if-elif-else
    - Repetition Control Structures using While loops 
    - Keyboard input using the input() function
    - Typecast variables to differnt datatypes 

the benefit of using a computer at all is the amount of data your computer is capable of processing. 

So if I wanted a bunch of related data points, the only way I can do that currently is by creating
a bunch of individual variables
"""

num1 = 10
num2 = 20

""" 
what happens when our data set is 100 data points long? Creating individual variables is a really
unwieldy way of going about this. We need some sort of way to aggregate related pieces of information
under one alias. <= name

we do this in python with lists. 

Lists = linear, ordered collections of objects under one variable name (under one memory address)
      = lists are also variables

<name of the list> = [<member attributes>]
"""

mylist = [5,10,15,20]
         #this creates our list
print(mylist)

""" 
How do we access ONE SINGULAR element from our list? square brackets indicate we're working with a list,
so we can use the square bracket operator on the variable name and place the index of the object 
we want to reference inside the square brackets. 

index = the numerical position of the object within the list 
"""

print(mylist[0])

""" 
Counting in computer science starts at 0. Really, the first element is index = 0. accessing elements
from a list behaves exactly like a variable would. 
"""

print(mylist[0] * mylist[3])
      #first number times fourth number. 

sum = mylist[1] + mylist[2]
print(sum)

""" 
NOTE: If you have worked in other programming languages before python, you would expect lists 
to HAVE to be the same datatype across all member attributes. 
"""

mylist2 = [1,3.14,True,"hello"] #< this is perfectly okay in python. 
print(mylist2[2])

#print(mylist2[0] + mylist2[3]) #we get a type error because we're to add an integer to a string

""" 
You will get an index error if you try to reference unallocated memory. 
"""
#print(mylist2[4]) #You cannot access places in memory that are not allocated yet. 

print(mylist2[-1]) #negative indices go backwards 

mylist = [5,10,15,20]

""" 
In programming there is a design pattern called traversing a list. 
    - Repetition control structure
    - One by one, access each element of the list. 
    
iterator = is a number that corresponds to the current index you're trying to access 
typically we use the letter i to denote your iterator. 

we will use a while loop and iterator to traverse our list 
"""

i = 0 #< the current index is the first one, so we set it equal to 0.
while i <= 3: #this is our exit condition
    print(mylist[i]) #Accessing mylist at the value the iterator is currently at.
    #what can we do to our iterator to make sure it hits the exit condition?
    i = i + 1 #we can increment i by 1 to go to the next value.  
    
""" 
Most of the time, index errors occur from not having a suitable exit condition. This kind of control structure
is a little cumbersome to use. 

There is an entirely second way to do this that is ALMOST equivalent. we can use for-loops to do almsot
the same thing 

for <placeholder name> in <name of the list>:
    <code block>
"""

mylist = [5,10,15,20]
print("with forloop")

    
""" 
It does not matter what name you use for the variable before in. What for-loops actually do 
    1) creates a temporary variable assigned to the name you give 
    2) it assigns the current value of the list tothat temporary variable to the location you created
    3) does the procedure in the code block 
    4) goes to the next item in the list
    
    num =/= mylist[i] <= These are not the same thing. They are two separate places in memory but hold
    the same value 
"""

mylist = [1,4,2,3,5,3]

for num in mylist:
    num = num + 5
    
print(mylist)
    
i = 0
while i <= len(mylist) - 1: #you should be using len(list) - 1
    mylist[i] = mylist[i] + 5
    i = i + 1 
    
print(mylist)

""" 
The for-loop did not update the list but the while loop did update the list. 

for loops create copies, while loops directly access the list. 

The way we've writteh the while loop, we make a huge assumption about the list. The assumption we're making
is that the list's last object is at mylist[3]. In more complicated programs, the list my be length 0
it might be length 100. 

There is a way to intrinsically get the last value of the list.

len(<name of the list>) <= is the absolute length of the lsit 
"""

print(len(mylist))