def makeList():
    nums = []
    while True:
        user_input = input("Enter a number (or type 'stop'): ")
        
        if user_input.lower() == "stop":
            break
        else:
            nums.append(int(user_input))
    
    return nums

list1 = makeList()
print(list1)

list2 = makeList()
print(list2)
