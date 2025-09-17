"""
    - Sequential
    - Branching
    - Repetition

We are interested in repeating code blocks over and over again
"""

print(1)
print(1)
print(1)
print(1)
print(1)
print(1)
print(1)
print(1)
print(1)
print(1)
print(1)

"""
This already feels wrong and innefficient abd isn't really generalizable

There are 3 ways to repeat a code segment
    - While loops
    - For loops
    - Recursion
While loops are the easiest
"""


    
"""
Python Interpreter allocates partitions of RAM to two different collections
    - Stack: fixed ammount of memory for function calls and variable assignment
    - Heap: dynamic ammount of memory for complex gaming structures
"""
    
nums = [1,2,3,4,5,6,7,8,9,10]
x = 0
sum = 0
while x < len(nums):
        sum += nums[x]
        x +=1
print(f"the sum is {sum}")

check = False

while check == False:
    print("option 1")
    print("option 2")
    print("option 3")
    option = input("Select your option or type quit to exit: ")
    if option == "1":
        print(1)
    elif option == "2":
        print(2)
    elif option == "3":
        print(3)
    elif option == "quit":
        check = True
