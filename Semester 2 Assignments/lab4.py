""" 
Name: Jackson Sommerfeld
Section: 275 - 2
Description: Lab 4 
"""

import math


"""
Function Name: getList
Parameters: none
Return Type: List
Description: Prompts user to fill in an empty list until they are satisfied 
"""
def getList():
    print("Enter a list of integers, or type 'q' to end the list! ")
    userList = []
    check = True
    while check == True:
        option = input("Enter an integer: ")
        if option == "q":
            check = False
        else:
            try: 
                number = int(option)
            except Exception as e:
                print(e)
            else: 
                userList.append(number)
    return userList

print(getList())

""" 
Function Name: printMenu
Parameters: none
Return Type: none
Description: Prints menu for statistics calculator
"""
def printMenu():
    print("Please choose the statistic you would like to calculate: ")
    print("1. Min")
    print("2. Max")
    print("3. Mean")
    print("4. Median")
    print("5. Clear List")
printMenu()
option = input("Enter your option: ")

"""
Function Name: getMean
Parameters: List
Return Type: Float
Description: Calculates the mean for the list and returns the value 
"""
def getMean(userList):
    sum = 0
    for i in range(len(userList)):
        sum = sum + userList[i]
    return sum / len(userList)

if option == "3":
    myList = getList()
    print(f"The mean is: {getMean(myList)}")

"""
Function Name: getMedian
Parameters: List
Return Type: Float
Description: Calculates the median for the list and returns the value  
"""
def getMedian(userList):
    userList = sorted(userList)

""" 
Function Name: getMin
Parameters: List
Return Type: Float
Description: Finds the minimum of the unsorted list
"""
def getMin(userList):
    min = userList[0]
    for i in range(len(userList)):
        if userList[i] < min:
            min = userList[i]
    return min

if option == "1":
    myList = getList()
    print(f"The minimum is: {getMin(myList)}")

""" 
Function Name: getMax
Parameters: List
Return Type: Float
Description: Finds the maximum of the unsorted list
"""
def getMax(userList):
    max = userList[0]
    for i in range(len(userList)):
        if userList[i] > max:
            max = userList[i]
    return max

if option == "2":
    myList = getList()
    print(f"The maximum is: {getMax(myList)}")

""" 
Function Name: getStdDev
Parameters: List
Return Type: none
Description: Calculates the population Standard Deviation of a list
"""
def getStdDev(userList):
    pass



def main():
    pass


if __name__ == "__main__":
    main()