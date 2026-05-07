#oop2.py

""" 
Yesterday: 
    - We did object oriented Programming
        - Class: Blueprint for objects
        - Instances of Objects: Which are variables that are of the datatype of the class
        
    Objects have two things:
        - Member variables (attributes)
        - Member functions (methods)
        
    The reason why we want OOP:
        - They fix the scope problem:
            - Everything declared in def main has the same state:
                - Every function that is called in main has the same level of access to every variable that is also defined in main
                
            - This causes problems for a couple of reasons
                1) if you pass in a bad parameter into a function that access variables based on that parameter
                    - you might get unexpected behavior
                    
                change_grades(student)
                studentA.change_grades() # <- only has acccess to the member attributes of that instance of student 
                
    At the end of last class I said this thing:
        - Every single thing in python is an object including the code that you write: <- we're going to expand upon this 
        today
        
Today we're going to cover inheritance: <- we can define subclasses that borrow attributes and methods from a parent class

Person
    - Name
    - Address
    - SSN
    - phone number
    
    - greetings()
    
^ My first level abstraction of a human entity. Then we can define level 2 abstractions that are special cases of a person
(based on things like occupation, etc. )

Student
    - The same things a person
    - Grade Book #unique to student
    
    - Greetings() #derived from Person
    - Change_Grades() #unique to student

"""        

class Person:
    def __init__(self,name,address,ssn,phone):
            self.name = name
            self.address = address
            self.__ssn = ssn #this now has private scope only within the scope of the instance of a person object, same thing as private
            self.phone = phone
    
    def greetings(self):
        print(f"Hello, my name is {self.name} and I live at {self.address}")
        



""" 
Person is our top level abstraction, now we can define a Student child class
"""

class Student(Person): #if we pass a classname into the parenthesis of our class definition, we can create inheritance
    def __init__(self, name, address, ssn, phone,gradebook):
         super().__init__(name, address, ssn, phone) #super() calls the parent version of that function FIRST
         #and then every behavior after
         self.gradebook = gradebook
         
    
    def change_grades(self):
        try: 
            english_grade = int(input("enter the new english grade"))
            math_grade = int(input("enter the new math grade"))
            #you NEED to derefence the member attribute through self.<attribute> to update it
            self.grades["english"] = english_grade
            self.grades["math"] = math_grade
        except:
            print("error occured")




""" 
You can get really deep in the weeds on inheritance - it's basically what the entire AP CS test is.
    - Polymorphism: which is changing the behavior of methods that you're inheriting
    - Multiple Inheritance: You're inheriting the behaviors of two or more parent classes
    - Interfaces 
    - Enums 
    ... 
    
If you're in becoming:  
    - A game developer
    - A systems programmer
    - literally any SWE that is in the current workforce
    
If these interest you:
    - C++
    - C#
    - Java
    - Python
    - Typescript
    - Javascript 

So not only does OOP delineate attributes and methods between separate instances of objects, you're also allowed to hide exposure to variables to functions 
that don't deserve it. 

When you create a variable:
    - Public by default (even including member attributes)
    - privatize the variables 
    
    in Java these are separate keywords: public and private. But to make a member attribute private to global scope, you need to append a dunder to the prefix
    of that variable 
"""
class SpecialNumber:
    def __init__(self,val):
        self.value = val
        
    def __add__(self, other):
        return SpecialNumber(2*self.value + 2*other.value)

    def __str__(self):
        return f"{self.value}"

    def __getitem__(self, key):
        if key == 0:
            return self.value
        
    def __len__(self):
        return 4*self.value

def main():
    num1 = SpecialNumber(5)
    num2 = SpecialNumber(4)
    print(num1 + num2)
    print(num1[0])
    print(len(num1))
    

def foo(num):
    print(num)

""" 
Objects defined within the same scope don't have access to EACH OTHER'S variables 

The dunder functions (python specific) are magic functions in python. In python, the behavior of objects are not really determined by inherited behaviors.

What really determines the behavior of objects are how you implement the dunder functions 

functions are objects in python

.py files are really just text documents 

really .py is of datatype str

in python, every single thing is an object including the code that you write

Class A defines private foo
Class B defines public foo

Class C inherits from A and B

c.foo()
"""

object

main()