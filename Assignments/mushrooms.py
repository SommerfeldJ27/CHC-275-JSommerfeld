"""
Asks for the size of a mushroom repeatedly until they type stop
Sorts each mushroom into three separate lists, small, medium, large
Small mushrooms are mushrooms less than 100 in size
Medium mushrooms are mushrooms between 100 and 200 in size
Large mushrooms are mushrooms greater than or equal to 200 in size.
Print out the lists of each sized mushroom.
"""
# Initial lists for each mushroom size category
small_mushrooms = []
medium_mushrooms = []
large_mushrooms = []

check = False
while check == False:
    # Ask for mushroom size
    size = input("Enter mushroom size or type 'stop' to exit: ").strip().lower()

    # Stop condition
    if size == "stop":
        check = True
        
    if size.isnumeric():
        size = int(size)
        if size < 100:
            small_mushrooms.append(size)
        elif size > 99 and size < 199:
            medium_mushrooms.append(size)
        else:
            large_mushrooms.append(size)
    print("Small mushrooms", small_mushrooms)
    print("Medium mushrooms", medium_mushrooms)
    print("Large mushrooms", large_mushrooms)
