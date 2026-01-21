""" 
Strings.py

The next big unit of content is about strings and about the act of parsing strings. 

if you've never heard the verb "parse" in context of "parsing something"

what we're doing is effectively analyzing the input and making sure its in the correct format we're expecting .

we're reading input -> transforming into something that we care about/can manipulate -> python code on that

                                        ^ Parsing 
                                        
                                        
we know from the input function that keyboard input comes in as which data type? String.

a = input("enter num 1")

a of type string so we couldn't manipulate this as integer until we typecasting. Typecasting is a form of parsing our input. 

we talked about lists and for-loops and other forms of iteration as our last big piece of content. 

lists = ordered sequences of elements all contained under one name

we can traverse those lists using for-each loops, for-i loops, or while loops. 

strings of text also behave as lists <= supposed to be mindblowing 

"hello" <= an ordered list of letters. So we can consider this a list of characters. 

strings <= ordered lists of characters.
"""

mystr = "hello"



print("for-each loop")
for char in mystr:
    print(char)



print("for i loop")
for i in range(len(mystr)):
    print(mystr[i])
    
    
""" 
The same ideas from lists also work for strings
    len() function
    square bracket operators
    .index()
    for loops work, etc. 
    

the reason why we can use a lot of the same attributes from lists is because 

lists and strings both inherit from the same parent which is called an iterable <= this is python trivia. 
    
strings have their own functions that are interesting to us. 
"""


#Template program
print("1. transfer")
print("2. deposit")
print("3. withdraw")
print("4. quit")

option = input("Enter your selection: ")
if option.strip().lower() == "transfer": #if option after all white space is removed is equal to A, execute codeblock underneath
    print("Executing A")
elif option.strip().lower() == "deposit": #your string matching when you want to parse your input has to be the exact format you're specify
    print("Executing B")
elif option.strip().lower() == "withdraw":
    print("Executing C")
elif option.strip().lower() == "quit":
    print("Executing D")
    
#This is a design pattern you should be very familiar with at this point.

""" 
Our design pattern only works with very strict string parsing. We couldn't have extra added spaces, our input had to be exactly uppercase. 

Baseline: Our string matching had to be as exact as possible. 

Python has a lot of built in functions that allow us to parse strings better. 


.strip() <== removes leading and trailing whitespace
"""

mystr = "          A"
print(mystr)
mystr = mystr.strip() #Removes all trailing and leading whitespace 
print(mystr) 

""" 
.strip() removed all of our white spaces giving us more generous parsing. 

String matching was case sensitive. We have two functions that force the string to either be all uppercase or all lowercase

Transfer
Deposit
Withdraw

.lower()
.upper()
"""


mystr = "A"
print(mystr)
mystr = mystr.lower() #Forces mystr to be lowercase 
print(mystr) 

""" 
We have .lower() and .strip() 

addition only works if both values are of the same data type
"""
""" 
ex = "10" + 5 #<= this is going to give us a type error 
              #This is devastating because it crashes the whole program, the program halts. 
"""              




""" 
How do we change how option is parsed to make sure we only attempt to typecast when the user types in a number? 

if-else statement

if only evaluates to true when option is a number. <= we have a function that does this for us 

isnumeric() <= returns True if the strings it's called on is a number. 
"""

option = input("Enter a number: ")
if option.isnumeric(): #Check to see if option is a number, if it is, proceed
    option = int(option) #this is how we would typecast option into an integer 
                        #if we don't input a number into option, we got a value error when trying to typecast 
    ex = option + 5
    print(ex)
else:
    print(f"{option} was not a number!")
    
#Doing this did not cause our program to halt. Anything that was dependent on the current program's state is not lost after parsing our string. 


""" 
Parsing a string in order to not get an error <= called error/exception handling 

Our standards for our code is a lot higher now because I let you write unsafe code by not doing any typechecking or error handling. 

In python in particular, there are other keywords for error handling that I'll introduce after this unit. 


"""

poem = "asdh8efoeif\nasdhasjkdhasd\nasdfghajksfhjkasf"
      #if you've never seen \n <= this is called an escape sequence and \n stands for newline 
print(poem)

""" 
What if I wanted a list of lines inside my poem?  

I want to parse my poem string and separate each line into its own element of a list called lines. 

.splitlines() <= returns a list of strings where each element is split by a newline 

"""

lines = poem.splitlines()
print(lines)

""" 
Why is a function like this useful? 

but file I/O (read as file input/output) is done by parsing plaintext inside of a .txt, but each line is separated with a \n.


"""