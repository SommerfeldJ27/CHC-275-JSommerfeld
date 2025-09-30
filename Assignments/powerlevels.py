num1 = input("Enter Robot 1's power level: ")
num1 = int(num1)
num2 = input("Enter Robot 2's power level: ")
num2 = int(num2)

if (num1 > num2):
    print("Robot 1 Wins")
if (num1 < num2):
    print("Robot 2 Wins")
if (num1 == num2):
    print("It's a tie")