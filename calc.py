"""
Make a new file: calc.py

Make a four function calculator tyhat takes in two numbers PER operation

1) Take in two numbers
2) add thgem together
3) print the sum

1) take in two numbers (use input to save the numbers into vasriables)
2) subtract them
3) print the difference

Do this for all four math functions that we have

Use f-styrings, variables, input() and typecasting
"""
num1 = input("Enter num1 ")
num2 = input("Enter num2 ")
num1 = int(num1)
num2 = int(num2)
sum = num1 + num2
print(f"the sum of {num1} and {num2} is {sum}")

num3 = input("Enter num3 ")
num4 = input("Enter num4 ")
num3 = int(num3)
num4 = int(num4)
difference = num3 - num4
print(f"the difference of {num3} and {num4} is {difference}")

num5 = input("Enter num5 ")
num6 = input("Enter num6 ")
num5 = int(num5)
num6 = int(num6)
product = num5 * num6
print(f"the product of {num5} and {num6} is {product}")

num7 = input("Enter num7 ")
num8 = input("Enter num8 ")
num7 = int(num7)
num8 = int(num8)
quotient = num7 / num8
print(f"the quotient of {num7} and {num8} is {quotient}")