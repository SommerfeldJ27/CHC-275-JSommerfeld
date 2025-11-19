file = open("food.txt","r") #open("<filename>","<mode>") 
buffer = file.readlines() #this will take in our list of items and make each line an item inside our list 
items = [] #This would be account items
prices = [] #this would be total 
file.close() #flush the buffered memory being used for the contents of the files 
for line in buffer: #for each makes more sense here because we don't want to introduce
#index based technical overhead that is irrelevant to our program
    line = line.strip() #This removes white space
    line = line.split(",") #line is a list of two elements
                            #line[0] is the name
                            #line[1] is the grade value
    items.append(line[0])
    prices.append(line[1])

print(items)
print(prices)
cart = []

check = False

while check == False:
    print("Welcome to the grocery store. Please select your option:")
    print("1. Add to cart")
    print("2. Remove from cart")
    print("3. Checkout")

    option = input("Enter your selection: ").strip().lower()
    if (option == "1"):
        item = input("Enter Item:") #Name of new account
        cart.append(item) #Creates account name and adds to list
        for i in range(len(cart)):
            print(f"Cart {cart[i]}") #Prints results
    elif (option == "2"): #User input
        item = input("Enter Item:") #Account name being removed
        index = cart.append(item) #References back to Accounts list
        cart.pop(index) #Removes account
        for i in range(len(cart)):
            print(f"Account {cart[i]}") #Prints results
    elif (option == "3"):
        check = True
        print("Thank You Come Again!")