""" 
lists2.py

last time we talked about lists I showed you
    -how to makes lists
    -how to access elements in lists
    -for loops
    
for-loops make copies of elements rather than directly accessing them so when we did a forloop and modified
num it didn't update the list.


"""

mylist = [10,20,30,40,50]
            #0,1,2,3,4
            
""" 
So would you say the indices also count as an ordered sequence of elements? YES

so rather than traversing the list of elements in a for-loop. we could traverse over the indices instead. 

there are two new functions involved: 

    range(<name of list>) <= creates a list of numbers corresponding to the indices of a list. 
                          <= creates a list from 0-length minus one. 
                          
                          
    range(len(mylist)) = [0,1,2,3,4] <= we can do a for-loop over this instead. 
    
    len(<name of list>) = this returns the length of the list 
    
    
"""

for i in range(len(mylist)): #for all numbers from 0-4
    print(mylist[i])

for num in mylist:
    print(num)
    
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1

""" 
These are our three different ways of traversing a list. 

    1) for-i loop
    2) for-each loop
    3) while loop 
"""

print("example 2")
for i in range(len(mylist)):
    mylist[i] = mylist[i] + 5 #This directly accesses the list instead of making a copy so this
                              #will update the list

print(mylist)

print("example3")

""" 
Lists in python are dynamically sized. we can add and remove elements from the list 

To add something to the list:
    -<nameoflist>.append(<value we want to add to the list>)
"""
#first way
names = ["john","joe","paul"]
print(names)
names.append("zach") #appends zach to the end of names
print(names)

""" 
There are two ways to remove something 
    -either by the index
    -by the value 

-by the value

<nameoflist>.remove(<value you want to remove>)

-by the index

<nameoflist>.pop(<index at which you want to remove>)
"""

names.remove("joe") #.remove() is specifically for values
print(names)

names.pop(0) #pops the element at index off the list 
print(names)

print("example 4") #adding names to list program
names = [] #this makes an empty list
check = False
while check == False:
    name = input("Enter the name you want to add to the list: ")
    if name == "quit":
        check = True
    else:
        names.append(name) #adds the name you typed in into the list of names. 

print(names)

print("example 4")

students = ["john","zach","Paul"] #this is a little dangerous for which reason? mixed data types
GPAs = [88,71,85]

""" 
How are these two lists logically linked together using some aspect of the list. they're tied by the index.

"""
#keep this example in mind for the next assignment. 
for i in range(len(students)): #does it matter which list we take the length of?
     print(f"Student: {students[i]} GPA: {GPAs[i]}") #I can use the iterator to access both lists 


""" 
we are assuming that the user of the program has perfect knowledge and can access the contents and indices
of the list. This is a bad assumption (lists are dynamically sized, its bad to assume the same
elements will be in the same indices)

we need a way to search our list. How can we get the index of elements out without having to look at the
code beforehand? 

.index() 

<nameoflist>.index(<value>) <= returns the index of the object in our list. 
"""
print("example 5")
index = students.index("zach")
print(index) #should print 1

