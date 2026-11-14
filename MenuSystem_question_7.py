from InitializeStudentObject_question_3 import student
from StudentDatabase_question_1 import StudentDatabase
from ErrorHandling_question_8 import (
    StudentNotFoundError,
    enroll_student,
    drop_student,
)


def run_menu():
    while True:
        print("\nStudent Database Menu")
        print("1. View All Students")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            if not StudentDatabase.student_list:
                print("No students found.")
            else:
                for student in StudentDatabase.student_list:
                    student.view_student_info()
                    print("-" * 25)

        elif choice == "2":
            student_id = input("Enter the student ID to enroll: ").strip()
            try:
                student = enroll_student(student_id, StudentDatabase.student_list)
                print(f"{student.get_name()} is now enrolled.")
            except (StudentNotFoundError, ValueError) as error:
                print(error)

        elif choice == "3":
            student_id = input("Enter the student ID to drop: ").strip()
            try:
                student = drop_student(student_id, StudentDatabase.student_list)
                print(f"{student.get_name()} is no longer enrolled.")
            except (StudentNotFoundError, ValueError) as error:
                print(error)

        elif choice == "4":
            print("Exiting the student database.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    run_menu()
