accounts = ["Smasher" , "Silverhand", "Rogue", "Jackie", "V"]
balances = [1000, 2000, 3000, 4000, 5000]
check = False

while check == False:
    for i in range(len(accounts)):
        print(accounts[i])
    
    print("Welcome to FFCU! How can I help you today? ")
    print("1. Deposit or Withdraw")
    print("2. Transfer Money")
    print("3. List Accounts and Balances")
    print("4. Add or Remove Accounts")
    option = input("Select option or type quit to exit: ")
    if (option == "1"):
        print("Will you be depositing or withdrawing funds?")
        option = input("")
        if (option == "Depositing"):
                print("Good idea") #This is a place holder for later
        if (option == "Withdrawing"):
                print("Enjoy") #This is a place holder for later
    elif (option == "2"):
        print("To who?") #This is a place holder f holor later
    elif (option == "3"):
        print("here they are") #This is a place holder for later
    elif (option == "4"):
        print("Will you be adding or removing an account?")
        option = input("")
        if (option == "Adding"):
                name = input("Enter Account Name:")
                accounts.append(name)
                bal = input("Current Funds: ")
                bal = int(bal)
        if (option == "Removing"):
                name = input("Enter Account Name:")
                index = accounts.append(name)
                accounts.pop(index)
                balances.pop(index)
    elif (option == "Quit"):
        check = True