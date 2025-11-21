# Read file
file = open("food.txt", "r")
buffer = file.readlines()
file.close()

items = []
prices = []
cart = []        # items user selects
cart_prices = [] # matching prices

# Load items + prices from file
for line in buffer:
    line = line.strip().split(",")
    items.append(line[0])
    prices.append(float(line[1]))   # convert to number

print(items)
print(prices)

check = False

while check == False:
    print("Welcome to the grocery store. Please select your option:")
    print("1. Add to cart")
    print("2. Remove from cart")
    print("3. Checkout")

    option = input("Enter your selection: ").strip().lower()

    if option == "1":
        item_name = input("Enter Item Name: ").strip()

        if item_name in items:
            index = items.index(item_name)
            cart.append(item_name)
            cart_prices.append(prices[index])
            print(f"Added {item_name} to cart.")
        else:
            print("Item not found.")

        print("Current cart:", cart)

    elif option == "2":
        item_name = input("Enter Item Name to remove: ").strip()

        if item_name in cart:
            index = cart.index(item_name)
            cart.pop(index)
            cart_prices.pop(index)
            print(f"Removed {item_name} from cart.")
        else:
            print("Item not in cart.")

        print("Current cart:", cart)

    elif option == "3":
        check = True

        print("Receipt")
        for i in range(len(cart)):
            print(f"{cart[i]} - {cart_prices[i]}")

        subtotal = sum(cart_prices)
        statetax = 0.06
        tax = subtotal * statetax
        total = subtotal + tax
        print(f"Total: {total}")
        print("Thank You Come Again!")

    else:
        print("Invalid Option. Please Try again.")
