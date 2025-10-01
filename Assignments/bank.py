print("Welcome to FFCU! How can I help you today? ")
print("Deposit or Withdraw")
print("Transfer Money")
print("List Accounts and Balances")
print("Add or Remove Accounts")
option = input("")

if (option == "Deposit or Withdraw"):
    print("Will you be depositing or withdrawing funds?")
    option = input("")
    if (option == "Depositing"):
             print("Good idea") #This is a place holder for later
    if (option == "Withdrawing"):
            print("Enjoy") #This is a place holder for later
elif (option == "Tranfer Money"):
    print("To who?") #This is a place holder for later
elif (option == "List Accounts and Balances"):
    print("here they are") #This is a place holder for later
elif (option == "Add Account"):
    print("Hello Mr. Account") #This is a place holder for later
elif (option == "Remove Account"):
     print("Goodbye Mr. Account") #This is a place holder for later
     
name = ["James","Jack","John", "Paul"]
balance = [102,71,93,88]

for i in range(len(name)):
     print(f"Name: {name[i]} Balance: {balance[i]}") 