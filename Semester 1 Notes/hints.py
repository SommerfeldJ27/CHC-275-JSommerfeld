file = open("days.txt","r")
buffer = file.readlines() 
file.close()
print(buffer)

msft = buffer[0].split(",") #this is only string that looks like "msft, 346, 323, 466,...."
                 #Commas separate our substrings within our string
                 #Which string function divides our string based on a separator we specify
                 #all of the values in our list are currently strings
                 #we need to typecast these things into integers 

msft.pop(0) #this removes the first element
amzn = buffer[1]
nvda = buffer[2]

print(msft)

""" 
We have two kinds of for loops:
    - for each
    - for i 

one of these two allow direct modification of the list
    -for i 
    
    for-i loop that goes over all of the elements in each list and typecasts the numbers into integers
"""


