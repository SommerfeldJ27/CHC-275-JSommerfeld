file = open("food.txt","r") #opens file and mode
buffer = file.readlines()
items = [] #items
prices = [] #item prices
cart = [] #cart of what to purchase
quantity = []
cart_price = [] #price of wanted items
file.close()

for line in buffer:
    line = line.strip().split(",") #removes whitespace and splits them up
    items.append(line[0])
    prices.append(float(line[1])) #converts to number

print(items)
print(prices)

check = False

while check == False:
    print("Welcome to the grocery store. Please select your option:")
    print("1. Add to cart")
    print("2. Remove from cart")
    print("3. Checkout")

    option = input("Enter your selection: ").strip().lower() #user input
    if option == "1":
        item = input("Enter Item Name: ").strip() #user input
        quantity = float(input("How many would you like: "))
        try:
            index1 = items.index(item)
            cart.append(item) #adds item to cart
            cart_price.append(quantity * prices[index1]) #adds item price to cart
            print(f"Added {quantity} {item} to cart.")
        except ValueError:
            print("Item not found.")

        print("Current cart:", cart)
    elif option == "2":
        item = input("Enter Item Name to remove: ").strip() #user input
        quantity2 = float(input("How many would you like to remove: "))
        try:
            new_quantity = quantity - quantity2
            cart_price.append(new_quantity * prices[index1]) #establishes new price after removing items
            print(f"Removed {quantity2} {item} from cart.")
        except quantity2 > quantity or ValueError:
            print("Tried to remove too many items or item not found.")
        if quantity2 == quantity:
            index2 = cart.index(item)
            cart.pop(index2) #removes item from cart

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
