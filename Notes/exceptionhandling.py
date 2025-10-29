x = int(input("Enter Num 1: "))
y = int(input("Enter Num 2: "))
if (x == 0 and y != 0) or (x and y != 0):
    quotient = x/y
    print(quotient)
if x != 0 and y == 0:
    print("You Cannot Divide by 0")