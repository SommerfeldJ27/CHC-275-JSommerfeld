""" 
lab 4 hints

1. File I/O 
    i. if you look at foods.txt, it is name,value.
    ii. it is a similar file structure to something we have worked with in the past.
    iii. rather than typecasting the price to an int, typecast it into a float 

2. Sales Tax
    i. 6% sales tax in MD 
    ii. Tax = Total * .06
    iii. Total = Total + tax
    
3. What kind of empty variables do we need at the start? Whatis going to be set to 0, what is going to be 
an empty list?
    i. total = 0
    ii. food = []
    iii. prices = []
    

file I/O before your while loop 

Outline
    1. Declare Empty Variables
    2. File I/O
    3. While loop containing the actual program structure


you probably want to hold everything in a while loop

"""

price = "1.75" #how do i typecast this
price = float(price) #integers are specifically whole numbers
print(price)