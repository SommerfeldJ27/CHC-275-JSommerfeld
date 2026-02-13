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
    if len(userList) % 2 == 0:
        median = (userList[len(userList) // 2 - 1] + userList[len(userList) // 2]) / 2
    else:
        median = userList[len(userList) // 2]
    return median

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
Return Type: none
Description: Calculates the population Standard Deviation of a list
"""
def getStdDev(userList):
    mean = getMean(userList)
    n = len(userList)
    SSE = 0
    for i in range(len(userList)):
        SSE = SSE + (userList[i] - mean) ** 2
    SSE = SSE / n
    return math.sqrt(SSE)

def main():
    userList = getList()
    check = False
    while check == False:
        printMenu()
        option = input("Enter the number of the statistic you would like to calculate: ")
        if option == "1":
            print(f"The minimum of the list is {getMin(userList)}")
        elif option == "2":
            print(f"The maximum of the list is {getMax(userList)}")
        elif option == "3":
            print(f"The mean of the list is {getMean(userList)}")
        elif option == "4":
            print(f"The median of the list is {getMedian(userList)}")
        elif option == "5":
            print(f"The standard deviation of the list is {getStdDev(userList)}")
            check = True
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()