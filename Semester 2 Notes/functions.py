#functions.py

"""
We are not presenting projects

We are going straight into creating our own functions.

We need to remember what functions were:
    - a rule that takes in an input, transforms it, and spits something out
    
    f(x) = x + 5
    
    takes in a value x, adds 5 to, and returns the value x + 5.
    
Functions in programming are pretty much the exact same thing:
    - a repeatable routine that:
        - may or may not include an input
        - may or may not include an output 
        
Let's think why this might be appealing to us: 
    Lab 3 or 4, where file IO was really important (stock picker lab)
        - We had to read in a file,
            - manipulate the raw string data into integers and place corresponding lists
        - Take the average of the stock prices
        - compare average 1 to average 2
        
How did we rectify the fact that we had to deal with different files? (day 1-20 and 21-40), what we ended
up doing was just copying the program and pasting it again but changing the file name

Using functions is appealing because we can create named routines that we know we're going to use often
Rather than copy and pasting a bunch of code over and over again, we can actually just write the routine once,
and call the function twice. 

What are some examples of functions that we used before? 
    - input(<prompt>) <- this is a named routine
        -  print <prompt> to terminal
        -  wait for user input
        -  store the user input into the variable input() was being assigned to
        - ex. name = input("What is your name? ")
            - prints "what is your name? "
            - waits for the user to type their name in
            - assigns that name to the variable "name" 
    
    - .lower() 
        - change all of the characters in a string to lowercase
    
    - .strip()
        - removes all of the leading and trailing white space of a string 
        
Great: we see the appeal, we know we've used them before, how do we actually write our functions?

def <name of the function>(): <- syntax for defining our own function



"""


def foo(): #<- def <function name>(): is called the function header
           #includes the function definition, the function name, and the parameter list 
    print("bar")


""" 
In this case, our function is very simple, all we're doing is printing "bar" to the terminal. 

How do we call said function? 
"""

foo()
#REMEMBER: when we call a function, we ALWAYS need to end it with parentheses
#REMEMBER: tab back over to the left

def add5(num):
    #function definition: def
    #function name: add5
    #parameter list: num
    
    """
    When we add a parameter into the parameter list: num is a placeholder for a value we can specify later on
    
    num does not exist yet, we must specify it later on when we call the function. DESPITE THIS, 
    we can treat num as if it does exist and is a variable. 
    """
    
    num = num + 5 #Recall this design pattern from the start of last semester, all this does
    # is add 5 to the value num. 
    print(num)
    
add5(8)
add5(4)

mynum = 10 #I can pass in the raw values 8 and 4, or any variable
add5(mynum)

""" 
When we a use a function: "calling the function"
In the function header: the stuff inside the parentheses is called the "parameter list"
    - each individual value in the parentheses are called parameters

at runtime: 
    - the stuff inside the parentheses are called "arguments" 
    
we can think of the parameter as being an abstract placeholder and the arguments as being explicit
examples of the parameters. 
"""

""" 
I can pass in multiple parameters
"""

def multiply(num1,num2):
    #function name: mulitply
    #parameter list: num1 and num2
    
    product = num1*num2
    print(product)


multiply(3,5)
multiply(4,10)
#This is weird 
multiply(4,"a") 

""" 
python is dynamically typed: we don't have to specify the data types of our parameter list. 
We can call the parameters whatever we want, but we can't guarantee that the behavior is going to correspond
to specific data types. 
"""

def add(num1,num2):
    sum = num1+num2
    print(sum)
    
add(2,5)
add("hello","world")
add("world","hello")
#add(2,"5") #This is going to cause a type error

""" 
For our parameter list: the order matters. So in our add function:
add("hello","world") = "helloworld"
add("world","hello") = "worldhello" 


"""

def studentUpdate(name,age,gpa):
    age = age + 1
    print(f"Student name: {name}, student age: {age}, student gpa: {gpa}")
    
studentUpdate("bob",15,4.0)
#we expect bob, 16, 4.0
#studentUpdate(15,"bob",4.0)
#this is a type error

""" 
The bottom line: 

in the add example, we got lucky and didn't get a runtime error because the two data
types are expected to match.

In the studentUpdate example, we didn't get so lucky. When we passed "bob" into the "age" parameter, 
we got a runtime error because of the mismatched data types. 

It is our responsibility as programmers to make sure that the function we write gets the arguments 
we expect. 

for the last 5 minutes, I'm going to leave us with a thought experiment:
""" 

def update(num1):
    num1 = num1 + 10
    
x = 5
update(x)
print(x)

""" 
we expected 15, but 5 ended up getting printed out? Why is that the case?

pass by value vs pass by reference <- which we are going to pick up with next class. 

Before we talk about pass by value and pass by reference, we need to discuss mutability

mutability = ability to be changed or the possibility of having its state changed

immutable = its state cant be changed
mutable = its state CAN be changed

Based on our example above, integers are IMMUTABLE

the typical heuristic to figure out if something is mutable or immutable:
    - whether or not its size can change (its length)


mutable:
    - lists
    - strings

immutable:
    - numbers
"""
print("mutability example")
mylist = [1,2,3,4] #this is a list, its length can change

print(mylist)
def update2(nums):
    #we are expecting nums to be a list here
    nums.append(5)

update2(mylist)
print(mylist)

""" 
immutable objects are passed by value
    - when the function is called, python will make a temporary copy of the variable, and the variable outside of the function won't get updated
    
mutable objects are passed by reference
    - when the function is called, python will directly access the variable and update it if any changes are made. 
    
It's called pass by reference because:
    variables:
        - the name of the variable itself (we can think of this as a memory address)
        - its data type
        - the value(s) itself
        
    variables are named locations in memory where you can store a value
    
so when we say we are passing by reference, we are passing in the LOCATION of the object rather than the VALUE of the object.

How exactly do we update immutable objects? 

we have to use the "return" keyword

    - input() specifically "returns" a string
    
for objects declared inside of a function (this is including the copies of arguments for immutable objects), they have a limited lifespan. 

for example, if we created a function called foo(x), and x is supposed to be an integer, then x has a limited lifetime, after foo(x) ends, x 
will be destroyed and that memory will be freed up
"""
""" 
def foo(x):
    factor = 0.2
    print(factor)
    print(x*factor)
    
foo(5)
print(factor) 
print(100 * factor) #factor is still inaccessible
""" 

""" 
we can think of return as python flagging the computer to remember certain pieces of information from the function's lifetime.

Each codeblock in python has its own "scope" so things outside of that codeblock's "scope" can't access variables created inside that scope. 

When we did stuff like 


for x in mylist: x has a temporary lifetime, it can accessed within the scope of the for-loop. Tab levels indicate scope in python. 

"""

def updateBalance(money,change):
    #two parameters, money and change.
    money = money - change
    return money #if we return money, then we are flagging to the system to keep money within the system's money
    #all return does is flags the computer to remember something. We need to assign that remebered variable to something
    
print("return example")
balance = 500 
print(balance)
balance = updateBalance(balance,200) #just like using input, we need to assign this value back into a variable
print(balance)