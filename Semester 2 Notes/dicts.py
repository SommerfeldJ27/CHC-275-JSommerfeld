#dicts.py

""" 
We just did 2D lists which are just lists of lists. The only real way we know to aggregate data under one variable name is through lists.

Today we are going to learn dictionaries, which is another kind of data structures

data structures = its own subfield of CS dedicated to the storage of information and efficient retrival/sorting of that data

Dictionaries == Hashmaps/Hash tables in other programming languages

Information in dictionaries are stored using something called a hash function <- a really complicated mathematics function
https://en.wikipedia.org/wiki/Hash_function <- Source if you want to learn how this works theoretically


Lists <- ORDERED collections of data under one variable name

What uniquely determines a value inside of a list? <- the index uniquely determines a value/position

list = [1,0,1,1,1] <- the difference between the ones is which index its at.

What happens if you remove something in the middle of a list? Everything AFTER that value shifts over to i-1, which is BAD in some cases. 

Think about our implementation for bank:

names = []
balances = []

We supposed that the schema (defining structure of the data) of names and balances is that each name and balance shares THE SAME index

JOHN = INDEX 0 = names[0] and balances[0] 

This is not the ideal way to do this for this reason: 
    - Remove people from the bank.
    - If WE ONLY removed from names
    
    
Joseph, Mark
1000, 0, -250

If we get any sort of schema drift (if the lists become misaligned), then all of a sudden our records are not correct anymore. This is the motivation
for why we care about dictionaries

Lists had indices and values,

Dictionaries have key-value pairs

A dictionary is an UNORDERED list where the elements are (key,value) pairs

"""

mydict = {}
        #curly braces to define a dictionary

#we can populate a dictionary at variable instantiation by using :,s

mydict2 = {"John":1000, "Joseph":0, "Mark":-250}
#So now each name and balance is instead a key,value pair inside of a dictionary. 
#How do we retrieve from a dictionary? How did you do it for a list? You would use the square bracket operator

print(mydict2["John"]) #what do we expect to print out? 1000

""" 
Getting values from a dictionary uses this syntax

<name of the dictionary>[<key>] <- this returns the value at the key
"""

print(mydict2["Mark"]) #-250

""" 
Rather than indices uniquely determining values, KEYS uniquely determine values. 

Let's talk about keys:
    - What is allowed to be a key? IMMUTABLE OBJECTS
        - Mutable: Lists
        - Immutable: strings, numerics
        - Immutable objects are the only things allowed to be keys <- its because of the hash function really 
        
        | key 2 | key 1 | key 3
          4 bytes 2 bytes  1 byte
    - Can a key have more than one value? NO
        - Graphical test we use in algebra 2 to determine if a graph is a function? 
            - VLT = Every X value has EXACTLY one Y value
            - Dictionaries work on a hash FUNCTION

Let's talk about Values:
    - What is allowed to be a value? LITERALLY ANYTHING can be a value? 
        - does that include lists? YES
        - does that include strings? YES
        - does that include ints? YES
        - does that include another dictionary? YES
 """
 
mydict3 = {1:["a","b","c"],2:{"foo":10},3:True}

print(mydict3) 

""" 
The question is, how we get get "a" from this dictionary?

How did we get individual values from a 2D list? How many sets of square brackets did we use? two sets?

grid[row][col]

The same syntax works for nested lists inside dictionaries and nested dictionaries inside dictionaries
"""

print(mydict3[1][1]) #we should expect to get the letter b
print(mydict3[2]["foo"]) #print 10

""" 
Keep this example in your brain, highly important for the lab? How about adding things to a dictionary

.append()  <- does not exist for dictionaries

<dict>[<newkey>] = <newvalue>
"""

mydict2["Frank"] = 10000 #this adds Frank:10000 to the dictionary

print(mydict2)
print(mydict2["Frank"])

""" 
How about removing something from a dictionary? There are two different ways: one of which is very unsafe, the other way implicitly handles
the exception that you could get. 

1) del keyword <- this just zaps the key:value pair from memory 

"""
del mydict2["John"]
print(mydict2)

""" 
The second way is .pop(), which is a much safer way, for a list this takes in ONE parameters.

but for a dictionary, it takes in two parameters.


"""

mydict2.pop("Joseph","user not found")
            #key     #error message if key not found
print(mydict2)

print(mydict2.pop("Joseph","user not found")) #remember returned values need to be printed if you want to use them 
print(mydict2)

""" 
We've answered:
    1)How do we retrieve information
    2)How do we add information
    3)How do we remove information
    
We still need to answer:
    1)How do looping statements behave for dictionaries
    
The developers of python have two natural choices for what happens in a for-each loop


"""

for x in mydict2: #Lets think about what makes sense for x to be #it could be either the keys or the values? 
    print(x) #we got the keys
    print(mydict2[x]) #if we want the values within the dictionaries
""" 
for each loops give us the keys. 

There is something important that we need to make note of. square brackets ALWAYS directly accesses memory. There might be times where
we DONT want to do that


.values() <- returns a view object of the values
.keys() <- return view objects of the keys
"""

for x in mydict2.values():
    print(x) #this gets the balances
    
    
""" 
Tuples: 
    - Keys: HAVE TO BE IMMUTABLE
        - Restricts us to Strings and Numbers <- this might not be sufficient for some usecases
        
        
"""

accounts = {} #<= this is how you create a dictionary

""" 
KEYS: NAME FOR THE ACCOUNT HOLDER
VALUE: BALANCE

THE SCHEMA OF THIS DICTIONARY IS KEYS: ACCOUNT NAMES VALUES: BALANCES (NAME:BALANCE)

two people: 
    - John Smith : -250
    - John Smith : 1000000
"""

accounts["John Smith"] = -250 #we add the first John Smith
print(accounts)
accounts["John Smith"] = 1000000 #this is no longer adding into the dictionary, this becomes variable reassignment
print(accounts)

""" 
NAMES ARE NOT SUFFICIENT TO UNIQUELY DETERMINE DIFFERENT CORRECT. IDEALLY IN A PERFECT WORLD, WE WANT MULTIPLE PIECES OF INFORMATION
TO UNIQUELY DETERMINE SOMEONE
    - LISTS 
    - DICTIONARIES
    
are these mutable or immutable? MUTABLE, so we can't use them as keys. we need a new data structure that can hold a collection of objects
while also being immutable

THE TUPLE SOLVES THIS PROBLEM
"""

mytuple = () #<- this is a tuple
#typically tuples are used as unique identifiers for other variables

ID1 = (1,"John Smith")
ID2 = (2,"John Smith") 

accounts2 = {ID1:-250, ID2:1000000}

print(accounts2[ID2])

""" 
THIS IS A COMMON INTERNSHIP INTERVIEW PROBLEM:

    1) What is the difference between immutable and mutable objects?
    2) What is the difference between a tuple and a list? 
"""

""" 
REMEMEBER THIS FOR THE LAB:

DIRECTORY <- DICTIONARY

<"NAME OF THE STUDENT">:{"GRADES":{},"GRADELEVEL":INT,"EMAIL":STRING}


FOR ADD STUDENT:
    -ASK FOR THE NAME
    -EACH GRADE INDIVIDUALLY
    -THE EMAIL
    -GRADE LEVEL
    
    -ASSEMBLE THE GRADES DICTIONARY USING THE GRADES YOU ASKED FOR 
    -ADD THE STUDENT INTO THE DIRECTORY DICTIONARY USING THE NAME YOU ASKED FOR AS THE KEY
"""