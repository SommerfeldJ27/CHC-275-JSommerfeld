check = False
while check == False:
    print("What kind of fish do you have? ")
    print("Carnivourous")
    print("Salt Water")
    print("Community")
    option = input("Enter Fish Type: ")

    if (option == "Carnivourous"):
        print("Do you already have it?")
    option = input("")
    if (option == "Yes"):
             print("H1")
    if (option == "No"):
            print("OOPS")
    elif (option == "Salt Water"):
        print("PP")
    elif (option == "Community"):
        print("0!")
    else:
        check = True
        print("I don't think thats a kind of fish")
