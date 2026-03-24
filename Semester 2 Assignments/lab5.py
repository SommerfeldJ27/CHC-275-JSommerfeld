"""
Name: Jackson Sommerfeld
Section: 275-2
Description: Template for Lab 5
"""

"""
Scenario: we live in a world where blackbaud no longer exists. our job is to write
a student records program that can print out the transcript, grade level, and email of our students.
You are to implement this using functions, dictionaries, and lists
"""


def getStudent(directory, student):
    return directory[student]["grades"], directory[student]["grade_level"], directory[student]["email"]

def getStudentGrades(directory, student):
    return directory[student]["grades"]

def getStudentGradeLevel(directory,student):
    return directory[student]["gradelevel"]

def getStudentEmail(directory,student):
    return directory[student]["email"]

def getStudentsByGradeLevel(directory, gradelevel):
    """
        Function Name: getStudentsbyGradeLevel
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            gradelevel <int> : integer corresponding to the grade level
            Return Type:  none
        Description:
            procedure that prints out all of the students of a corresponding grade level.
    """
    pass

def addStudent(directory):
    name = input("Please Enter Name:")
    grades = int("Please Enter Grades") #needs to be fixed
    email = input("please enter email")
    gradelevel = int("please enter grade level")
    directory[name] = {"grades": grades, "email": email, "gradelevel": gradelevel}
    """
        Function Name: addStudent
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            Return Type:  none
        Description:
            procedure that adds a student with the following values: <dict> grades, <int> grade level, <string> email to the <dict>directory
    """
    pass

def removeStudent(directory, student):
    directory[student].pop #.pop instead of delete should be 1 liner

def updateGrade(directory, student):
    """
     Function Name: updateGrades
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type:  none
        Description:
            procedure that updates a student's gradebook
    """
    pass


def calculateGPA(directory, student):
    """
     Function Name: calculateGPA
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type:  <float> average of all grades
        Description:
            creates a GPA variable set equal to zero, then computes the average (mean) of all of the grades in the gradebook
    """
    GPA = 0
    pass


def checkHonorRoll(directory,student):
    """
     Function Name: checkHonorRoll
        Parameters:
            Directory <dict> : Student Directory that is specified in the main() function
            student <String> : String that corresponds to the student name
            Return Type:  <bool> True or False depending on a student has made the honor roll or not
        Description:
            Calls the calculateGPA() subroutine that gets the GPA then checks all grades in the grade book to see if they are all over 81, then returns True or False depending on if the GPA is 88 or better
    """
    pass

def printMenu():
    print("Welcome to Calvert Hall's Student Directory!")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Get Student")
    print("4. Update Grades")
    print("5. Calculate GPA")
    print("6. Get Students by Grade Level")
    print("7. Exit")
    pass

def main():
    #TODO: Implement every function in main
    Students = {"Jimmy": {"grades": {"Math": 90, "Science": 85},"gradelevel": 10,"email": "jimmy@email.com"},
                "Timmy": {"grades": {"Math": 80, "Science": 88},"gradelevel": 11,"email": "timmy@email.com"},
                "Mike": {"grades": {"Math": 95, "Science": 92},"gradelevel": 12,"email": "mike@email.com"},
                "John": {"grades": {"Math": 75, "Science": 70},"gradelevel": 9,"email": "john@email.com"}}
    printMenu()
    choice = input("Choose an option: ")

    if choice == "1":
        addStudent(Students)

    elif choice == "2":
        student = input("Student name: ")
        removeStudent(Students, student)

    elif choice == "3":
        student = input("Student name: ")
        print(getStudent(Students, student))

    elif choice == "4":
        student = input("Student name: ")
        updateGrade(Students, student)

    elif choice == "6":
        grade = int(input("Grade level: "))
        getStudentsByGradeLevel(Students, grade)

    elif choice == "7":
        return

    else:
            print("Invalid choice")

if __name__ == "__main__":
    main()

