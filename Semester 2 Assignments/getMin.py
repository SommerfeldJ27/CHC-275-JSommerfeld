def getMin(userList):
    min = userList[0]
    for i in range(len(userList)):
        if userList[i] < min:
            min = userList[i]
    return min

first = [1,2,3,4]
print(first)
print(f"minimum of first list {getMin(first)}")

second = [4,2,1,3]
print(second)
print(f"minimum of second list {getMin(second)}")