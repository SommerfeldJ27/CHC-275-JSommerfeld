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
    name = input("Please Enter Name: ").strip().lower()
    enggrades = float(input("Please Enter English Grade: "))
    mathgrades = float(input("Please Enter Math Grade: "))
    histgrades = float(input("Please Enter History Grade: "))
    relgrades = float(input("Please Enter Religion Grade: "))
    grades = {"English": enggrades, "Math": mathgrades, "History": histgrades, "Religion": relgrades}
    email = input("please Enter Email: ").strip().lower()
    gradelevel = int(input("Please Enter Grade Level: "))
    directory[name] = {"grades": grades, "gradelevel": gradelevel, "email": email}
    print(f"{name} was added successfully")

def removeStudent(directory, student):
    if student in directory:
        directory.pop(student)
        print(f"{student} was removed successfully")

def updateGrade(directory, student):
    if student in directory:
        enggrades = float(input("Please Enter English Grade:"))
        mathgrades = float(input("Please Enter Math Grade:"))
        histgrades = float(input("Please Enter History Grade:"))
        relgrades = float(input("Please Enter Religion Grade:"))
        directory[student]["grades"] = {"English": enggrades, "Math": mathgrades, "History": histgrades, "Religion": relgrades}
        print(f"{student}'s grades were updated successfully")

def calculateGPA(directory, student):
    grades = directory[student]["grades"]
    total = sum(grades.values())
    classes = len(grades)
    GPA = total / classes
    return (f"{student}'s GPA is {GPA}")

def checkHonorRoll(directory,student): #Still needs work done
    grades = directory[student]["grades"]
    GPA = calculateGPA(directory, student)
    if GPA >= 88 and min(grades.values()) > 81:
        print(f"{student}, made the Honor Roll!")
    else:
        print(f"Sorry but {student}, did not make the Honor Roll")

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
    Students = {"jimmy": {"grades": {"English": 90, "Math": 95, "History": 95, "Religion": 89},"gradelevel": 12,"email": "jimmy@email.com"},
                "timmy": {"grades": {"English": 90, "Math": 85, "History": 75, "Religion": 89},"gradelevel": 11,"email": "timmy@email.com"},
                "mike": {"grades": {"English": 90, "Math": 85, "History": 75, "Religion": 89},"gradelevel": 12,"email": "mike@email.com"},
                "john": {"grades": {"English": 90, "Math": 85, "History": 75, "Religion": 89},"gradelevel": 9,"email": "john@email.com"}}
    check = False
    while check == False:
        printMenu()
        choice = input("select your option: ")

        if choice == "1":
            addStudent(Students)

        elif choice == "2":
            student = input("Student name: ").strip().lower()
            removeStudent(Students, student)

        elif choice == "3":
            student = input("Student name: ").strip().lower()
            print(getStudent(Students, student))

        elif choice == "4":
            student = input("Student name: ").strip().lower()
            updateGrade(Students, student)
        
        elif choice == "5":
            student = input("Student name: ").strip().lower()
            print(calculateGPA(Students, student))
            print(checkHonorRoll(Students, student))

        elif choice == "6":
            gradelevel = int(input("Grade level: "))
            getStudentsByGradeLevel(Students, gradelevel)

        elif choice == "7":
            print(Students)
            return True

        else:
                print("Invalid choice")

if __name__ == "__main__":
    main()