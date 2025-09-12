"""
    we want keyboard input
    hardcoding values into programs is not exactly how we use computers
    we want some sort of input and output from the computer based on what the user does
    it prints the prompt into the terminal
    it scans the keyboard for input
    saves the input into a variable
    input what is the first number
    out objecxtibe is take two numbers and add trhem together
"""
numsix = input("enter your number ")
lorkeez = input("enter your second number ")
sum = numsix + lorkeez
print(f"The sum is {sum}")

"""
the user is going to type in

numsix = 10
lorkeez = 5
sum = numsix + lorkeez

what do you expecty to be printed. we expect 15

we got 105 that is not the right answer the thing is about input is when it scans the keyboard it assigns the variable to the string data type
the name
the data type
the attribute
numsix
the name numsix
string
"10"

you cannot do m,ath with stings we do smth called typecasting
typecasting reassigfns the datatype of the bariabnlew as long as its a valid target
numsix = "Jackson Sommerfeld" <- can't typecast
numsix = "10" <- I can typecast this
to change a string to a number
"""

numsix = input("enter your number ")
numsix = int(numsix)
    #int(variable name)
lorkeez = input("enter your second number ")
numsix = int(lorkeez)
sum = numsix + lorkeez
print(f"The sum is {sum}")