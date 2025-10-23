def is_palindrome(option):

    left, right = 0, len(option) - 1

    while left < right:

        if option[left] == " ":
            left += 1
        if option[right] == " ":
            right -= 1

        if option[left] != option[right]:
            return False

        left += 1
        right -= 1

    return True

option = input("Enter a word: ")
if is_palindrome(option):
    print("Palindrome")
else:
    print("Not a Palindrome")
