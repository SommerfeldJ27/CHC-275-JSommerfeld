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
    return directory[student]["grades"], directory[student]["gradelevel"], directory[student]["email"]

def getStudentGrades(directory, student):
    return directory[student]["grades"]

def getStudentGradeLevel(directory,student):
    return directory[student]["gradelevel"]

def getStudentEmail(directory,student):
    return directory[student]["email"]

def getStudentsByGradeLevel(directory, gradelevel):
    for student in directory:
        if directory[student]["gradelevel"] == gradelevel:
            print(student)

def addStudent(directory):
    name = input("Please Enter Name:")
    enggrades = float(input("Please Enter English Grade:"))
    mathgrades = float(input("Please Enter Math Grade:"))
    histgrades = float(input("Please Enter History Grade:"))
    relgrades = float(input("Please Enter Religion Grade:"))
    grades = {"English": enggrades, "Math": mathgrades, "History": histgrades, "Religion": relgrades}
    email = input("please enter email")
    gradelevel = int(input("please enter grade level"))
    directory[name] = {"grades": grades, "gradelevel": gradelevel, "email": email}

def removeStudent(directory, student):
    if student in directory:
        directory.pop(student)

def updateGrade(directory, student):
    if student in directory:
        enggrades = float(input("Please Enter English Grade:"))
        mathgrades = float(input("Please Enter Math Grade:"))
        histgrades = float(input("Please Enter History Grade:"))
        relgrades = float(input("Please Enter Religion Grade:"))
        directory[student]["grades"] = {"English": enggrades, "Math": mathgrades, "History": histgrades, "Religion": relgrades}

def calculateGPA(directory, student):
    grades = directory[student]["grades"]
    total = sum(grades.values())
    classes = len(grades)
    GPA = total / classes
    return GPA

def checkHonorRoll(directory,student): #Still needs work done
    grades = directory[student]["grades"]
    GPA = calculateGPA(directory, student)
    if GPA >= 88 and min(grades.values()) > 81:
        print(f"{student}, made the Honor Roll!")
    else:
        print(f"sorry but {student}, did not make the Honor Roll")

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
    Students = {"Jimmy": {"grades": {"English": 90, "Math": 95, "History": 95, "Religion": 89},"gradelevel": 12,"email": "jimmy@email.com"},
                "Timmy": {"grades": {"English": 90, "Math": 85, "History": 75, "Religion": 89},"gradelevel": 11,"email": "timmy@email.com"},
                "Mike": {"grades": {"English": 90, "Math": 85, "History": 75, "Religion": 89},"gradelevel": 12,"email": "mike@email.com"},
                "John": {"grades": {"English": 90, "Math": 85, "History": 75, "Religion": 89},"gradelevel": 9,"email": "john@email.com"}}

    printMenu()
    choice = input("select your option: ")

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
    
    elif choice == "5":
        student = input("Student name: ")
        print(calculateGPA(Students, student))
        print(checkHonorRoll(Students, student))

    elif choice == "6":
        gradelevel = int(input("Grade level: "))
        getStudentsByGradeLevel(Students, gradelevel)

    elif choice == "7":
        return

    else:
            print("Invalid choice")

if __name__ == "__main__":
    main()