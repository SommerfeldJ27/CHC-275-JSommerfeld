""" 
branching.py 

When we run a calculator program, we expect to be able to choose which operation we want to do
from a list of options.

Having some sort of main menu protocol is contingent on our control structure. 

control structures = individual steps in our program
    - sequential (lines running one after another)
    - branching (what we're going to do today)
    - repetition (repeating code blocks)
    
branching = we want some code blocks to run based on certain conditions being met within our program.

strings, integers, floats (basically numbers and text.), boolean

boolean = True or False 

conditional = some logical statement that can evaluated to a boolean value 
            = some english statement that is either true or false 
            
if <conditional>:
    <MUST BE TABBED OVER code block>
<when you're done, untab>

if you're familiar with another language, usually looks something lie this

if (conditional) {}

modulus: % 

what modulus does is divide a by b and returns the remainder

a % b = a mod b = the remainder after a/b

we can use modulus to check for divisibility rules. For a number to be divisible by 2

a % 2 = 0

"""

""" 
ONE EQUALS (=) is for variable assignment TWO EQUALS (==) is for equality checking.

    Guaranteed ways kids screw up with if statements:
        1) make sure you have a colon after the if statement 
        2) make sure the codeblock underneath the if statement is tabbed over
        3) make sure EVERY line of code under the if statement has the SAME AMOUNT of white space
        
    VS CODE TOP TIP:
    
        If you highlight all of the whitespace, you'll see how many spaces are there.
        
        1 tab = 4 spaces. 
"""



""" 
The question is, what happens if we want to check some other condition. in other languages:

    if 
        thing
    else if 
        second thing 
        
python has a contraction for else and if 

    elif <= checks a second condition inside of our if-else chain 
"""



""" 
if 
elif 

both of these rely on some conditional statement. What about "all other states"? 

else
"""


    
""" 
What is the difference between 
"""

x= 10
#top one
if x % 2 == 0:
    #if x mod 2 is equal to 0, run the code block below
    #Runs when x = 10, does not run when x = 5
    print(f"{x} is divisble by 2")
elif x % 5 == 0:
     print(f"{x} is divisble by 5")

     
#bottom
if x % 2 == 0:
    #if x mod 2 is equal to 0, run the code block below
    #Runs when x = 10, does not run when x = 5
    print(f"{x} is divisble by 2")
    
if x % 5 == 0:
     print(f"{x} is divisble by 5") 
     
     
""" 

"""