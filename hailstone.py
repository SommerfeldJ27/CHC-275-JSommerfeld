"""
- Take any integer (x) (use input and typecasting )
-if it's odd you multiply it by 3 and add 1 (relevant skills % and if statements) (any odd number divided by 2 has a remainder of 1)
-if it's even, you divide by 2 (number mod 2 == 0)
"""

x = input("Enter a number: ")
x = int(x)
#top one
if x % 2 == 0:
    print(f"{x} is divisble by 2")
elif x % 2 == 1:
     print(f"{x} is divisble by 5")