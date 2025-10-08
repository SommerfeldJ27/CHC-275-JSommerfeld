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
                balances[index] = balances[index] - money #Formula to subtract money from balance
                for i in range(len(accounts)):
                    print(f"Account {accounts[i]} Balance {balances[i]}") #Prints results
        
    elif (option == "2"): #User input
        name = input("Which account are you transfering from: ") #Question based on input
        index = accounts.index(name) #Refrences back to Accoutns list
        money = input("How much would you like to transfer: ") #Question based on responce
        money = int(money) #Money holds value
        balances[index] = balances[index] - money #Formula to subtract money from balance
        name = input("Which account are you transfering to: ") #Follow up question
        index = accounts.index(name) #Refrences back to Accoutns list
        balances[index] = balances[index] + money #Formula to add money to balance
        for i in range(len(accounts)):
            print(f"Account {accounts[i]} Balance {balances[i]}") #Prints results
        
    elif (option == "3"): #User input
        for i in range(len(accounts)):
            print(f"Account {accounts[i]} Balance {balances[i]}") #Prints current accounts and balances
        
    elif (option == "4"): #User input
        print("Will you be adding or removing an account?") #Question based on input
        option = input("") #User response
        if (option == "Adding" or "adding"):#User input
                name = input("Enter Account Name:") #Name of new account
                accounts.append(name) #Creates account name and adds to list
                balance = input("Current Funds: ") #Current balance of new account
                balance = int(balance) #Creates balance and adds to list
        if (option == "Removing" or "remove"): #User input
                name = input("Enter Account Name:") #Account name being removed
                index = accounts.append(name) #References back to Accounts list
                accounts.pop(index) #Removes account
                balances.pop(index) #Removes account
                
    elif (option == "Quit" or "quit"): #User input
        check = True #Kills the code
        print("Thank you come again!") #Friendly exit to command line