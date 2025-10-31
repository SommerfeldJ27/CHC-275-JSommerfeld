"""
Notes
.docx are just .txts with mircrosoft overhead so when word parses it it styrips the overheads and properly displays it
"""

msg = "hello \nworld"
print(msg)

file = open("names.txt","r") #open("<filename>","<mode>")

names = file.readline()
print(names)
for i in range(len(names)):
        names[i] = names[i].strip()
print(names)
file.close()