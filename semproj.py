"Stat Tracker"

file = open("current_stats.txt","r")
buffer=file.readlines()
file.close()

accounts = buffer[0].strip().split(":")
accounts.pop(0)
games_played = buffer[1].strip().split(":")
games_played.pop(0)
kills = buffer[2].strip().split(":")
kills.pop(0)
deaths = buffer[3].strip().split(":")
deaths.pop(0)
wins = buffer[4].strip().split(":")
wins.pop(0)
losses = buffer[5].strip().split(":")
losses.pop(0)

for i in range(len(accounts)):
    accounts[i] = accounts[i].strip().lower()
    games_played[i] = int(games_played[i])
    kills[i] = int(kills[i])
    deaths[i] = int(deaths[i])
    wins[i] = int(wins[i])
    losses[i] = int(losses[i])

print(f"Accounts: {accounts}")
print(f"Kills: {kills}")
print(f"Deaths: {deaths}")
print(f"Wins: {wins}")
print(f"Losses: {losses}")

check = False
check1 = False
check2 = False
check3 = False
check4 = False

while check == False:
    print(f"Hey Admin what would you like to do?")
    print("1. Add Stats")
    print("2. Remove Stats")
    print ("3. Add Accounts")
    print("4. Remove Accounts")
    print("5. Quit")

    option = input("Enter your selection: ").strip()
    if option == "1":
        print("Which account would you like to add stats to?")
        gamertag = input("Enter Account Name: ").strip().lower()
        if gamertag in accounts:
            index = accounts.index(gamertag)
        else:
            print("Account not found.")
            continue
        option = input("What would you like to add: \n 1. Wins \n 2. Losses \n Add: ").strip()
        if option == "1":
            try:
                option = int(input("How many wins did you get: "))
                wins[index]+= option
                games_played[index] += option
            except ValueError:
                print("Invalid input. Please enter a number.")
            print(f"Added {option} wins")
            while check1 == False:
                option = input("Did you get any kills?: ").strip().lower()
                if option == "y".strip().lower():
                    try:
                        option = int(input("How many kills did you get?: "))
                        kills[index]+= option
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                    print(f"Added {option} kills")
                    check1 = True
                elif option == "n".strip().lower():
                    print("No kills added.")
                    check1 = True
                else:
                    print("Invalid input.")
            while check2 == False:
                option = input("Did you die?: ").strip().lower()
                if option == "y".strip().lower():
                    try:
                        option = int(input("How many deaths did you have?: "))
                        deaths[index]+= option
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                    print(f"Added {option} deaths")
                    check2 = True
                elif option == "n".strip().lower():
                    print("No deaths added.")
                    check2 = True
                else:
                    print("Invalid input.")
        elif option == "2":
            try:
                option = int(input("How many losses did you get: "))
                losses[index]+= option
                games_played[index] += option
            except ValueError:
                print("Invalid input. Please enter a number.")
            print(f"Added {option} losses")
            while check3 == False:
                option = input("Did you get any kills?: ").strip().lower()
                if option == "y".strip().lower():
                    try:
                        option = int(input("How many kills did you get?: "))
                        kills[index]+= option
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                    print(f"Added {option} kills")
                    check3 = True
                elif option == "n".strip().lower():
                    print("No kills added.")
                    check3 = True
                else:
                    print("Invalid input.")
            while check4 == False:
                option = input("Did you die?: ").strip().lower()
                if option == "y".strip().lower():
                    try:
                        option = int(input("How many deaths did you have?: "))
                        deaths[index]+= option
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                    print(f"Added {option} deaths")
                    check4 = True
                elif option == "n".strip().lower():
                    print("No deaths added.")
                    check4 = True
                else:
                    print("Invalid input.")

    elif option == "2":
        print("which account would you like to remove stats from?")
        gamertag = input("Enter Account Name: ").strip().lower()
        if gamertag in accounts:
            index = accounts.index(gamertag)
        else:
            print("Account not found.")
            continue
        option = input("What would you like to remove: \n 1. Wins \n 2. Losses \n 3. Kills \n 4. Deaths \n Remove: ").strip()
        if option == "1":
            try:
                option = int(input("How wins would you like to remove: "))
                wins[index]-= option
                games_played[index] -= option
            except ValueError:
                print("Invalid input. Please enter a number.")
            print(f"Removed {option} wins")
        elif option == "2":
            try:
                option = int(input("How many losses would you like to remove: "))
                losses[index] -= option
                games_played[index] -= option
            except ValueError:
                print("Invalid input. Please enter a number.")
            print(f"Removed {option} Losses")
        elif option == "3":
            try:
                option = int(input("How many kills would you like to remove: "))
                kills[index] -= option
            except ValueError:
                print("Invalid input. Please enter a number.")
            print(f"Removed {option} kills")
        elif option == "4":
            try:
                option = int(input("How many deaths would you like to remove: "))
                deaths[index] -= option
            except ValueError:
                print("Invalid input. Please enter a number.")
            print(f"Removed {option} deaths")

    elif option == "3":
        gamertag = input("Enter Account Name:").strip().lower()
        accounts.append(gamertag)
        option = input("Would you like to enter base stats for this account: ").strip().lower()
        if option == "y".strip().lower():
            try:
                games_played_1 = int(input("Enter number of games played: "))
                games_played.append(games_played_1)
                wins_1 = int(input("Enter number of wins: "))
                wins.append(wins_1)
                losses_1 = int(input("Enter number of losses: "))
                losses.append(losses_1)
                kills_1 = int(input("Enter number of kills: "))
                kills.append(kills_1)
                deaths_1 = int(input("Enter number of deaths: "))
                deaths.append(deaths_1)
            except ValueError:
                print("Invalid input. Please enter a number.")
        if option == "n".strip().lower():
            print("No base stats added")
        else:
            print("Invalid input.")
            
    elif option == "4":
        gamertag = input("Which account are we deleting:").strip().lower()
        index = accounts.index(gamertag)
        accounts.pop(index)
        games_played.pop(index)
        wins.pop(index)
        losses.pop(index)
        kills.pop(index)
        deaths.pop(index)

    elif option == "5":
        check = True
        print("Exiting Stat Tracker")
        file_name = "new_stats.txt"
        file = open(file_name,"w")
        line0 = f"Accounts: {accounts}\n"
        line1 = f"Games Played: {games_played}\n"
        line2 = f"Kills: {kills}\n"
        line3 = f"Deaths: {deaths}\n"
        line4 = f"Wins: {wins}\n"
        line5 = f"Losses: {losses}\n"
        buffer = [line0, line1, line2, line3, line4, line5]
        file.writelines(buffer)
        file.close()
    else:
        print("Invalid option. Please try again.")

import pygame

pygame.init()
size = 600, 400
screen = pygame.display.set_mode((size))
pygame.display.set_caption("Stat Tracker")

file1 = open("current_stats.txt", "r")
buffer1 = file1.read().splitlines()
file1.close()

file2 = open("new_stats.txt", "r")
buffer2 = file2.read().splitlines()
file2.close()

font = pygame.font.SysFont(None, 30)
line_height = 35

running = True
while running:
    screen.fill((0, 0, 0))

    y = 50
    for line in buffer1:
        text_surface = font.render(line, True, (255, 255, 255))
        screen.blit(text_surface, (50, y))
        y += line_height

    y = 50
    for line in buffer2:
        text_surface = font.render(line, True, (255, 255, 255))
        screen.blit(text_surface, (250, y))
        y += line_height

    pygame.display.flip() #hi

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()