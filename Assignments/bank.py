# Filename: bank.py
# Author: Jackson Sommerfeld
# Created: 10-8-2025
# Description: Create a working bank that deposits, withdraws, and tranfers money. Can add or remove accounts and list said accounts and balances.

#Inital accounts and balances for the bank to work with
accounts = ["Jackie", "Silverhand" , "Smasher", "Rogue", "V"]
balances = [1000, 2000, 3000, 4000, 5000]
check = False

while check == False:
    
    print("Welcome to FFCU! How can I help you today? ") #Prints prompt to welcome user
    print("1. Deposit or Withdraw") #Lists options
    print("2. Transfer Money") #Lists options
    print("3. List Accounts and Balances") #Lists options
    print("4. Add or Remove Accounts") #Lists options
    
    option = input("Select option or type quit to exit: ") #Allows user response
    
    if (option == "1"): #User input
        print("Will you be depositing or withdrawing funds?") #Question based on input
        option = input("") #Allows user response
        if (option == "Depositing" or "depositing"): #User input
                name = input("Which account are you depositing into: ") #Question based on response
                index = accounts.index(name) #Refrences back to Accoutns list
                money = input("How much would you like to deposit: ") #Follow up question
                money = int(money) #Money holds value
                balances[index] = balances[index] + money #Formula to add money to balance
                for i in range(len(accounts)):
                    print(f"Account {accounts[i]} Balance {balances[i]}") #Prints results
        option = input("") #Allows user response
        if (option == "Withdrawing" or "withdrawing"): #User input
                name = input("Which account are you withdrawing from: ") #Question based on response
                index = accounts.index(name) #Refrences back to Accounts list
                money = input("How much would you like to withdraw: ") #Follow up question
                money = int(money) #Money holds value
                balances[index] = balances[index] - money #Formula to add money to balance
                for i in range(len(accounts)):
                    print(f"Account {accounts[i]} Balance {balances[i]}") #Prints results
        
    elif (option == "2"):
        name = input("Which account are you transfering from: ")
        index = accounts.index(name)
        money = input("How much would you like to transfer: ")
        money = int(money)
        balances[index] = balances[index] - money
        name = input("Which account are you transfering to: ")
        index = accounts.index(name)
        balances[index] = balances[index] + money
        for i in range(len(accounts)):
            print(f"Account {accounts[i]} Balance {balances[i]}")
        
    elif (option == "3"):
        for i in range(len(accounts)):
            print(f"Account {accounts[i]} Balance {balances[i]}")
        
    elif (option == "4"):
        print("Will you be adding or removing an account?")
        option = input("")
        if (option == "Adding" or "adding"):
                name = input("Enter Account Name:")
                accounts.append(name)
                balance = input("Current Funds: ")
                balance = int(balance)
        if (option == "Removing" or "remove"):
                name = input("Enter Account Name:")
                index = accounts.append(name)
                accounts.pop(index)
                balances.pop(index)
                
    elif (option == "Quit" or "quit"):
        check = True
        print("Thank you come again!")