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

games_played = buffer[0].strip().split(":")
games_played.pop(0)
kills = buffer[1].strip().split(",")
kills.pop(0)
deaths = buffer[2].strip().split(",")
deaths.pop(0)
wins = buffer[3].strip().split(",")
wins.pop(0)
losses = buffer[4].strip().split(",")
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
    print("1. Add Stats")
    print("2. Remove Stats")
    print("3. Quit")
    games_played = sum(wins) + sum(losses)
    killdeathratio = sum(kills) / sum(deaths)
    winlossratio = sum(wins) / sum(losses)

    option = input("Enter your selection: ").strip().lower()
    if option == "1":
        option = input("What would you like to add: \n 1. Wins \n 2. Losses \n Add: ").strip()
        if option == "1":
            try:
                option = float(input("How many wins did you get: "))
                index = len(wins) - 1
                wins[index]+= option
            except ValueError:
                print("Invalid input. Please enter a number.")
            print(f"Added {option} wins")
            option = input("Did you get any kills?: ")
            if option == "y":
                try:
                    option = float(input("How many kills did you get?: "))
                    index = len(kills) - 1
                    kills[index]+= option
                except ValueError:
                    print("Invalid input. Please enter a number.")
                print(f"Added {option} kills")
            elif option == "n":
                print("No kills added.")
            option = input("Did you die?: ")
            if option == "y":
                try:
                    option = float(input("How many deaths did you have?: "))
                    index = len(deaths) - 1
                    deaths[index]+= option
                except ValueError:
                    print("Invalid input. Please enter a number.")
                print(f"Added {option} deaths")
            elif option == "n":
                print("No deaths added.")
        elif option == "2":
            try:
                option = float(input("How many losses did you get: "))
                index = len(losses) - 1
                losses[index]+= option
            except ValueError:
                print("Invalid input. Please enter a number.")
            print(f"Added {option} losses")
            option = input("Did you get any kills?: ")
            if option == "y":
                try:
                    option = float(input("How many kills did you get?: "))
                    index = len(kills) - 1
                    kills[index]+= option
                except ValueError:
                    print("Invalid input. Please enter a number.")
                print(f"Added {option} kills")
            elif option == "n":
                print("No kills added.")
            option = input("Did you die?: ")
            if option == "y":
                try:
                    option = float(input("How many deaths did you have?: "))
                    index = len(deaths) - 1
                    deaths[index]+= option
                except ValueError:
                    print("Invalid input. Please enter a number.")
                print(f"Added {option} deaths")
            elif option == "n":
                print("No deaths added.")
    elif option == "2":
        option = input("What would you like to remove: \n 1. Wins \n 2. Losses \n 3. Kills \n 4. Deaths \n Remove: ").strip()
        if option == "1":
            try:
                option = float(input("How wins would you like to remove: "))
                index = len(wins) - 1
                wins[index]-= option
            except ValueError:
                print("Invalid input. Please enter a number.")
            print(f"Removed {option} wins")
        elif option == "2":
            try:
                option = float(input("How many losses would you like to remove: "))
                index = len(losses) - 1
                losses[index] -= option
            except ValueError:
                print("Invalid input. Please enter a number.")
            print(f"Removed {option} Losses")
        elif option == "3":
            try:
                option = float(input("How many kills would you like to remove: "))
                index = len(kills) - 1
                kills[index] -= option
            except ValueError:
                print("Invalid input. Please enter a number.")
            print(f"Removed {option} kills")
        elif option == "4":
            try:
                option = int(input("How many deaths would you like to remove: "))
                index = len(deaths) - 1
                deaths[index] -= option
            except ValueError:
                print("Invalid input. Please enter a number.")
            print(f"Removed {option} deaths")
    elif option == "3":
        check = True
        print("Exiting Stat Tracker")
        file_name = "new_stats.txt"
        file = open(file_name,"w")
        line0 = f"Games Played: {games_played}\n"
        line1 = f"Kills: {kills}\n"
        line2 = f"Deaths: {deaths}\n"
        line3 = f"Kill/Death Ratio: {killdeathratio}\n"
        line4 = f"Wins: {wins}\n"
        line5 = f"Losses: {losses}\n"
        line6 = f"Win/Loss Ratio: {winlossratio}\n"
        buffer = [line0, line1, line2, line3, line4, line5, line6]
        file.writelines(buffer)
        file.close()
    else:
        print("Invalid option. Please try again.")