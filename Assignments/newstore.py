file = open("food.txt","r")
buffer = file.readlines()
items = []
prices = []
cart = []
cart_price = []
file.close()

for line in buffer:
    line = line.strip()
    line = line.split(",")
    items.append(line[0])
    prices.append(float(line[1]))

try: #i'm gouing to wrap this inside of a try-except because we might get an unexpected error, we haven't 
    #closed the file yet
    for i in range(len(prices)): #for-i loop because I'm modifying the prices directly
        prices[i] = int(prices[i]) #typecast
except ValueError:
    print("Price must be a number")

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
        quantity = float(input("How many would you like: "))
        try:
            index = items.index(item)
            cart.append(item)
            cart_price.append(quantity * prices[index])
            print(f"Added {quantity} {item} to cart.")
        except ValueError:
            print("Item not found.")

        print("Cart:", cart)

    elif option == "2":
        item = input("Enter Item Name: ").strip()
        quantity2 = float(input("How many would you like to remove: "))
        try:
            index = cart.index(item)
            index2 = cart_price.index(prices)
            cart.pop(index)
            for i in range(len(cart_price)): #for-i loop because I'm modifying the prices directly
                cart_price[i] = int(cart_price[i]) #typecast
            cart_price.pop(i)
            print(f"Removed {quantity2} {item} from cart.")
        except ValueError:
            print("Item not found.")
    elif option == "3":
        print("Reciept:")
        subotal = cart_price
        tax = sum(cart_price) * 0.06
        total = sum(cart_price) + tax
        print(f"Items: {cart} - {cart_price}")
        print(f"Tax: {tax}")
        print (f"Your total is: {total}")
        print("Thank you come again")
        check = True