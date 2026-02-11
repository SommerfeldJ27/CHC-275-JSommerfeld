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
    print("Welcome to the List Statistics Calculator")
    print("Enter a list of integers or 'q' to end the list! ")
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

""" 
Function Name: printMenu
Parameters: none
Return Type: none
Description: Prints menu for statistics calculator
"""
def printMenu():
    print("Please choose the statistic you would like to calculate! ")
    print("1. Min")
    print("2. Max")
    print("3. Mean")
    print("4. Median")
    print("5. Clear List")

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

"""
Function Name: getMedian
Parameters: List
Return Type: Float
Description: Calculates the median for the list and returns the value  
"""
def getMedian(userList):
    userList = sorted(userList)
    length = len(userList)
    if length % 2 == 0:
        mid1 = userList[length // 2 - 1]
        mid2 = userList[length // 2]
        return (mid1 + mid2) / 2
    else:
        return userList[length // 2]

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

""" 
Function Name: getStdDev
Parameters: List
Return Type: Float
Description: Calculates the population Standard Deviation of a list
"""
def getStdDev(userList):
    mean = getMean(userList)
    n = len(userList)
    SSE = 0
    for current in userList:
        SSE = SSE + (current - mean) ** 2
    SSE = SSE / n
    return math.sqrt(SSE)

def main():
    myList = getList()
    if len(myList) == 0:
        print("The list is empty.")
        return
    while True:
        printMenu()
        option = input("Please enter your choice, or press 0 to exit:")
        if option == "0":
            print("Exiting")
            break
        elif option == "1":
            print("The minimum is:", getMin(myList))
        elif option == "2":
            print("The maximum is:", getMax(myList))
        elif option == "3":
            print("The mean is:", getMean(myList))
        elif option == "4":
            print("The median is:", getMedian(myList))
        elif option == "5":
            print("The standard deviation is:", getStdDev(myList))
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
