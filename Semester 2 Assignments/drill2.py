def makeList():
    nums = []
    check = False
    while check == False:
        option = input("Enter a number or type stop to finish: ").strip()

        if option.strip().lower() == "stop":
            check == True
            return nums
        else:
            nums.append(int(option))

list1 = makeList()
print(list1)
list2 = makeList()
print(list2)