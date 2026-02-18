#exprogram.py

"""
We're going to implement a four function calculator using def main and functions.

It's best practice to define all of our functions at the top of the file, and have the code 
we actually expect to execute at the bottom. When you are developing, there's a keyword called pass
that allows you to put placeholders in your code
"""


def add(x,y):
    return x + y
    
def subtract(x,y):
    return x - y
    
def multiply(x,y): 
    return x * y

def divide(x,y):
    return x / y

def pow(x,y):
    return x**y

def main():
    print("Welcome to the calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power ")
    check = True
    while check == True:
        option = input("Select your operation or type quit to exit: ")
        if option == "1":
            #inputting our numbers
            num1 = input("enter num1: ")
            num2 = input("enter num2: ")
            try: #typecasting to an int 
                num1 = int(num1)
                num2 = int(num2)
            except Exception as e:
                print(e)
            finally:
                #add the numbers if the typecast succeeds
                sum = add(num1,num2)
                print(f"your sum is: {sum}")
                
        if option == "2":
            #inputting our numbers
            num1 = input("enter num1: ")
            num2 = input("enter num2: ")
            try: #typecasting to an int 
                num1 = int(num1)
                num2 = int(num2)
            except Exception as e:
                print(e)
            finally:
                #add the numbers if the typecast succeeds
                sum = subtract(num1,num2)
                print(f"your difference is: {sum}")
                
        if option == "3":
            #inputting our numbers
            num1 = input("enter num1: ")
            num2 = input("enter num2: ")
            try: #typecasting to an int 
                num1 = int(num1)
                num2 = int(num2)
            except Exception as e:
                print(e)
            finally:
                #add the numbers if the typecast succeeds
                sum = multiply(num1,num2)
                print(f"your product is: {sum}")
                
        if option == "4":
            #inputting our numbers
            num1 = input("enter num1: ")
            num2 = input("enter num2: ")
            try: #typecasting to an int 
                num1 = int(num1)
                num2 = int(num2)
            except Exception as e:
                print(e)
            finally:
                #add the numbers if the typecast succeeds
                sum = divide(num1,num2)
                print(f"your quotient is: {sum}")
                
        if option == "5":
            #inputting our numbers
            num1 = input("enter num1: ")
            num2 = input("enter num2: ")
            try: #typecasting to an int 
                num1 = int(num1)
                num2 = int(num2)
            except Exception as e:
                print(e)
            finally:
                #add the numbers if the typecast succeeds
                sum = pow(num1,num2)
                print(f"your result is: {sum}")
        
            
        if option == "quit":
            check = False
            
if __name__ == "__main__": #two underscorees on both sides of name and main
    main()