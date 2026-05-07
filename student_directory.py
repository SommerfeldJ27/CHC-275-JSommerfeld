# student_directory.py

class Student:

    # Constructor
    def __init__(self, name, email, grad_year):

        # Attributes
        self.name = name
        self.email = email
        self.grad_year = grad_year

        # Dictionary of grades
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

        print("Grades updated!")

    # Method to calculate average
    def get_average(self):

        total = sum(self.grades.values())
        average = total / len(self.grades)

        return average

    # Method to display info
    def display_info(self):

        print("\n----------------------")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Graduation Year: {self.grad_year}")

        print("\nGrades:")

        for subject, grade in self.grades.items():
            print(f"{subject}: {grade}")

        print(f"\nAverage Grade: {self.get_average():.2f}")
        print("----------------------")


class StudentDirectory:

    # Constructor
    def __init__(self):

        # List of Student objects
        self.students = []

    # Add a student
    def add_student(self):

        print("\n=== Add Student ===")

        name = input("Enter name: ")
        email = input("Enter email: ")
        grad_year = input("Enter graduation year: ")

        # Create Student object
        student = Student(name, email, grad_year)

        # Add object to list
        self.students.append(student)

        print(f"\n{name} added successfully!")

    # View all students
    def view_students(self):

        print("\n=== Students ===")

        if len(self.students) == 0:
            print("No students found.")
            return

        for i, student in enumerate(self.students):
            print(f"{i + 1}. {student.name}")

    # Find student object by name
    def find_student(self, name):

        for student in self.students:

            if student.name.lower() == name.lower():
                return student

        return None

    # Update grades
    def update_student_grades(self):

        name = input("\nEnter student name: ")

        student = self.find_student(name)

        if student is None:
            print("Student not found.")
            return

        student.update_grades()

    # Display student info
    def display_student_info(self):

        name = input("\nEnter student name: ")

        student = self.find_student(name)

        if student is None:
            print("Student not found.")
            return

        student.display_info()


# Main program
def main():

    directory = StudentDirectory()

    while True:

        print("\n====== STUDENT DIRECTORY ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Grades")
        print("4. Display Student Info")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            directory.add_student()

        elif choice == "2":
            directory.view_students()

        elif choice == "3":
            directory.update_student_grades()

        elif choice == "4":
            directory.display_student_info()

        elif choice == "5":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option.")


# Runs program
if __name__ == "__main__":
    main()