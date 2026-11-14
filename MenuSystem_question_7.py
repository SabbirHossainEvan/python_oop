from InitializeStudentObject_question_3 import student
from StudentDatabase_question_1 import StudentDatabase


def find_student(student_id):
    for student in StudentDatabase.student_list:
        if str(student.student_id) == student_id:
            return student
    return None


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
            student = find_student(student_id)
            if student is None:
                print("Student not found.")
            else:
                student.enroll_student()
                print(f"{student.name} is now enrolled.")

        elif choice == "3":
            student_id = input("Enter the student ID to drop: ").strip()
            student = find_student(student_id)
            if student is None:
                print("Student not found.")
            else:
                student.drop_student()
                print(f"{student.name} is no longer enrolled.")

        elif choice == "4":
            print("Exiting the student database.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    run_menu()
