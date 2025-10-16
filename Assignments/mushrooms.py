"""
Asks for the size of a mushroom repeatedly until they type stop
Sorts each mushroom into three separate lists, small, medium, large
Small mushrooms are mushrooms less than 100 in size
Medium mushrooms are mushrooms between 100 and 200 in size
Large mushrooms are mushrooms greater than or equal to 200 in size.
Print out the lists of each sized mushroom.
"""
# Initialize empty lists for each mushroom size category
small_mushrooms = []
medium_mushrooms = []
large_mushrooms = []

while True:
    # Ask for mushroom size
    user_input = input("Enter mushroom size (or type 'stop' to finish): ").strip().lower()

    # Stop condition
    if user_input == "stop":
        break

    # Try to safely convert input to a number
    try:
        size = float(user_input)
    except ValueError:
        print("Invalid input! Please enter a number or type 'stop' to finish.")
        continue  # Skip to next iteration

    # Sort into correct list
    if size < 100:
        small_mushrooms.append(size)
    elif size < 200:
        medium_mushrooms.append(size)
    else:
        large_mushrooms.append(size)

# Print results
print("\nSmall mushrooms (< 100):", small_mushrooms)
print("Medium mushrooms (100–199):", medium_mushrooms)
print("Large mushrooms (≥ 200):", large_mushrooms)
