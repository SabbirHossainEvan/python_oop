class Student:

    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

#this code belongs to question 7,8 and 9, it is a combination of the previous three questions

    def enroll_student(self):
        if self.__is_enrolled:
            raise ValueError("This student is already enrolled.")
        self.__is_enrolled = True

    def drop_student(self):
        if not self.__is_enrolled:
            raise ValueError("This student is not enrolled.")
        self.__is_enrolled = False

    def view_student_info(self):
        enrollment_status = "Enrolled" if self.__is_enrolled else "Not enrolled"
        print(f"Student ID: {self.__student_id}")
        print(f"Name: {self.__name}")
        print(f"Department: {self.__department}")
        print(f"Enrollment Status: {enrollment_status}")
