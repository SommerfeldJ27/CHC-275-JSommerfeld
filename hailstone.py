x = input("Enter a number: ")
x = int(x)

check = False

while check == False:
    print (x)
    if x == 1:
        check == True
    if x % 2 == 1:
        x = x * 3 + 1
    elif x % 2 == 0:
        x = x/2