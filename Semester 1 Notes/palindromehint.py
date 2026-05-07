""" 
strings are lists (iterable) 

we can do for-loops over strings

for-loops pull out one character at a time 


"""

word = "hello"

for char in word: #creates a temporary variable corresponding to each individual character 
                  #inside of word  
   print(char)


#that means square bracket operators are fair game

print(word[0]) #print first character


""" 
first character: 0
last character: 4

length of a list is denoted as len(list) 

len(list) is which index? 

len(word) = 5 but there's no fifth index i can do 

len(word) - 1 <= this will actually get the last index 


word[0] <= first character
word[len(word) - 1] <= last character
""" 


str1 = "hello"
str2 = "world"
print(str1 + str2)
print(str2 + str1)


reverse = "" #<= this is the empty string 
letter1 = "a"
letter2 = "b"



print(letter1 + letter2 + reverse) #ab
print(letter2 + letter1 + reverse) #ba 

""" 
approach 1: 


after we save the word backwards into reverse using for-loop, the empty string, and concatenation, 

all we need to do is what? we can check equality with an if-statement 

1) input your word into a variable
2) reverse the word, save it into reverse
3) check if word == reverse

approach 2: two-pointer 

we know that strings are lists: 

mylist[index] <= something like this pulls out the element of a list

racecar
r     r
 a   a
  c c
   e
   
   
what is the index of the first item in a list? 0
what is the index of the last item in a list? -1, len(list) -1


while loop and a counting variable, the counting variable corresponds to the indices of the letters
in the word

and exit the loop as soon as the word is no longer a palindrome 

if we had a while loop with count variable as i = 0 initially, 

what should our exit condition be for our while loop?

if we're going to use i as our exit condition, what should the last number be for i? I only need
to iterate through the first half

while i < len(size) - 1 rather than doing this, i can

while i < (len(size) - 1)//2  <= this gets HALF of the indices inside our word 

i = 0

word[len(word) - 1] <= this is the last character
word[len(word) - 2]<= this is the second to last one
 
 
assume i = [0,1,2,3] 
 
word[len(word) - 1 - i] <= this is going to count downwards

check = True


racecar
r     r
 a   a
  c c
   e



while i < (len(size) - 1)//2 and check == True:
   if word[i] == word[len(word) - 1 - i]:
      i = i + 1
   else: 
      check = False

 
"""
