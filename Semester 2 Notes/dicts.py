#dicts.py

""" 
We've only ever used one data structure so far:
    - A list
    - 2D list 
    
2D Lists as lists of lists. 

What uniquely determines an element in a list? If I were to get an element
from a list, what piece of information within the list identifies that object?
    - Its position (index) inside of the list

That might not be the best way to uniquely identify an object. There are other ways
to naturally order objects.

    - We can order people:
        - Birthdate (index) 
        - Class year (not necessarily an index because there's no difference within
        the groups)
        - By the order they walked in the room (which is basically another index)
        - Identify them by their names 
        
Lists in python are ordered sequences of objects and the index uniquely identifies
each object 
   
   
[1,2,3,1] 

We might want to identify things by other attributes: Dictionary 

In other languages, they might not be called dictionaries, hashmaps/hash tables

The way dictionaries work is you have a list of UNORDERED objects, and they are differentiated
by their key 

{(key:value), (key:value), (key:value)}

Objects in dictionaries are key:value pairs
"""

products = {"oranges":0, "apples":5, "pears":10, "grapes":8}
#to make a dictionary in python, you would use the curly braces at variable 
#creation

""" 
In my products dictionary, I'm going to create a bunch of key:value pairs that 
correspond to products and their quantities

when we create a dictionary, we can fill the dictionary with key:value pairs
by using <key>:<value> 

EVERY KEY REQUIRES A VALUE. How do you think I would retrieve a value from a dictionary?

I can retrieve information using the square bracket operator as usual
"""

print(f"Oranges: {products["oranges"]}")

""" 
list[index], dict["key"]

As opposed to lists where the position uniquely identifies every object, in a dictionary, it is the key that uniquely identifies
every object. 


"""

productsList = [0,5,10,8] #same values as the products dictionary
print(productsList[0]) #i don't know what this values correspond to? 

productsList.pop(0)
print(productsList[0]) #5

""" 
Using the position as a unique identifier might not be the best idea in some circumstances because what happens
when an item gets added or removed from the list? All of the positions change

if index 0 is SUPPOSED to correspond to oranges, and for some reason .pop gets called on the list, then our indices
no longer match up with our table of contents.

Dictionaries circumvent this problem by having very verbose indentifiers for objects. The existence of dictionaries
directly solves the problem from lab 2 involving banks, because in that lab we had two parallel lists, so if one list
becomes unaligned with the other, we will end up having a lot of problems. 

Rather than having two parallel lists, one for the name and one for the balance, we couldve instead had 

A SINGLE DICTIONARY, where the key was the name and value the balance


There are some rules you need to know about dictionaries (about keys):
    - what things can be keys?
        - Keys MUST be immutable: They can't change 
            - Strings
            - integer values
            - Floating point values
        - the technical reason why this is: 
            - Dictionaries are also called hashmaps, so how it works is the data is fed into a hashing function based on the key
            so if the key changes, the output of the hashing function also changes (https://en.wikipedia.org/wiki/Hash_function)
    - Can you have duplicate objects inside of a dictionary? 
        - The answer is YES for values but NO for keys
            - Having a single key map to two things breaks a certain mathematical principle about functions: 
                - This breaks the vertical line test 
                
How do we add things into a dictionary? in a list we would use .append(), but for dictionaries this wont work because
we need to also specify a key   
"""

products["bananas"] = 15
#the syntax is <nameofdict>[<new key>] = <new value> this is completely different syntax than before
print(f"bananas: {products["bananas"]}")
#what if I tried to redeclare my key and point it to a new thing
products["bananas"] = 10
print(f"bananas: {products["bananas"]}")
#because having one key mapping to two objects breaks the VLT, the natural way to deal with this kind of operation
#is to just overwrite the value at that key

""" 
Do all of my keys need to be the same data type? The answer is no,
"""

products[1] = 60
print(f"1: {products[1]}")

""" 
What happens if we print the entire dictionary? We are going to get all of the keys and their corresponding values
"""

print(products)

""" 
What about looping statements? If you know what happens you're a genius, but otherwise its fine. For looping statements over
dictionaries, there are two natural options:

1) Keys
2) Values
"""

for x in products: 
    print(products[x])
    
""" 
For loops over dictionaries explicitly returns the keys. So if I wanted the value, how would I change that print statement?
knowing that x is now a key.

Remember if you want the values out of a dictionary you need to use square brackets. for-each loops behave strangely for dictionaries

There are two helper functions baked into dictionaries that allow you to make the "shallow" copies of the values/keys

Let's say you were a teacher, and you wanted to see if a curve would dramatically affect the mean of a test 
"""

test = {"john":60,"mark":75}

