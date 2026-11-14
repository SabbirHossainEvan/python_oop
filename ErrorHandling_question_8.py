class StudentNotFoundError(Exception):
    pass


def find_student(student_id, student_list):
    for student in student_list:
        if str(student.student_id) == str(student_id):
            return student
    raise StudentNotFoundError(f"No student found with ID '{student_id}'.")


def enroll_student(student_id, student_list):
    student = find_student(student_id, student_list)
    student.enroll_student()
    return student


def drop_student(student_id, student_list):
    student = find_student(student_id, student_list)
    student.drop_student()
    return student
