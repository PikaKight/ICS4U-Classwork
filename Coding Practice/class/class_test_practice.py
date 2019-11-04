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

p = Person("Marcus", "Tuen Muk", date(2002, 10, 19))
print(p.get_age())

