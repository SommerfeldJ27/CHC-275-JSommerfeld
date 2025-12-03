"Stat Tracker"
import pygame
pygame.init()
WIDTH, HEIGHT = 1024, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stat Tracker")

file = open("current_stats.txt","r")
buffer = file.readlines()
games_played = int(buffer[0].strip())
print(f"Games Played: {games_played}")
kills = []
deaths = []
killdeathratio = kills/deaths
wins = []
losses = []
winlossratio = wins/losses
file.close()

for line in buffer:
    line = line.strip().split(",")
    kills.append(float(line[0]))
    deaths.append(float(line[1]))

print(kills)
print(deaths)
print(kills / deaths)
gamertag = input("Enter your gamertag: ").strip()
check = False

while check == False:
    print(f"Hey {gamertag} what would you like to do?")
    print("1. Add wins or losses")
    print("2. Remove wins or losses")
    print("3. Add Games Played")

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
file_name = "new_stats.txt"
file = open(file_name,"w")
line0 = f"Games Played: {games_played}\n"
line1 = f"Kills: {kills}\n"
line2 = f"Deaths: {deaths}\n"
line3 = f"Kill/Death Ratio: {killdeathratio}\n"
line4 = f"Wins: {wins}\n"
line5 = f"Losses: {losses}\n"
line6 = f"Win/Loss Ratio: {winlossratio}\n"
buffer = [line0, line1, line2, line3]
file.writelines(buffer)
file.close()
