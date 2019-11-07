from typing import List
from datetime import date

class Person:
    def __init__(self, first_name: str, last_name: str, DOB: date, email=None):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._DOB = DOB
    
    def set_first_name(self, first_name: str):
        self._first_name = first_name
        return self._first_name
    
    def get_first_name(self):
        return self._first_name

    def set_last_name(self, last_name: str):
        self._last_name = last_name
        return self._last_name
    
    def get_last_name(self):
        return self._last_name

    def set_email(self, email: str):
        self._email = email
        return self._email
   
    def get_email(self):
        return self._email

    def greet(self) -> str:
        return f"Hello, my name is {self._first_name} {self._last_name}."

    def get_DOB(self):
        return(self._DOB)

    def get_age(self) -> int:
        today = date.today()
        self._age = today.year - self._DOB.year - ((today.month, today.day) < (self._DOB.month, self._DOB.day))
        return self._age

class Student(Person):
    def __init__(self, first_name: str, last_name: str, DOB: date, student_number: int, email=None):
        super().__init__(first_name, last_name, DOB, email)
        self._email_k12 = self._generate_email_12
        self._sn = student_number

    def _generate_email_k12(self):
        return f"{self._first_name.lower}.{self._last_name.lower}{(self._DOB.year + 18) % 100}@ycdsbk12.ca"
    
    def set_student_number(self, sn:int):
        try:
            self._sn = sn
        except ValueError:
            raise TypeError("Student Number must be an integer!")

class Classroom:
    warning = []
    def __init__(self, subject: str):
        self._name = subject
        self._students = []
        self.warning = Classroom.warning
        
    def get_students(self):
        return self._students

    def get_name(self):
        return self._name

    def set_name(self, new_name: str):
        self._name = new_name
        return self._name

    def add_student(self, student: Student):
        if student in self._students:
            raise Exception(f"{student._first_name} {student._last_name} is already in this class.")
        else:
            self._students.append(student)
        
        if len(self._students) > 33:
            Classroom.warning.append(f"{self._name} has more than 33 students.") 
    
    def remove_student(self, student: Student):
        if student not in self._students:
            raise Exception(f"{student._first_name} {student._last_name} is not part of this class.")
        else:
            self._students.remove(student)
    
class Teacher(Person):
    all_teacher = {}
    def __init__(self, email_k12: str, OCT_Pin: int, school: str, classes: List[Classroom]):
        self._OCT_Pin = OCT_Pin
        self._school = school
        self._classes = classes
        Teacher.all_teacher[Person._last_name] = self.OCT_Pin

    def greet(self):
        return f"Hello, I am {self._first_name} {self._last_name} and I am a teacher at {self._school}"
    
    def add_class(self, classroom: Classroom):
        if len(self.__classes) < 6:
            self._classes.append(classroom)
        
    def remove_class(self, classroom: Classroom):
        self._classes.remove(classroom)

    @classmethod
    def find_by_OCT_Pin(cls, teacher_OCT_Pin: int):
        for pin in cls.all_teacher.values():
            if teacher_OCT_Pin in pin:
                return Person

    @classmethod
    def find_by_last_name(cls, teacher_last_name: str):
            for name in cls.all_teacher.keys():
                    if teacher_last_name in name:
                        return Person


    
def main():
    p = Person("Marcus", "Tuen Muk", date(2002, 10, 19), "marcus.tuenmuk20@ycdsbk12.ca")
    print("\n", p.get_age(), "\n", p.greet())
    math = Classroom("math")    

if __name__ == "__main__":
    main()

