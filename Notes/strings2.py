""" 
strings2.py


Last class we were parsing strings.

    - strings behave like lists
        - for-loops 
        - while loops
    - strip() removes all trailing and leading whitespace
    - lower()/upper() forces the string to be either entirely lowercase ore entirely uppercase
    - isnumeric() <- returns True if the string was a number


We have a few more string functions that are interesting to us, and the next PSET is uploaded. In the spirit of parsing strings, there are 
a few more things we might consider
"""


mystr = "Frank Teague Preston"  #all of my names are in one string but separated by spaces

""" 
I can split mystr into a list of individual strings by using .split()
"""

names = mystr.split() #This will split the string into a list of elements where each element is separated by the whitespaces
print(names)

""" 
So you might get a data packet over a computer network that is delineated by a start and end sequences of bits


11010101 <= my sentinel bit sequence (this denotes when one message ends and another begins) 
"""

mystr = "11010101Hello11010101World11010101How11010101Are11010101You11010101"

msg = mystr.split("11010101") 
print(msg)

""" 
In terms of parsing strings, having the ability to split a datastream by a reserved start and end sequence helps clean up our message. 
"""

""" 
.join() <= you can think of this as being the inverse of .split() 


"""


space = " " #You wouldn't typically create a variable for blank spaces. 
newmsg = space.join(msg)
print(newmsg)

""" 
What .join() does is it takes the stirng you call .join() on, and creates a concatenated string where each element of the list is split by
the string you call .join() 

You can call string methods on strings that aren't saved to variable 
"""

newmsg = " ".join(msg).strip() #You can chain functions together like i mentioned before. 
print(newmsg)


""" 
Python behaves in a weird way compared to other languages because are a lot of shortcuts. Chaining strings together like this is very "pythonic"
"""

"""
#Template program
print("1. transfer")
print("2. deposit")
print("3. withdraw")
print("4. quit")

option = input("Enter your selection: ").strip().lower()
if option == "transfer": #if option after all white space is removed is equal to A, execute codeblock underneath
    print("Executing A")
elif option == "deposit": #your string matching when you want to parse your input has to be the exact format you're specify
    print("Executing B")
elif option == "withdraw":
    print("Executing C")
elif option == "quit":
    print("Executing D")
    
    
"""
""" 
we have

-lower()
-upper()
-strip()
-isnumeric()
-split()
-splitlines()
-join()
"""

""" 
Recall this fact:

we can add numbers together just using the plus sign.

"""

sum = 5 + 4 #<= completely valid, we expect this behavior

str1 = "Hello"
str2 = "World"
joined = str1 + str2 #This concatenates str1 to str2
joined2 = str2 + str1 #This effectively reversed the string 
print(joined)
print(joined2) 