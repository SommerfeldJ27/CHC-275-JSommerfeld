file = open("food.txt","r")
buffer = file.readlines()
items = []
prices = []
cart = []
cart_price = []
file.close()

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
        item = input("Enter Item Name: ").strip()
        if item in items:
            index = items.index(item)
            cart.append(item)
            cart_price.append(prices[index])
            print(f"Added {item} to cart.")
        else:
            print("Item not found.")

        print("Current cart:", cart)
    elif option == "2":
        item = input("Enter Item Name to remove: ").strip()
        if item in cart:
            index = cart.index(item)
            cart.pop(index)
            cart_price.pop(index)
            print(f"Removed {item} from cart.")
        else:
            print("Item not found.")

        print("Current cart:", cart)
    elif option == "3":
        check = True
        print("Receipt")
        for i in range(len(cart)):
            print(f"{cart[i]} - {cart_price[i]}")
        subtotal = sum(cart_price)
        statetax = 0.06
        tax = subtotal * statetax
        total = subtotal + tax
        print(f"Total: {total}")
        print("Thank You Come Again!")
    else:
        print("Invalid Option Try again.")
