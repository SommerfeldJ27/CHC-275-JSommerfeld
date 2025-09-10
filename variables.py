""" 
file name: variables.py

Live coding: I write code in one python file and have my notes in multiline comments in between code 
segments

What is python? 

    - Python is a programming language
        - A set of syntax and protocols that you write instructions in for your computer to follow 
    
    - Python is a command line program
        - When you download python off the internet, you're downloading what is actually called
        the python interpreter
        
    - The interpreter's role on your computer
        - It looks at .py files, and line by line convert valid python syntax into machine code
        
    - Python is an interpreted language
        - We just point the interpreter at a python file and it'll run the code
        
    - Compiled languages
        - c, c++, java, etc. 
        - Call the compiler on your code file, and it'll get compiled into an executible file that you
        run 
        
    The first thing that is of importance to us are variables. 
    
    Variables carry three properties:
        - The name of the variable
        - Its data type
        - Its attribute <= the actual data itself
        
    A variable is just a named place on your computer's RAM that stores information
    
    
"""
x = 5
#^ This is a variable 
#<name of your variable> = <attribute> 
print(x)

""" 
Data Types: 

    - Numbers
    - Strings of text 
    
There are two datatypes for numbers
    - Integer: A whole number, including 0 and negative numbers
    - Float: Floating Point Number, pi 
    
"""
x = 5
#This is a variable named x, of type integer, of value 5 

""" 
We can add, subtract, multiply, divide, and square numbers
"""
y = 10
#Addition
print(x + y)
#Subtraction
print(x - y)
#Multiplication
print(x * y)
#Division
print(x / y)
#Squaring a number
print(x**2)

""" 
Sometimes when we're manipulating numbers, we want to work with the results again later on. 

All we did was print the results of our arithmetic. 

The python interpreter is really not that smart, it doesn't remember what it prints. So in order for 
python to remember what it did, you need to save it back into another variable (or itself)
"""
sum = x + y
print(sum)
""" 
So let's keep sum in mind and also add another variable to it. 

The equals sign is really just an assignment operator and not an equality operator.

common things that happen:
    - you'll have a variable that you need to update repeatedly
"""

sum = sum + 20 #This is perfectly valid 
""" 
Sum is a named place in memory

on the left hand side of the equals sign, we're declaring a variable
on the right hand side, we substitute the value of sum into where called it

sum = x + y 
    = 15

sum = sum + 20
      15 + 20
      
sum = 35 
"""
print(sum)

""" 
Strings of text: 

    - In other programming langauges, you have a data type specifically for single characters of text
    - In python, strings of text are all the same data type (string)
"""

name = "Jackson Sommerfeld"
#<name of the variable> = <attribute>
print(name)

#What if I want to print out "My name is <name>"

""" 
In python, we can do this in two ways. 

    - fstrings: format string and it lets specify placeholder values in strings so you can drop in variables
    
"""
print(f"My name is {name}")
print(f"the sum of x and y is {sum}")