phone = input("Enter phone number: ").strip()
new_phone = ""

for char in phone:
    if char.isdigit() or char == "(" or char == ")" or char == "-":
        new_phone += char

if len(new_phone) != 13:
    print("Error: Phone number is not sufficient length or formatting")
elif new_phone[0] != "(":
    print("Error: Perenthesis not in proper position")
elif new_phone[4] != ")":
    print("Error: Perenthesis not in proper position")
elif new_phone[8] != "-":
    print("Error: Dash not in proper position")
else:
    area_code = new_phone[1:4]
    exchange = new_phone[5:8]
    line_number = new_phone[9:13]

    print("Area code:", area_code)
    print("Exchange:", exchange)
    print("Line number:", line_number)
    print("Phone number:", new_phone)