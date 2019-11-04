from typing import *
from datetime import date
class Person:
    def __init__(self, first_name: str, last_name: str, Dob: date):
        self._first_name = first_name
        self._last_name = last_name
        self._email = None
        self._dob = Dob

    def greet(self) -> str:
        return f"Hello, I am {self._first_name} {self._last_name}."

    def get_age(self) -> int:
        today = date.today()
        self._age = today.year - self._dob.year - ((today.month, today.day) < (self._dob.month, self._dob.day))
        return self._age

class Teacher(Person):
    def __init__(self, email_k12: str, OCT_Pin: int, school: str, classes: List[Class]):
        self._OCT_Pin = OCT_Pin
        self._school = school
        self._classes = classes

    def greet(self) -> void:
        return f"Hello, I am {self._first_name} {self._last_name} and I am a teacher at {self._school}"

class Class:
    def __init__(self, subject: str, students: List[Student]):
        pass

class Student(Person):
    def __init__(self, email_k12: str,student_number: int):
        self.email_k12 = email_k12
        self.sn = student_number
    
def main():
    p = Person("Marcus", "Tuen Muk", date(2002, 10, 19))
    print("\n", p.get_age(), "\n", p.greet())
    

if __name__ == "__main__":
    main()

