option = input("Enter a word: ").strip().lower()
def palindrome(option):

    left, right = 0, len(option) - 1

    while left < right:


        if option[left] != option[right]:
            return False
        
        left += 1
        right -= 1

    return True

if palindrome(option):
    print("Palindrome")
else:
    print("Not a Palindrome")