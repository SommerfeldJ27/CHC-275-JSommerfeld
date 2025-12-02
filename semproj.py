"Stat Tracker"
file = open("current_stats.txt","r")
buffer = file.readlines()
kills = []
deaths = []
wins = []
losses = []
file.close()

for line in buffer:
    line = line.strip()
    line = line.split(",")
    kills.append(line[0])
    deaths.append(float(line[1]))

print(kills)
print(deaths)

check = False

while check == False:
    print("Welcome to the grocery store. Please select your option:")
    print("1. Add to wins")
    print("2. Remove from wins")
    print("3. Checkout")

    option = input("Enter your selection: ").strip().lower()
    if option == "1":
        item = input("Enter item name: ").strip()
        quantity = float(input("How many would you like: "))
        try:
            index = kills.index(item)
            wins.append(item)
            losses.append(quantity * deaths[index])
            print(f"Added {quantity} {item} to wins.")
        except ValueError:
            print("Item not found.")

        print("Current wins:", wins)
        
    elif option == "2":
        item = input("Enter item name to remove: ").strip()
        try:
            index = wins.index(item)
            wins.pop(index)
            losses.pop(index)
            print(f"Removed {item} from wins.")
        except ValueError:
            print("Item not found.")

        print("Current wins:", wins)

    elif option == "3":
        check = True
        subtotal = sum(losses)
        statetax = 0.06
        tax = subtotal * statetax
        total = subtotal + tax
        print("Receipt:")
        print(f"{wins} - {losses}")
        print(f"Subtotal: {subtotal}")
        print(f"Tax: {tax}")
        print(f"Total: {total}")
        print("Thank You Come Again")
    else:
        print("Invalid Option")
avg_filename = "new_stats.txt"
file = open(avg_filename,"w")
line0 = f"MSFT: {"mean1"} , {"mean4"}\n"
line1 = f"AMZN: {"mean2"} , {"mean5"}\n"
line2 = f"NVDA: {":"} , {"mean6"}\n"
line3 = f"The best investments would be {""}"
buffer = [line0, line1, line2, line3]
file.writelines(buffer)
file.close()
