from StudentClass_question_2 import Student
from StudentDatabase_question_1 import StudentDatabase


student = Student(
    student_id="S001",
    name="Student Name",
    department="Computer Science",
    is_enrolled=True,
)
StudentDatabase.add_student(student)
