def is_palindrome(option):

    palindrome = option

    left, right = 0, len(palindrome) - 1

    while left < right:

        if palindrome[left] == " ":
            left += 1
        if palindrome[right] == " ":
            right -= 1

        if palindrome[left] != palindrome[right]:
            return False

        left += 1
        right -= 1

    return True

option = input("Enter a word: ")
if is_palindrome(option):
    print("It's a palindrome")
else:
    print("It's not a palindrome")
