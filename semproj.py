"Stat Tracker"
"""
import pygame
pygame.init()
WIDTH, HEIGHT = 1024, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stat Tracker")
"""

file = open("current_stats.txt","r")
buffer=file.readlines()
file.close()

kills = buffer[0].strip().split(",")
kills.pop(0)

deaths = buffer[1].strip().split(",")
deaths.pop(0)

wins = buffer[2].strip().split(",")
wins.pop(0)

losses = buffer[3].strip().split(",")
losses.pop(0)

for i in range(len(kills)):
    kills[i] = int(kills[i])
    deaths[i] = int(deaths[i])
    wins[i] = int(wins[i])
    losses[i] = int(losses[i])
    print(f"Kills:{kills}")
    print(f"Deaths:{deaths}")
    print(f"Wins:{wins}")
    print(f"Losses:{losses}")

gamertag = input("Enter your gamertag: ").strip()
check = False

while check == False:
    print(f"Hey {gamertag} what would you like to do?")
    print("1. Add wins or losses")
    print("2. Remove wins or losses")
    print("3. Add Games Played")

    option = input("Enter your selection: ").strip().lower()
    if option == "1":
        option = input("Are you adding: \n 1. Wins \n 2. Losses? ").strip()
        if option == "1" or "wins":
            option2 = float(input("How many did you get: "))
            try:
                index = kills.index(option)
                wins.append(option)
                losses.append(option2 * deaths[index])
                print(f"Added {option2} {option} to wins.")
            except ValueError:
                print("Item not found.")

            print("Current wins:", wins)
        
    elif option == "2":
        option = input("Enter option name to remove: ").strip()
        try:
            index = wins.index(option)
            wins.pop(index)
            losses.pop(index)
            print(f"Removed {option} from wins.")
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
line1 = f"kills: {kills}\n"
line2 = f"deaths: {deaths}\n"
line3 = f"Kill/Death Ratio: {killdeathratio}\n"
line4 = f"wins: {wins}\n"
line5 = f"Losses: {losses}\n"
line6 = f"Win/Loss Ratio: {winlossratio}\n"
buffer = [line0, line1, line2, line3]
file.writelines(buffer)
file.close()
