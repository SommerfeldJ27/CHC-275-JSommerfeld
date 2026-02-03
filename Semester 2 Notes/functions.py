#functions.py

"""
Last semester: 
    - if you missed one assignment or if you did poorly on one, that wrecks your grade
    - I did not test conceptual understanding all that much
    
This semester:
    - Drills <- this assignments are going to be very low stakes 
        - programming a small program
        - reading code and evaluating what the output is or whether there is an error 
        
Last semester we learned a lot about basic programming
    - variables, data types, how to input variables from the terminal using the input() function <- september
    - control structures
        - sequential evaluation 
        - selection (if-else)
        - reptition (looping statements like for loops and while loops)
    - lists (how to collect multiple pieces of information under one variable name)
    - file I/O and exception handling
    
One of the most annoying things about last semester:
    - stock picker lab
        - writing the solution once, and then copy and pasting the entire program again. 
        - we basically rewrote the same program twice for days 1-20 and 21-40.
        - This is not the most efficient way to go about this, 
            - Write the code once, and use it twice. 
            
We can enable this by using things called functions. You should have run into a similar concept in a math
class

f(x) = x^2

^ takes in x as an input and outputs x squared. 

Functions: 
    - named routines that you can repeat that outputs something
    - so rather it being a mathematical expression, it could also be a set of repeatable instructions.


This subject has a lot of nuance in programming 

pros:
    - we can reuse code rather than having to rewrite it all the time
    - much more readable. 
    
cons: 
    - kind of difficult to understand what is actually happening within the program. 
    - we introduce a large level of abstraction that we are not used to so far. 
        - this includes "control flow" being more complicated, in the sense that code execution has 
        owners and services. 
        

"""

#basic function example
def foo(): #this is called the function header. 3 parts to the function header. 
           #1. Def keyword. This tells the python interpreter that you are about to specify a function
           #2. Function name. This is the name of the routine that you to use. Ex, foo is the name
           #3. Parameter list. Are your inputs of your function, and they go inside the ()
    
    #starting from line 63, this is the function body. Function bodies need to indented. 
    #when a function ends, you must unindent the codeblock. 
    print("bar")

foo() #remember, when you are using a function, you must end that function name with the parentheses. 

""" 
Functions really like act verbs in plain english. You can think of the parentheses as being the period 
at the end of a sentence. 

This example feels a little stupid right, all we're doing is printing something out into the terminal. 
"""

def add(x,y):
    #1. def keyword 2. function name: add 3. parameter list: x,y
    #how parameters behave: they are just placeholders for values that we can plug in later. 
    print(x + y)
    
""" 
The parameter list is very confusing to first year students of computer science. In this program,
I have not previously assigned values to x and y, yet I am using them inside of the function body as if 
they exist. 
"""

add(6,7) #now I want to use the add function
add("foo","bar") #we can add two strings together as well. 
#add("hello",5) #this is going to be a type error
""" 
6 and 7 get plugged in for x and y when the function is used. For vocabulary purposes:
    - When we use a function, we are "calling the function" 
        - line 86 is a "function call" 
    - 6 and 7 are not parameters
        - they are called arguments. 
        
The parameter list are abstract placeholders for values to be used inside the function. 
The function's arguments at runtime (the stuff inside the parentheses), are explicit examples of those 
parameters. 

Here is a quirk about python: 
    - The data types of the parameters are not specified. 
    - When I use those values, python does not know what to expect until the function is actually called.
    
What is exactly happening during a function call? 
    - When you are running a program, the program has a concept called "ownership"
        - the primary owner of a program is python.exe 
        - python.exe is in "control" of the program
    - When we make a function call, python "passes control" of the program to the function being called. 
        - Weird things will happen with the program once we pass control.
        
    We can think of this as our computer's RAM being a map. 
        - one of the continents is python.exe
        - another continent could be a function. 
        - we can think of sailing from one continent to another as passing control of the program. 
    
    variables are declared within the function cannot be accessed from outside the function. 
    
"""

def transaction(x):
    tax = x * 0.06 #this is 6 percent sales tax
    print(x - tax)
    
transaction(100)
#print(tax) #tax is not defined outside of the function..


""" 
Functions' variables have temporary lifetimes. Things that are created inside of a function are going to
be destroyed after the function ends. 

This makes perfect sense: 
    - These programs can be running 24/7 365 days a year. 
    - If everytime a function is called, the intermediate variables persisted after the function ends. 
    - you would waste all of the resources on your computer. 

This concept of temporary lifetimes of variables is called scope.

Scope = what variables the function has access to at any given moment. 

python.exe has global scope. But transaction(x) has its own local scope. So anything declared inside
of its local scope is going to get destroyed when transaction passes control back to python. 

Here is a thought question:
"""

def add5(x):
    x = x + 5 #we're taking x and adding 5 to itself
    
num1 = 10
print(num1)
add5(num1)
print(num1) #the result of add5 did not save back into num1. 
#that feels weird

""" 
When we pass a global scope variable into a function and that function updates that variable in its local
scope, we should expect that value to change back outside in the global scope. 

Recall from for-loops: 

for x in mylist:
    x = x + 5

for-each loops created temporary copies of those variables. For-each loops have their local scope.   
"""

mylist = [1,2,3,4]

def add10(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10
        
print(mylist)
add10(mylist)
print(mylist) #this behaved differently than the previous example

""" 
This is a concept called pass by value vs pass by reference, this is where we are going to pick up tomorrow.

To understand pass by value vs pass by reference: we need to talk about mutability
    - mutability = ability to be able to be changed 

data types in programming can either be mutable or immuatable
    - mutable = it can be changed
    - immuatble = it cant be changed 
    
datatypes
    - integers = immutable
    - all numeric types are immutable
    
    lists = mutable 
    
pretty much anything that can change in length is mutable. So when it comes to functions, parameters that are mutable are pass by reference
and parameters that are immutable are pass by value

pass by reference = the parameter that actually gets passed in is the location in memory. <- when we change values at those memory locations
those edits are going to stick when the function passes control back to python. 

pass by value = the parameter that gets passed into the function is the value, so the value gets copied within the local scope of the function
so edits do not persist because we are not actually accessing the original variable, we are accessing a local scope copy.

So immutable objects, in local scope they end dying after the function ends. How do we keep local scope objects after a function call ends?

return <- this is how you save values after a function call ends. At the end of the function, if we use the return keyword, it'll flag python
to remember the variable you are to return when control is passed back to python. 
"""

def add7(x):
    x = x + 7
    return x #this is going to flag python to remember that x got reassigned to x + 7

""" 
When we talked input(), which is a function, I explicitly said "input() returns a string" 
"""

num2 = 10
print(num2)
num2 = add7(num2) #if you use return, you NEED to reassign this to a variable. 
print(num2)

""" 
All return does is flag to python that there is something worth remembering, it doesn't actually do the task of remembering said value. 

Any time we want a value to persist, we need to use return. Looking back at add(x,y), all we did was print the value x + y, not return it.

Typically for functions, you don't want to print within the function. Typically that result is relevant and SHOULD persist after the function ends.

"""

#DONT DO THIS
def add(x,y):
    print(x + y) #This is bad practice, you shouldn't do this
    
#DO THIS INSTEAD 
def add2(x,y):
    return x+y #this is the typical design pattern you should do 

num1 = 5
num2 = 10
sum = add2(num1,num2)
print(sum) #print in global scope rather than local scope 
