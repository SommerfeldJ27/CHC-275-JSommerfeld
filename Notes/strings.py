"""
strings and parsing strings
.strip removes all white space
.lower forces all text to be lowercase
.upper forces all text to be uppercase
"""
print("1. A")
print("2. B")
print("3. C")
print("4. D")
option = input("Enter Your Selection: ")
if option.strip().lower == "A":
    print("Executing A")
elif option.strip().lower == "B":
    print("Executing B")
elif option.strip().lower == "C":
    print("Executing C")
elif option.strip().lower == "D":
    print("Executing D")