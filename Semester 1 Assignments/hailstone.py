x = input("Enter a number: ")
x = int(x)

while x != 1:
    print (x)
    if x % 2 == 0:
        x = x/2
    elif x % 2 == 1:
        x = x * 3 + 1
if x == 1:
    print(x)