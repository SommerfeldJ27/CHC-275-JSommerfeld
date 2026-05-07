#OOP.py

""" 
In programming there are 3-ish paradigms

paradigm = a way to think about designing something
    - Imperative: We write instructions for the computer to follow
    - Functional: Really hard and math based (you'll learn this in college if you're a CS major)
    - Objected Oriented: 
        - It's on the AP 
        - It's probably the most common way enterprise software is modeled
        - Based on the class-object design philosophy 
        
Context: Recall the student directory lab:
    - We stored every single student (as a dictionary) inside of another dictionary
        - Each student is 1 dictionary
            - Grades
            - Email
            - Class Year
            - Name
        - Each directory contains
            - a list of dictionaries
            
The directory is a container for students

Students is a container for the attributes that pertain to a student. 

There is a problem with this however: Scope 

Scope = The level of access a function has to certain variables that are delcared in other functions

Main <= global scope
Each function thats called within main has local scope to its own function body

Function A has its own scope
Function B has its own Scope

the Scope of A is not interoperable with the scope of B 

Scoping issues really pertains to making sure functions have the correct level of access to the variables
that only to pertain to itself 

change_grades() <- you don't want this function to have scope on variables that don't pertain to the student
you're passing in. 

student <= originally a string that corresponds to the key for the dictionary of that student

When change_grades is called, you could theoretically access EVERY single student's grades if you pass in
weird strings

bit shifts on strings which will cause issues and access problems 

Object Oriented Programming aims to fix the scope problem

1) Entity <= can be any abstract concept (Objects)
    - Member variables (attributes)
    - Member Functions (methods)
    
Every single object can be determined by its attributes and methods.

Dog object 
    - breed
    - name
    - coat color
    
    - Bark
    - greeting
    - Eat 
    
Dog.bark() or Dog.eat() <- and these unique methods are only exposed to (instances) of the Dog class. 

OOP:
    1) Classes (blueprints of objects)
    2) Instances of Classes (declared variables of the datatype Class)
    
mydog = Dog() <= mydog is an instance of the Dog class. 

let's create a student class

For a class to be valid (or at least usable) in python, there are certain required functions (methods)
    1) Constructor: when we declare an object of datatype Student, 
        - The constructor is called and it instantiates the member attributes based on the argument
        of the constructor 
        
In python there are a certain class of functions that you need to be aware of: Magic Functions

__ <= dunder 

Magic functions are also called dunder functions 

These functions are special built-in functions in python that are meant to be redefined 

The constructor dunder function in python: __init__()
"""
class Student: 
    def __init__(self,name,grades,email,gradyear): #< whenever we are writing classes (the blueprints)
        #the self parameter needs to be passed in ALWAYS, but when we call it, it's implicitly passed in
        self.name = name
        self.grades = grades
        self.email = email
        self.gradyear = gradyear
        
    #when we create an instance of the student class, these parameters are initialized 
    
    def change_grades(self):
        try:
            self.grades["Math"] = int(input("Enter your math grade"))
            self.grades["English"] = int(input("Enter your English grade"))
        finally:
            pass

mygrades = {"English":80,"Math":85}
mystudent = Student("John",mygrades,"john@chc.com",12) #this is how you call the constructor 
            #^ The color of this function is interesting to us 
            
# int() str() float() list() dict() are all constructors

#I can access attributes using dot notation
print(mystudent.name) #John
print(mystudent.grades) #{"English":80,"Math":85}
print(mystudent) #Whats going to happen? We get a memory address <= this is a problem we'll solve later

mystudent.change_grades() #This is different than how we implemented this in lab5
print(mystudent.grades)

""" 
The scope of student.change_grades()
    - Local Scope to the attributes of Student
    - Global Scope of the function its called within 
    
    
Previously for lab 5

This is our memory block [main[directory[student A,....,Student Z]]]
    - When we call change_grades on student
        The scope of change_grades is IDENTICAL to the scope of main

Now our block has changed 

[main[directory[student A,....,Student Z]]]

studentA.change_grades() [StudentA,global attributes]

In object oriented programming we can be much more specific about how our program's memory is managed 

OOP:
    Objects
        Attributes
        Methods 
        
Create instances of objects 
        Object A
            - Attributes A
            - Methods A
            
        Object B
            - Attributes B
            - Methods B
            
        Methods A does not have access to Attributes B 
        
we saw our primitive data types ints, strings, floats, bools have constructors. The implication is that primitives in python are objects

if primitives are objects that means the base building blocks of python are objects
"""

def foo():
    print("bar")
    
print(type(foo))

""" 
foo is also an object of type function

1) primitives are objects
2) functions are objects 

within python. What isn't an object? nothing. Everything is an object in python. The code you write in python is also
an object 
"""

mycode = "print('hello')"
myprogram = compile(mycode,"test","exec") #Now my program is a CodeType object 
exec(myprogram)

""" 
The behavior of objects in python can be uniquely determined by a file within your installation of python

builtins.pyi <- IS the specifications of python
"""

print("1" + "1") #11
print(1 + 1) #2

class SpecialNumber: 
    def __init__(self,value,value2):
        self.value = value
        self.value2 = value2
     

    def __add__(self, other):
        return 2*self.value + 2*other.value
    
    def __sub__(self, other):
        pass
    
    def __mul__(self, other):
        pass
    
    def __getitem__(self, key):
        if key == 1:
            return self.value
        elif key == 2:
            return self.value2
    
    
mynum1 = SpecialNumber(5,10)
mynum2 = SpecialNumber(4,8)

print(mynum1+mynum2) #this addition is not standard integer addition 
print(mynum1[1])
""" 
when we use squarebracket notation for lists/dictionaries

mylist.__getitem__(index)
mydict.__getitem__(key)
"""

list()

import pandas as pd 

pd.DataFrame