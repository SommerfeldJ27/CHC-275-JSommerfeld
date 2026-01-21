        
print("What kind of fish do you have? ")
print("Carnivourous")
print("Salt Water")
print("Community")
option = input("Enter Fish Type: ")

if (option == "Carnivourous"):
    print("Do you already have it?")
    option = input("")
    if (option == "Yes"):
             print("Too bad")
    if (option == "No"):
            print("Enjoy")
elif (option == "Salt Water"):
    print("You're a fancy fish parent")
elif (option == "Community"):
    print("You should get more than one")
else:
    print("I don't think thats a kind of fish")