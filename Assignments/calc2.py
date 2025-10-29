check = False
while check == False:
    option = input("Please Select Preferred Function or Type 'Quit' To Exit: ")
if option == ("Add").strip().lower():
    num1 = int(input("Enter Num 1"))
    num2 = int(input("Enter Num 2"))
    sum = num1 + num2
    print(f"the sum of {num1} and {num2} is {sum}")
elif option == ("Subtract").strip().lower():
    num3 = int(input("Enter Num 3"))
    num4 = int(input("Enter Num 4"))
    difference = num3 - num4
    print(f"the difference of {num3} and {num4} is {difference}")
elif option == ("Multiplication").strip().lower():
    num5 = int(input("Enter Num 5"))
    num6 = int(input("Enter Num 6"))
    product = num5 * num6
    print(f"the product of {num5} and {num6} is {product}")
elif option == ("Divide").strip().lower():
    num7 = int(input("Enter Num 7"))
    num8 = int(input("Enter Num 8"))
    if (num7 == 0 and num8 != 0) or (num7 and num8 != 0):
        quotient = num7/num8
        print(quotient)
    if num7 != 0 and num8 == 0:
        print("You Cannot Divide by 0")
elif option == ("Quit"):
    check == True