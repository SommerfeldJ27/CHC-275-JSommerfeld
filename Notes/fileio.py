""" 
fileio.py


exception handling naturally leads us to file input/output. When the program stopped running, our program is reverted
back to its initial conditions.

every new account that we made, after the run of the program ends, we lose at the end. The natural way to circumvent this is by including
file input/output into our program. 

Most files on computers are just textual files with specifics contexts. 

There's nothing structurally different about python files vs regular text files <- this is true for mostly everything.

.docx are really just .txts with the microsoft overhead attached to them so when microsoft word parses the file when you open it, it strips
the overhead (which is used for styling and stuff) and displays it how you expect it to. 

excel spreadsheets are really csvs <- comma separated values 


escape sequences: special characters we put inside our strings in order to format it a certain way 
    - \n <= this stands for new line

"""

msg = "hello \nworld"
print(msg) #I should expect hello on line 1 and world on line 2 

""" 
These escape sequences are how files determine when one line starts and the next one ends. you can really expect a \n to be implicitly placed
at the end of each line. 

We covered exception handling for one particular reason: The file itself might not actually exist in our filesystem, and we don't the program
to stop running if the file exist <- I'll show you how to get around this stuff probably during the next class.

How file I/O works <- when we open a file 
"""

file = open("names.txt","r") #open("<filename>","<mode>") 


""" 
When we call the open function, the contents of your file is buffered in memory. 
"""

buffer = file.readlines() #this will take in our list of names and make each line an item inside our list 
names = [] #This would be account names
grades = [] #this would be balance
print(buffer) 
for line in buffer: #for each makes more sense here because we don't want to introduce
#index based technical overhead that is irrelevant to our program
    line = line.strip() #This removes white space
    line = line.split(",") #line is a list of two elements
                            #line[0] is the name
                            #line[1] is the grade value
    names.append(line[0])
    grades.append(line[1])
    

try: #i'm gouing to wrap this inside of a try-except because we might get an unexpected error, we haven't 
    #closed the file yet
    for i in range(len(grades)): #for-i loop because I'm modifying the grades directly
        grades[i] = int(grades[i]) #typecase
except ValueError:
    print("grade must be a number")

print(names)
print(grades)
file.close() #flush the buffered memory being used for the contents of the files 

""" 
What if we want two separate lists of related information? 

what if we wanted to have names,grade in the class? We could run two parallel
lists that are joined together by their specific indices. 
"""