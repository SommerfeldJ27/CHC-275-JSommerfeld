"""
Name:
Section:
Description: Template for Lab 7
"""

def getStudent(directory, student):
    if student in directory:
        return directory[student]["grades"], directory[student]["gradelevel"], directory[student]["email"]
    else:
        return None


def getStudentGrades(directory, student):
    if student in directory:
        return directory[student]["grades"]
    return None


def getStudentGradeLevel(directory, student):
    if student in directory:
        return directory[student]["gradelevel"]
    return None


def getStudentEmail(directory, student):
    if student in directory:
        return directory[student]["email"]
    return None


def getStudentsByGradeLevel(directory, gradelevel):
    for student in directory:
        if directory[student]["gradelevel"] == gradelevel:
            print(student)


def addStudent(directory):
    name = input("Enter student name: ")
    email = input("Enter student email: ")
    gradelevel = int(input("Enter grade level: "))

    grades = {}
    num_classes = int(input("How many classes? "))

    for i in range(num_classes):
        course = input("Course name: ")
        grade = int(input("Grade: "))
        grades[course] = grade

    directory[name] = {
        "grades": grades,
        "gradelevel": gradelevel,
        "email": email
    }


def removeStudent(directory, student):
    if student in directory:
        del directory[student]
        print("Student removed.")
    else:
        print("Student not found.")


def updateGrade(directory, student):
    if student in directory:
        course = input("Enter course to update: ")
        grade = int(input("Enter new grade: "))
        directory[student]["grades"][course] = grade
    else:
        print("Student not found.")


def calculateGPA(directory, student):
    GPA = 0
    grades = directory[student]["grades"].values()

    total = sum(grades)
    count = len(grades)

    if count > 0:
        GPA = total / count

    return GPA


def checkHonorRoll(directory, student):
    gpa = calculateGPA(directory, student)

    grades = directory[student]["grades"].values()

    for grade in grades:
        if grade <= 81:
            return False

    if gpa >= 88:
        return True

    return False


def printMenu():
    print("\nStudent Records System")
    print("1. Get Student Info")
    print("2. Get Student Grades")
    print("3. Get Students By Grade Level")
    print("4. Add Student")
    print("5. Remove Student")
    print("6. Update Grade")
    print("7. Check Honor Roll")
    print("8. Quit")


def main():

    Students = {
        "Jimmy": {
            "grades": {"Math": 90, "Science": 85},
            "gradelevel": 10,
            "email": "jimmy@email.com"
        },
        "Timmy": {
            "grades": {"Math": 80, "Science": 88},
            "gradelevel": 11,
            "email": "timmy@email.com"
        },
        "Mike": {
            "grades": {"Math": 95, "Science": 92},
            "gradelevel": 12,
            "email": "mike@email.com"
        },
        "John": {
            "grades": {"Math": 75, "Science": 70},
            "gradelevel": 9,
            "email": "john@email.com"
        }
    }

    while True:
        printMenu()
        choice = input("Choose an option: ")

        if choice == "1":
            student = input("Student name: ")
            print(getStudent(Students, student))

        elif choice == "2":
            student = input("Student name: ")
            print(getStudentGrades(Students, student))

        elif choice == "3":
            grade = int(input("Grade level: "))
            getStudentsByGradeLevel(Students, grade)

        elif choice == "4":
            addStudent(Students)

        elif choice == "5":
            student = input("Student name: ")
            removeStudent(Students, student)

        elif choice == "6":
            student = input("Student name: ")
            updateGrade(Students, student)

        elif choice == "7":
            student = input("Student name: ")
            print(checkHonorRoll(Students, student))

        elif choice == "8":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()