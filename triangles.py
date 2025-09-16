angle1 = input("Enter angle 1: ")
angle1 = int(angle1)

angle2 = input("Enter angle 2: ")
angle2 = int(angle2)

angle3 = input("Enter angle 3: ")
angle3 = int(angle3)

if (angle1 == 90 and angle2 + angle3 == 90) or (angle2 == 90 and angle1 + angle3) or (angle3 ==  90 and angle1 + angle2 == 90):
    print("This is a triangle")