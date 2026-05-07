""" 
exceptionhandling.py

We're almost to november, 
    - there are no semester exams 
    - 15% goes towards a semester project
    
- completed in a group of 1 or 2
- completely open ended
    - come up with your own idea
    - submit a proposal 
    - it needs to have at least once instance of every skill we've discussed in this first semester
    - you can use third party python imports
        - matplotlib (for plotting)
        - pygame (allows for graphics in your games)
        - requests (which allows to make network connections with other ipaddresses) 
        - pybaseball (pulls all of the information baseball savant) 
        - flask for making website
        - tkinter for making general GUIs 
        
project ideas
    - a lot of people do command line text based games
        - the oregon trail
        - a weather app
        - cyber security util program (traceroute)
        - blackjack 
        - 4th down conversion probability chart
        

We spent the last unit working on string parsing (we modified our input and made sure it was valid for
the operations we were trying to do) we had a wrap a lot of the checking for values inside of if statements

if num.isnumeric(): 
    code block
else: 


^^ this was kind of annoying, but it also does not capture every possible error that might occur
"""

""" 
we got two distinct errors from the same control sequence.

exception handling is dealing with runtime errors in our program gracefully.

runtime errors = things that cause the program to crash while it is running
    -Zero division errors
    -value errors
    -type errors
compile time errors = errors that don't even allow the program to run 
    - mising colons
    - missing parentheses
    - bad indentation
 
 it is our duty as programmers to minimize the catastrophe that happens at runtime. runtime errors are especially
 bad because we have to restart the program and we lose the changes we make to variables as a result. 
 
 try:
    <code block> 
 except <exception>:
    <if some runtime erorr happens, execute this block>
 finally:
    <regardless of if try or except succeeds, run this codeblock>
    
we say when a program has a runtime error = the program threw an exception
exception =  the kind of error that showed up
"""


try: 
    x = int(input("enter num 1: ")) #this is of type list
    y = int(input("enter num 2: ")) #this is of type int
    quotient = x/y
    print(quotient)
except ValueError:
    #if either x or y is not a number, jump down to this block
    print("Both inputs need to be numeric") 
except ZeroDivisionError:
    print("denominator must be nonzero")
except Exception as e:
    #this captures all possible errors that are not value errors or zero division errors 
    print(e) #this informs me of any potential exceptions that might come up even if they don't have their own dedicated exception block
finally:
    #this will run no matter what, even if try succeeds or an exception occurs, this codeblock will run
    #finally blocks are NOT  required, but if you have a try block, then AT LEAST ONE except block needs to included. 
    print("thank you for using our calculator")
    
    
    
    
""" 
if we did with our previous tools, 
"""

""" 
x = input("enter num 1: ")
y = input("enter num 2: ")
if x.isnumeric():
    x = int(x)
if y.isnumeric():
    y = int(y)
if y != 0:
    quotient = x /y
    print(quotient)
    
""" 
""" 
So far we're only capturing two possible errors, value errors and divide by zero errors. How do we capture all generic exceptions except for
the ones that I have listed already.

catching exceptions is really important when it comes to manipulating files outside of python. 
    - I can't make assumptions about files already existing
    - I can't make assumptions about folders existing 
    - I can't make assumptions about websites still being running. 
on other people's computers. This is we use exception handling a lot 

A question that might come up in your mind is: 
    - why don't I always use except Exception as e:? 
        - we might want to do something specific depending on the error
        
finally: <= no matter if try succeeds, run the codeblock underneath


an exception handling philosophy thing: you want your try-except blocks to be capturing the smallest possible behavior where an exception might
occur. 

write a four function calculator where:
    - the input is string parsed
    - the program does not close after one math operation
    - each math operation is inside of a try-except block
"""