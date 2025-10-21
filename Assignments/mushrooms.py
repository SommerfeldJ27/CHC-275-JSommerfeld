"""
Asks for the size of a mushroom repeatedly until they type stop
Sorts each mushroom into three separate lists, small, medium, large
Small mushrooms are mushrooms less than 100 in size
Medium mushrooms are mushrooms between 100 and 200 in size
Large mushrooms are mushrooms greater than or equal to 200 in size.
Print out the lists of each sized mushroom.
"""
# Initialize empty lists for each mushroom size category
smallmushrooms = []
mediummushrooms = []
largemushrooms = []
check = False
while check == False:
    # Ask for mushroom size
    userinput = input("Enter mushroom size or type stop to finish: ").strip().lower()
    # Try to safely convert input to a number
    try:
        size = input()
    except ValueError:
        print("Invalid input! Please enter a number or type 'stop' to finish.")
        continue  # Skip to next iteration

    # Sort into correct list
    if size < 100:
        smallmushrooms.append(size)
    elif size > 100 and size < 200:
        mediummushrooms.append(size)
    elif size > 200:
        largemushrooms.append(size)
# Stop condition
    if userinput == "stop":
        check = True

# Print results
print("Small mushrooms", smallmushrooms)
print("Medium mushrooms", mediummushrooms)
print("Large mushrooms", largemushrooms)