""" 
test.values()
<dict.values() <- returns a list of the values inside of the dictionary
"""
average = 0
for grade in test.values():
    average += grade + 5
    
average= average/2
print(average)
print(sum(test.values())/len(test.values()))

print(test)

""" 
dict.keys() gives you the keys
"""

for name in test.keys():
    print(name)
    
""" 
What about the values? Would there be a natural restriction on values? No, anything can be a value

INCLUDING:
    - lists
    - Another dictionary
"""

testdict = {1:"hello",2:True,3:[1,2,3],4:{"foo":1,"bar":2}}
print(testdict)

""" 
Last class we covered dictionaries. These are a new kind of data structure that offer tradeoffs versus standard lists

1) Information retrieval ends up being more descriptive, because we store things in key-value pairs over position-based 
descriptions, information retrieval ends up becoming more intuitive. 
2) the syntax is much harder and there are a lot of limitations on what can be a key
    i) Immutable objects
        - Integers
        - Strings
        - Tuple <- we'll get to this
        
Creating a dictionary requires curly braces

mydict = {} <- curly braces instead of square brackets

information retrieval is done the same way as a list

mydict[<key>] <- this returns the value associated with the key 

There are helper functions that might be useful such as .keys() and .values()

1) When we do a for-loop over a dictionary, what does the temp variable represent?
    - Keys or Values? For-loops return keys
"""


""" 
Adding things is different compared to lists: 
    1) for a list we used .append()
    2) for a dictionary, we need to specify both a key and a value 
        i) dict[<key>] = value
        
Dictionaries are based on something called a hash function <- wait until college to figure this out

There are some questions that we have unanswered:
    1) How do we remove something from dictionaries? 
        - There are two ways 
"""


mydict = {1:"foo",2:"bar",3:"hello"}


""" 
The unsafe way: is using the del keyword.
"""

del mydict[1] #this will remove the key/value pair at the key specified
print(mydict)

#del mydict[1] #This is unsafe because you can accidentally delete the entire dictionary or you can get a keyError
#which terminates the program if the key doesn't exist. 
#print(mydict)

""" 
Rather than getting name and key errors from making a mistake with del keyword, we can use a dictionary builtin function
that accomplishes the same thing but returns a value instead of just straight up crashing the program

.pop(<key>)
"""

mydict.pop(2)
print(mydict) #3:"hello"

""" 
.pop() for lists take no other argument, but for dictionaries, if the doesn't exist anymore, you can specify a second argument
that is returned when python doesn't find the key specified
"""
print("after second pop")
mydict.pop(2,0) #pop key 2 and return 0 if key 2 isn't in the dictionary
print(mydict)

print(mydict.pop(2,"object not found"))

""" 
.pop() returns the value that was deleted
"""

mydict.clear() #this just removes everything from the dictionary 
print(mydict)

""" 
mutable objects are pass by reference: lists, dictionaries, etc. 

immutable objects are pass by value: integers and floats/strings 

dictionaries model file types called .JSONs <- when you are parsing JSONs through dictionaries it would be useful
to have a clear function because you don't want to destroy the RAM on your computer. 

The last new data structure I'm willing to introduce in this class is called a tuple. <- They are just lists that are immutable

tuples use the ordered pair notation. (x,y) <- tuples use this same notation
"""

mytuple = (10,20,30)
print(mytuple)

#mytuple[1] = 200 #tuples are immutable, this should give me an error
print(mytuple)

"""
why do we care about tuples? they just seem like worse lists. 

can a List be a key? lists are mutable so they can't be. 

So if I wanted a key to be a collection of information, I can't use a list

People can have the same name, so I can't just use a raw string

"John Smith" <- can't have this just be my key, you can have multiple John Smiths 

(studentID,firstName,LastName) <- this is a satisfying key because studentID uniquely determines a student 
"""

students = {}


students[(1,"John","Smith")] = {"english":80,"math":90,"econ":71} #this is typically a much safer way to store
students[(2,"Myles","Whatever")] = {"english":85,"math":90,"econ":71} 
#user information in a dictionary. 
print(students)

""" 
Typically going to be served data in a .csv (which is a spreadsheet) -> construct keys using tuples from columns
of the spreadsheet -> you will use such tuples as keys for a dictionary -> you will serve that data as a .JSON file 
from a dictionary 

^This is how APIs work basically 
"""


#Syntax tip for the lab
mydict = {} #students in main
mydict1 = {} #individual student level
mydict2 = {"foo":10} #grades

mydict["a"] = mydict1
mydict1[1] = mydict2

#in a 2D list we did double square square brackets to get an individual number

print(mydict["a"])
print(mydict["a"][1]) #this should give me mydict2
print(mydict["a"][1]["foo"]) #this will give me the number 10