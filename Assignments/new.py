file = open("food.txt","r")
buffer = file.readlines()
items = []
prices = []
cart = []
cart_price = []
cart_quantity = []
file.close()

for line in buffer:
    line = line.strip()
    line = line.split(",")
    items.append(line[0])
    prices.append(float(line[1]))

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
        item = input("Enter item Name: ").strip()
        quantity = float(input("How many would you like: "))
        try:
            index = items.index(item)
            if item in cart:
                index = cart.index(item)
                cart_quantity[index] = quantity
                cart_price[index] = quantity * prices[index]
            else:
                cart.append(item)
                cart_quantity.append(quantity)
                cart_price.append(quantity * prices[index])
            print(f"Added {quantity} {item} to cart.")
        except ValueError:
            print("Item not found.")

        print("Current cart:", cart)
        
    elif option == "2":
        item = input("Enter item Name to remove: ").strip()
        try:
            index = cart.index(item)
            remove_quantity = float(input("How many would you like to remove? "))
            if remove_quantity >= cart_quantity[index]:
                cart.pop(index)
                cart_price.pop(index)
                cart_quantity.pop(index)
                print(f"Removed {item} from cart.")
            else:
                cart_quantity[index] = remove_quantity
                cart_price[index] = remove_quantity * prices[index]
                print(f"Removed {remove_quantity} {item} from cart.")
        except ValueError:
            print("Item not found.")

        print("Current cart:", cart)

    elif option == "3":
        check = True
        subtotal = sum(cart_price)
        statetax = 0.06
        tax = subtotal * statetax
        total = subtotal + tax
        print("Receipt:")
        print(f"{cart} - {cart_price}")
        print(f"Subtotal: {subtotal}")
        print(f"Tax: {tax}")
        print(f"Total: {total}")
        print("Thank You Come Again")
    else:
        print("Invalid Option")
