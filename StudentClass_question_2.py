class Student:

    def __init__(self, student_id, name, department, is_enrolled):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.is_enrolled = is_enrolled

#this code belongs to question 7 and 8

    def enroll_student(self):
        if self.is_enrolled:
            raise ValueError("This student is already enrolled.")
        self.is_enrolled = True

    def drop_student(self):
        if not self.is_enrolled:
            raise ValueError("This student is not enrolled.")
        self.is_enrolled = False

    def view_student_info(self):
        enrollment_status = "Enrolled" if self.is_enrolled else "Not enrolled"
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Enrollment Status: {enrollment_status}")
