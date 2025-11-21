file = open("food.txt","r")
buffer = file.readlines()
items = []
prices = []
file.close()

for line in buffer:
    line = line.strip()
    name, price = line.split(",")
    items.append(name)
    prices.append(price)

print(items)
print(prices)

cart = []
check = False

while check == False:
    print("Welcome to the grocery store. Please select your option:")
    print("1. Add to cart")
    print("2. Remove from cart")
    print("3. Checkout")

    option = input("Enter your selection: ").strip()

    if option == "1":
        print("Available Items:")
        for i in range(len(items)):
            print(f"{items[i]} - {prices[i]}")

        item = input("Enter item name to add: ").strip()
        if item in items:
            cart.append(item)
            print(f"Added {item} to cart.")
        else:
            print("Item not found.")

        print("Current Cart:")
        for i in cart:
            print(cart)

    elif option == "2":
        item = input("Enter item name to remove: ").strip()
        if item in cart:
            cart.remove(item)
            print(f"Removed {item}.")
        else:
            print("Item not in cart.")

        print("Current Cart:")
        for i in cart:
            print(cart)

    elif option == "3":
        check = True
        print("Checkout")
        subtotal = 0

        for item in cart:
            index = items.index(item)
            price = prices[index]
            subtotal += price
            print(f"{item}: {price}")

        tax = subtotal * 0.06
        total = subtotal + tax

        print(f"Subtotal: {subtotal}")
        print(f"Tax (6%): {tax}")
        print(f"Total: {total}")
        print("Thank You Come Again!")
