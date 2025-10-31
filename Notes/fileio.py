"""
Notes
.docx are just .txts with mircrosoft overhead so when word parses it it styrips the overheads and properly displays it
if both .txt file and .py file referencing the .txt are in the same folder use ls and cd commands to list and change directories to fix errors
"""

msg = "hello \nworld"
print(msg)

file = open("names.txt","r") #open("<filename>","<mode>")

buffer = file.readlines()
names = []
grades = []
print(buffer)
for line in buffer:
    
    line = line.strip()
    line = line.split(",")
    
    
    names.append(line[0])
    grades.append(line[1])


try:
    
    for i in range(len(grades)):
        grades[i] = int(grades[i])
except ValueError:
    print("grade mustr be a number")

print(names)
print(grades)
file.close()
