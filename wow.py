
stats = []

def load_stats():
    try:
        with open("stats.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                # File format: game|kills|wins|hours
                parts = line.split("|")
                game_name = parts[0]
                kills = int(parts[1])
                wins = int(parts[2])
                hours = float(parts[3])

                stats.append({
                    "game": game_name,
                    "kills": kills,
                    "wins": wins,
                    "hours": hours
                })
    except FileNotFoundError:
        # If file doesn't exist, start with empty stats
        pass


# --------------------------------------------
# Save stats to file
# --------------------------------------------
def save_stats():
    with open("stats.txt", "w") as file:
        for entry in stats:
            line = f"{entry['game']}|{entry['kills']}|{entry['wins']}|{entry['hours']}\n"
            file.write(line)
    print("Stats saved successfully!\n")


# --------------------------------------------
# Add a new game
# --------------------------------------------
def add_game():
    game_name = input("Enter the name of the game: ")
    stats.append({
        "game": game_name,
        "kills": 0,
        "wins": 0,
        "hours": 0.0
    })
    print(f"Game '{game_name}' added!\n")


# --------------------------------------------
# Update stats for an existing game
# --------------------------------------------
def update_stats():
    if len(stats) == 0:
        print("No games added yet.\n")
        return

    print("\nWhich game would you like to update?")
    for i in range(len(stats)):
        print(f"{i + 1}. {stats[i]['game']}")

    try:
        choice = int(input("Enter the number of the game: ")) - 1
        if choice < 0 or choice >= len(stats):
            print("Invalid choice.\n")
            return
    except ValueError:
        print("Please enter a valid number.\n")
        return

    game = stats[choice]
    print(f"\nUpdating stats for {game['game']}")

    # Typecasting user input
    try:
        new_kills = int(input("Enter kills: "))
        new_wins = int(input("Enter wins: "))
        new_hours = float(input("Enter hours played: "))
    except ValueError:
        print("Invalid number entered. Stats not updated.\n")
        return

    # Update dictionary
    game["kills"] = new_kills
    game["wins"] = new_wins
    game["hours"] = new_hours

    print("Stats updated successfully!\n")


# --------------------------------------------
# Display all stats
# --------------------------------------------
def view_stats():
    if len(stats) == 0:
        print("No stats to display.\n")
        return

    print("\n=== All Game Stats ===")
    for entry in stats:
        print(f"Game: {entry['game']}")
        print(f"  Kills: {entry['kills']}")
        print(f"  Wins: {entry['wins']}")
        print(f"  Hours Played: {entry['hours']}")
        print("-----------------------------")
    print()


# --------------------------------------------
# MAIN PROGRAM LOOP
# --------------------------------------------
load_stats()

while True:
    print("=== Video Game Stat Tracker ===")
    print("1. Add a new game")
    print("2. Add/Update stats for a game")
    print("3. View all stats")
    print("4. Save stats")
    print("5. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_game()
    elif choice == "2":
        update_stats()
    elif choice == "3":
        view_stats()
    elif choice == "4":
        save_stats()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
