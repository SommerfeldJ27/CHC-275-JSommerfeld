""" 
variables2.py

We want keyboard input.

Hardcoding values into programs is not exactly how we use computers
we want some sort of input and output from the computer based on what the user does. 

For example, if we wanted to have a calculator, we would want the user to be able to 
choose the numbers to be added before runtime. Thankfully in python, doing this is relatively easy

there is an entire function in python dedicated to keyboard input 

input(<prompt>) <= this function does 3 things

    1) It prints the prompt into the terminal
    2) It scans the keyboard for input
    3) Saves the input into a variable
    
input("what is the first number")

Our objective is: take two numbers and add them together
"""

""" 
The user is going type in 

numsix = 10
lorkeez = 5
sum = numsix + lorkeez

what do you expect to be printed. we expect 15

We got 105, that is not the right answer. The thing is about input, is when it scans the keyboard it
assigns the variable to the string data type

Variables have 3 pieces of information
    1) The name
    2) The data type 
    3) The attribute 
    
numsix 
    1) the name numsix
    2) String
    3) "10" 
    
You cannot do math with strings. We do something called typecasting

Typecasting = Reassigning the datatype of the variable as long as its a valid target 

numsix = "Jackson Sommerfeld" <- i want to typecast this into a number 
numsix = "10" <- I can typecast 

to change a str -> int


"""


numsix = input("Enter your number ")
numsix = int(numsix)
        #int(variable name) <= will typecast your variable into integer (as long as its allowed)
lorkeez = input("Enter your second number ")
lorkeez = int(lorkeez)
        #now numsix and lorkeez are both of datatype integer (They are both numbers!)
sum = numsix + lorkeez
print(f"The sum is {sum}")

""" 
input() ALWAYS gives a string -> You need to typecast this into the correct datatype that you're expecting


"""