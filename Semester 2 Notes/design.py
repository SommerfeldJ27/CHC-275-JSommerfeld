#design.py

"""
WE now have programmer implemented functions, the problem is now that we are jumping up and down within our file, the organization
of our file is no longer obvious to us. 

When we use user implemented functions, we are noww jumping around our file to where the function headers are. 

We are interested in a file layout that is
    1) readable
    2) exposes all of the user implemented functions right as the interpreter starts executing code
        exposed = the function is able to be called
        
Here are our requirements as software engineers:
    1) all of functions to be exposed to us
    2) don't want code being executed inline with function definitions
    
How should we lay out our file when we start a project? 
    - Function definitions at the top
    - Code to be evaluated at the bottom
    
We can think of functions as services that we can use at the bottom of our file. 

we want to introduce a new structure that is relevant to pretty much all other coding languages. This structure is called
the main function
"""

import functions #this functions file is the notes file from last cycle

def foo():
    print("bar")
    
def fizz(x):
    if x % 2 == 1: #check if x is even or odd
        print("buzz")
        
#---------------------------------^ functions we want to use

def main(): #main is a special kind of function, this only gets evaluated if the parent file is the being executed
            #i'll expound upon this later.



    x = 5
    functions.add5(x)
    check = True
    while check == True:
        print("Welcome to our test program")
        print("1. foo")
        print("2. fizz")
        print("type quit to quit")
        option = input("Enter your option: ")
        if option == "1":
            foo()
        if option == "2":
            number = input("What is your number: ")
            try: 
                number = int(number) #immutability is why this design pattern is the way it is
            except Exception as e:
                print(e)
            else: 
                fizz(number)
        if option == "quit":
            check = False


"""
to call the main function, we need to do a convoluted process in an if statement 
"""


if __name__ == "__main__": #this is something you want memorized
                           #double underscore around name and main, and main is a string
    main()
    
""" 
The first reason is we can collect all of our variables in one obvious scope 

The second reason is the import keyword. Any python file can be imported into another python file. 
"""