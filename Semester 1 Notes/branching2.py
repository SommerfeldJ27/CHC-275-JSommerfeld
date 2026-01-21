""" 
Branching2.py


Let's discuss from a software development standpoint how if-elifs can be used in a software design question.

When you launch a game you open to a main menu. We typically want some sort of main menu in our command line programs.

Whats an easy way to make a main menu? 

1. PRINT OUT ALL OF THE OPTIONS
2. TAKE IN KEYBOARD INPUT
3. USE IFs and ELIFs in order to select the option the user typed in. 

freshman get 5 dollars
sophomores get 7
juniors get 9
seniors get 11
"""

print("Welcome to the lunch loan program")
print("1. freshman")
print("2. sophomore")
print("3. junior")
print("4. senior")
option = input("Enter your grade level: ")

""" 
Your goal is to match the output to the option using ifs and elifs. 

"""

print("welcome to the lunch loan program")
print("1 Freshman")
print("2 Sophomore")
print("3 Junior")
print("4 Senior")
option = input("Enter your grade level: ")

if (option == "Freshman"):
    print("You get 5 dollars")
if (option == "Sophomore"):
    print("You get 7 dollars")
if (option == "Junior"):
    print("You get 9 dollars")
if (option == "Senior"):
    print("You get 11 dollars")