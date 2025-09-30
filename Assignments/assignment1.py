"""
Assignment 1




Problem 1: hailstone.py

The hailstone problem (collatz conjecture) is an open problem in the field of number theory in math.

(all of this is inside of a while loop.) (exit condition  == 1)
 - Take any integer (x) (use input and typecasting )
 - if it's odd you multiply it by 3 and add 1 (relevant skills % and if statements) (any odd number divided by 2 has a remainder of 1)
 - if it's even, you divide by 2 (number mod 2 == 0)
 
The problem statement is:

- every number eventually ends in a loop of 4-2-1


67 after 3*67+1
202 after 101
304 after 152
152 after 76
76 after 38
38 after 19
19 odd 58
58


your goal, using while loops and an int variable, print out the path a number takes to hit the 4-2-1



problem 2: fish.py

if-elif-else problem:

you have one type of fish (carnivorous, salt water, community).

you want the user to describe what kind of fish they have.
    If its carniviorous
        - ask if they already have it
        if they already have it,
            - print too bad
        - if they dont
            - print enjoy
    elif  its salt water
        print you're a fancy fish parent
    elif community
        print you should get more than one
    else
        print i dont think thats a kind of fish




problem 3: powerlevels.py

take in two numbers,

if the first number is bigger than the second one, print num 1 wins
if the second number is bigger, print num 2 wins
if theyre equal print that its a tie


"""