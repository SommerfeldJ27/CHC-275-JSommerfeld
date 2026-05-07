""" 
Make a new file: calc.py

Make a four function calculator that takes in two numbers PER operation

1) Take in two numbers
2) add them together
3) print the sum

1) take in two numbers (use input to save the numbers into variables)
2) Subtract them
3) print the difference 

Do this for all four math functions that we have 

Use f-strings, variables, input() and typecasting 

+ - * /
""" 
num1 = input("Enter num 1: ")
num2 = input("Enter num 2: ")
num1 = int(num1)
num2 = int(num2)
sum = num1 + num2
print(f"The sum of {num1} and {num2} is {sum}")