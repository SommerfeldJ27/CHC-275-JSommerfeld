"""
Lists.py

recap:
create variables
manupulate them
    math
branching ctrl structures
    if
    elif
    else
repetition using while loops


"""

num1 = 10
num2 = 20

"""
Lists - linear ordered collections of objects under 1 variable name (under 1 memory adress)
"""

mylist = [5,10,15,20]


"""
this creates our list
how do we access only 1 singular element from our list?
square bracket opperator 
"""



"""
counting in comp sci starts at 0

"""

"""
print(mylist[0] * mylist[3])

sum = mylist[1] + mylist[2]
print(sum)
"""

mylist = [5,10,15,20]
for num in mylist:
    num = num + 5
print(mylist)
    
i = 0
while i <=3:
    mylist[i] = mylist[i] + 5
    i = i +1
    print(mylist)