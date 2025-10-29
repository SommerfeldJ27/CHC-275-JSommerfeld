check = False
while check == False:
    option = input("Please Select Preferred Function or Type 'Quit' To Exit")
if option == ("Add").strip().lower():
    num1 = input("Enter num1 ")
    num2 = input("Enter num2 ")
    num1 = int(num1)
    num2 = int(num2)
    sum = num1 + num2
    print(f"the sum of {num1} and {num2} is {sum}")
if option == ("Subtract").strip().lower():
    num3 = input("Enter num3 ")
    num4 = input("Enter num4 ")
    num3 = int(num3)
    num4 = int(num4)
    difference = num3 - num4
    print(f"the difference of {num3} and {num4} is {difference}")
if option == ("Multiplication").strip().lower():
    num5 = input("Enter num5 ")
    num6 = input("Enter num6 ")
    num5 = int(num5)
    num6 = int(num6)
    product = num5 * num6
    print(f"the product of {num5} and {num6} is {product}")
if option == ("Divide").strip().lower():
    num7 = input("Enter num7 ")
    num8 = input("Enter num8 ")
    num7 = int(num7)
    num8 = int(num8)
    quotient = num7 / num8
    print(f"the quotient of {num7} and {num8} is {quotient}")
if option == ("Quit"):
    check == True