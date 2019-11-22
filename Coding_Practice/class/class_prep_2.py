import datetime
from typing import List, Optional

class Classroom:
    warnings: List[str] = []

    def __init__(self, name: str):
        self._subject = name
        self._students: List[Student] = []

    def set_name(self, name: str):
        self._subject = name
        
    def get_name(self):
        return self._subject
    
    def add_student(self, student: "Student"):
        if student in self._students:
            raise Exception("Cannot add a student to a class more than once!")

        self._students.append(student)

        if len(self._student) > 33:
            warning = f"{self._subject} has more than 33 students!"
            Classroom.warnings.append(warning)

    def remove_student(self, student: "Student"):
        self._students.remove(student)

    def get_student(self):
        return self._students

class Person:
    def __init__(self, first_name: str, last_name: str, DOB: datetime.datetime, email: str = None):
        self._first_name = first_name
        self._last_name = last_name
        self._DOB = DOB
        self._email = email

    def set_first_name(self, name: str):
        self._first_name = name

    def get_first_name(self):
        return self._first_name

    def set_last_name(self, name: str):
        self._last_name = name

    def get_last_name(self):
        return self._last_name

    def set_email(self, email: str):
        self._email = email
    
    def get_email(self) -> Optional[str]:
        return self._email
    
    def get_DOB(self) -> datetime.datetime:
        return self._DOB

    def get_age(self):
        today = datetime.date.today()
        return today.year - self._DOB.year

    def greet(self):
        return f"Hello, my name is {self._first_name} {self._last_name}."

class Student(Person):
    def __init__(self, first_name: str, last_name: str, DOB: datetime.datetime, student_number: int, email: str = None):
        super().__init__(first_name, last_name, DOB, email)
        self._student_number = student_number
        self._k12 = self._generate_k12
        
    def _generate_k12(self):
        grad = (self._DOB.year + 18) % 100
        return f"{self._first_name.lower()}.{self._last_name.lower()}{grad}@ycdsbk12.ca"
    
    def set_student_number(self, sn: int):
        try:
            self._student_number = int(sn)
        except:
            raise Exception("Student number must be an integer.")
    
    def get_student_number(self):
        return self._student_number
    
    def greet(self):
        return f"Hello, my name is {self._first_name} {self._last_name} and I'm a student."   

class Teacher(Person):
    def __init__(self, first_name: str, last_name: str, DOB: datetime.datetime, OCT_Pin: int, school: str, email: str = None):
        super().__init__(first_name, last_name, DOB, email)
        self._OCT_Pin = OCT_Pin
        self._school = school
        
    def _generate_k12(self):
        return f"{self._first_name.lower()}.{self._last_name.lower}@ycdsbk12.ca"
        

