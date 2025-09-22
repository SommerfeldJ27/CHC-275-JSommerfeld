        
print("What kinda fishy do you have? ")
print("Carnivourous")
print("Salt Water")
print("Community")
option = input("Enter Fish Type: ")

if (option == "Carnivourous"):
    print("do you already have it?")
    option = input("")
    if (option == "yes"):
             print("too bad")
    if (option == "no"):
            print("enjoy")
elif (option == "salt water"):
    print("you're a fancy fish parent")
elif (option == "community"):
    print("you should get more than one")
else:
    print("i dont think thats a kind of fish")