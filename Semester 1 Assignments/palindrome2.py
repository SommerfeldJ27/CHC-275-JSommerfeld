word = "racecar"
i = 0
check = True
while i < len(word)//2:
    if word[i] != word[-i -1]:
        check = False
        break
    i +=1
print(check)