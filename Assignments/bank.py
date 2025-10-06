accounts = ["Smasher" , "Silverhand", "Rogue", "Jackie", "V"]
balances = [1000, 2000, 3000, 4000, 5000]
check = False

while check == False:
    for i in range(len(accounts)):
        print(accounts[i])
    for i in range(len(balances)):
        print(balances[i])
    print(f"Account {accounts[i]} Balance {balances[i]}")
    
    print("Welcome to FFCU! How can I help you today? ")
    print("1. Deposit or Withdraw")
    print("2. Transfer Money")
    print("3. List Accounts and Balances")
    print("4. Add or Remove Accounts")
    
    option = input("Select option or type quit to exit: ")
    
    if (option == "1"):
        print("Will you be depositing or withdrawing funds?")
        option = input("")
        if (option == "Depositing" or "depositing"):
                name = input("Which account are you depositing into: ")
                index = accounts.index(name)
                money = input("How much would you like to deposit: ")
                money = int(money)
                balances[index] = balances[index] + money
                print(accounts)
                print(balances)
        option = input("")
        if (option == "Withdrawing" or "withdrawing"):
                name = input("Which account are you withdrawing from: ")
                index = accounts.index(name)
                money = input("How much would you like to withdraw: ")
                money = int(money)
                balances[index] = balances[index] - money
                print(accounts)
                print(balances)
        
    elif (option == "2"):
        print("To who?") #This is a place holder f holor later
        
    elif (option == "3"):
        print(accounts)
        print(balances)
        
    elif (option == "4"):
        print("Will you be adding or removing an account?")
        option = input("")
        if (option == "Adding" or "adding"):
                name = input("Enter Account Name:")
                accounts.append(name)
                bal = input("Current Funds: ")
                bal = int(bal)
        if (option == "Removing" or "remove"):
                name = input("Enter Account Name:")
                index = accounts.append(name)
                accounts.pop(index)
                balances.pop(index)
                
    elif (option == "Quit" or "quit"):
        check = True