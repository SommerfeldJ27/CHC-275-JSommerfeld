"Stat Tracker"

file = open("current_stats.txt","r")
buffer=file.readlines()
file.close()

accounts = buffer[2].strip().split(":")
accounts.pop(0)
games_played = buffer[3].strip().split(":")
games_played.pop(0)
kills = buffer[4].strip().split(":")
kills.pop(0)
deaths = buffer[5].strip().split(":")
deaths.pop(0)
wins = buffer[6].strip().split(":")
wins.pop(0)
losses = buffer[7].strip().split(":")
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
        option1 = input("What would you like to add: \n 1. Wins \n 2. Losses \n Add: ").strip()
        if option1 == "1":
            try:
                option2 = int(input("How many wins did you get: "))
                wins[index]+= option2
                games_played[index] += option2
            except ValueError:
                print("Invalid input. Please enter a number.")
            print(f"Added {option} wins")
            while check1 == False:
                option3 = input("Did you get any kills?: ").strip().lower()
                if option3 == "y".strip().lower():
                    try:
                        option4 = int(input("How many kills did you get?: "))
                        kills[index]+= option4
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                    print(f"Added {option4} kills")
                    check1 = True
                elif option3 == "n".strip().lower():
                    print("No kills added.")
                    check1 = True
                else:
                    print("Invalid input.")
            while check2 == False:
                option5 = input("Did you die?: ").strip().lower()
                if option5 == "y".strip().lower():
                    try:
                        option6 = int(input("How many deaths did you have?: "))
                        deaths[index]+= option6
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                    print(f"Added {option6} deaths")
                    check2 = True
                elif option5 == "n".strip().lower():
                    print("No deaths added.")
                    check2 = True
                else:
                    print("Invalid input.")
        elif option == "2":
            try:
                option7 = int(input("How many losses did you get: "))
                losses[index]+= option7
                games_played[index] += option7
            except ValueError:
                print("Invalid input. Please enter a number.")
            print(f"Added {option7} losses")
            while check3 == False:
                option8 = input("Did you get any kills?: ").strip().lower()
                if option8 == "y".strip().lower():
                    try:
                        option9 = int(input("How many kills did you get?: "))
                        kills[index]+= option9
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                    print(f"Added {option9} kills")
                    check3 = True
                elif option8 == "n".strip().lower():
                    print("No kills added.")
                    check3 = True
                else:
                    print("Invalid input.")
            while check4 == False:
                option10 = input("Did you die?: ").strip().lower()
                if option10 == "y".strip().lower():
                    try:
                        option11 = int(input("How many deaths did you have?: "))
                        deaths[index]+= option11
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                    print(f"Added {option11} deaths")
                    check4 = True
                elif option10 == "n".strip().lower():
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
        option12 = input("What would you like to remove: \n 1. Wins \n 2. Losses \n 3. Kills \n 4. Deaths \n Remove: ").strip()
        if option12 == "1":
            try:
                option13 = int(input("How wins would you like to remove: "))
                wins[index]-= option13
                games_played[index] -= option13
            except ValueError:
                print("Invalid input. Please enter a number.")
            print(f"Removed {option13} wins")
        elif option12 == "2":
            try:
                option14 = int(input("How many losses would you like to remove: "))
                losses[index] -= option14
                games_played[index] -= option14
            except ValueError:
                print("Invalid input. Please enter a number.")
            print(f"Removed {option14} Losses")
        elif option12 == "3":
            try:
                option15 = int(input("How many kills would you like to remove: "))
                kills[index] -= option15
            except ValueError:
                print("Invalid input. Please enter a number.")
            print(f"Removed {option15} kills")
        elif option12 == "4":
            try:
                option16 = int(input("How many deaths would you like to remove: "))
                deaths[index] -= option16
            except ValueError:
                print("Invalid input. Please enter a number.")
            print(f"Removed {option16} deaths")

    elif option == "3":
        gamertag = input("Enter Account Name:").strip().lower()
        accounts.append(gamertag)
        option17 = input("Would you like to enter base stats for this account: ").strip().lower()
        if option17 == "y".strip().lower():
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
        if option17 == "n".strip().lower():
            games_played.append(0)
            wins.append(0)
            losses.append(0)
            kills.append(0)
            deaths.append(0)
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
        print(f"Account: {gamertag} has been deleted")

    elif option == "5":
        check = True
        print("Exiting Stat Tracker")
        file_name = "new_stats.txt"
        file = open(file_name,"w")
        line0 = f"New Stats:\n"
        line1 = f"----------------------\n"
        line2 = f"Accounts: {accounts}\n"
        line3 = f"Games Played: {games_played}\n"
        line4 = f"Kills: {kills}\n"
        line5 = f"Deaths: {deaths}\n"
        line6 = f"Wins: {wins}\n"
        line7 = f"Losses: {losses}\n"
        buffer = [line0, line1, line2, line3, line4, line5, line6, line7]
        file.writelines(buffer)
        file.close()
    else:
        print("Invalid option. Please try again.")

import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400)) #Screen Size
pygame.display.set_caption("Stat Tracker") #Name of Window

font = pygame.font.SysFont(None, 30) #Set Font and Size

file1 = open("current_stats.txt", "r")
buffer1 = file1.read().splitlines()
file1.close()

file2 = open("new_stats.txt", "r")
buffer2 = file2.read().splitlines()
file2.close()

running = True
while running:
    screen.fill((0, 0, 0)) #Set Background Color
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    y = 50 #Set First Line Height
    for line in buffer1:
        text_surface = font.render(line, True, (255, 255, 255)) #Color and Render Text
        screen.blit(text_surface, (50, y)) #Positions the Text Box
        y += 35 #Spacing in Between Lines

    y = 50 #Set First Line Height
    for line in buffer2:
        text_surface = font.render(line, True, (255, 255, 255)) #Color and Render Text
        screen.blit(text_surface, (350, y)) #Positions the Text Box
        y += 35

    pygame.display.flip()
pygame.quit()