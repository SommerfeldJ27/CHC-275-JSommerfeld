# student_directory.py
# Fully working example of Object-Oriented Programming (OOP)
# Student Directory System

class Student:
    # Constructor
    def __init__(self, name, email, grad_year):
        self.name = name
        self.email = email
        self.grad_year = grad_year

        # Each student has their own grades dictionary
        self.grades = {
            "Math": 0,
            "English": 0,
            "Science": 0
        }

    # Method to update grades
    def update_grades(self):
        print(f"\nUpdating grades for {self.name}")

        self.grades["Math"] = int(input("Enter Math grade: "))
        self.grades["English"] = int(input("Enter English grade: "))
        self.grades["Science"] = int(input("Enter Science grade: "))

        print("Grades updated successfully!")

    # Method to calculate average grade
    def get_average(self):
        total = sum(self.grades.values())
        return total / len(self.grades)

    # Method to display student information
    def display_info(self):
        print("\n---------------------------")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Graduation Year: {self.grad_year}")
        print("Grades:")

        for subject, grade in self.grades.items():
            print(f"  {subject}: {grade}")

        print(f"Average Grade: {self.get_average():.2f}")
        print("---------------------------")


# Student Directory Class
class StudentDirectory:
    def __init__(self):
        # List that stores Student objects
        self.students = []

    # Add student to directory
    def add_student(self):
        print("\n=== Add New Student ===")

        name = input("Enter student name: ")
        email = input("Enter student email: ")
        grad_year = input("Enter graduation year: ")

        # Create a Student object
        new_student = Student(name, email, grad_year)

        # Add object to list
        self.students.append(new_student)

        print(f"{name} was added successfully!")

    # View all students
    def view_students(self):
        if len(self.students) == 0:
            print("\nNo students in directory.")
            return

        print("\n=== Student Directory ===")

        for index, student in enumerate(self.students):
            print(f"{index + 1}. {student.name}")

    # Find student by name
    def find_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student

        return None

    # Update a student's grades
    def update_student_grades(self):
        name = input("\nEnter student name: ")

        student = self.find_student(name)

        if student is None:
            print("Student not found.")
        else:
            student.update_grades()

    # Display one student's information
    def display_student_info(self):
        name = input("\nEnter student name: ")

        student = self.find_student(name)

        if student is None:
            print("Student not found.")
        else:
            student.display_info()


# Main Program
def main():
    directory = StudentDirectory()

    while True:
        print("\n====== STUDENT DIRECTORY ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student Grades")
        print("4. Display Student Information")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            directory.add_student()

        elif choice == "2":
            directory.view_students()

        elif choice == "3":
            directory.update_student_grades()

        elif choice == "4":
            directory.display_student_info()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


# Runs the program
main()