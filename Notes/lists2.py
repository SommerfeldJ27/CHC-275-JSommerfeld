"""
range(<name of list>) <= creates a list of numbers corresponding to the indicies of a list
range(len(mylist)) <= we can do this for a loop instead
len(mylist) <= returns the length of the list
"""
mylist = [10,20,30,40]
for i in range(len(mylist)):
    print(mylist[i])
    
for num in mylist:
    print(num)
    
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i + 1

"""
Different Ways for Traversing a List
    1) For i loop
    2) For each loop
    3) While loop
"""