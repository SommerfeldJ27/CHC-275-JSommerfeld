
"""
file name: variables.py

Live coding: I write code in one pytheon file and have my notes in multiline comments in between code
segments

what is python?

    Python is a programing language
        a set of syntax and that you write instructions in for your computer to follow
        
        python is a command line prograsm
        when you download python odd the internet you're downloading what is actually called the python interepreter
        the interpretors role on your computer
        it looks at .py files and line by line convert valid python syntax into machine ConnectionAbortedError
    python is an interepreted language
    we just point the intereprerter aat'a python file and itl'll run the ConnectionAbortedError
    compiled languages
    c, c++, java, etc.
    call the compiler on your code file and till hwt cxompiled into an exicutable file tyhat you Run
    trhe first thing that is of importance tro us are variables
    the name of the variable
    its data type
    its Attribute <= the actual variabvle itself
    """
    
x=5
#^ This is a variable
#<name of your variable = <attribute>
    
print(x)

"""
    Data types
    numbers
    strings of text
    
    there are two kinda of data types
        -integer a whole number, including 0 and negative numbers
        - float floating point number, pi
        
    """
x = 5
    #this is a variable named x of type integer, of value 5
    
"""
    we can add subtract multiply divide and sqyare numbers
    """
y = 10
    
    #Addition
print(x + y)
    #Subtraction
print(x - y)
    #Multiplication
print(x * y)
    #Division
print(x / y)
    #Squaring a number
print(x ** 2)
    
"""
    sometuimes when we're manipulating numbers we want to qworek with the results again later on
    
    all we did was print thge results of our arithmatic
    
    the pythoin interpreter is reallu not thst smart it doesnty remembere whayt it prints so in order fpr
    python to remember what it did you nweeed to save it back into another variable or itself
    """
sum = x+y
print(sum)
"""
    so lets keep sun in mind and also add another variable tyo it
    
    thwe equals sign is reeaLLYU just an assignment operator and not an equality operator
    
    common things trhat happen
    you'll have a variabv;e that youy nwws to update repeatedly
    """
    
sum - sum + 20 #This is perfectly valid
"""sum is a named place in memory
    
    on the left hand side od the equals sign we're declatinmg a variable
    on the right hand sidfe we substitute the value of sum into where called it
    
    sum = x+y
    =15
    
    sum=sum+20
    sum=35
    """
print(sum)
"""
    sritngs of text in other programming langauages uyou have a data type specifically for singlwe chaeracters of text
    in poython strings of text are all the samwe data tyle (string)
    """
name = "Jackson Sommerfeld"
    #<namer of the variable> = <attributre>
print(name)
    
    #what if i want to print out "my name is"
    
"""
    in python we can do this in two ways
    
    fstrings format steingf and it lets specity placeholder values in strings so you can dop im variables
    
    """
print(f"My name is {name}")