"""
Asks for the size of a mushroom repeatedly until they type stop
Sorts each mushroom into three separate lists, small, medium, large
Small mushrooms are mushrooms less than 100 in size
Medium mushrooms are mushrooms between 100 and 200 in size
Large mushrooms are mushrooms greater than or equal to 200 in size.
Print out the lists of each sized mushroom.
"""
smallmushrooms = [""]
mediummushrooms = [""]
largemushrooms = [""]
check = False

while check == False:
    #Print general layout of welcome and options for the user
    print("Welcome to Mushroom Masters! How can I help you?")
    mushroom = input("Please Enter Mushroom Size: ") #Name of new account
    smallmushrooms.append(mushroom) #Creates account name and adds to list
    if mushroom < 100:
        print("This is a Small Mushroom")
        for i in range(len(smallmushrooms)):
                print(f"Account {smallmushrooms[i]}") #Prints results
    if (mushroom > 99 and mushroom < 199):
        print("This is a Medium Mushroom")
    if mushroom > 199:
        print("This is a Large Mushroom")
    elif (mushroom == "Stop" or "stop"): #User input
        check = True #Kills the code
        print("Thank You!") #Friendly exit to command line