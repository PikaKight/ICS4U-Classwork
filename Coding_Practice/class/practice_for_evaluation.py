class Person:
    all_person = []
    @staticmethod
    def find_by_name(name:str):
        pass

    @staticmethod
    def check_pin_unique(pin: int) -> bool:
        for person in Person.all_person:
            if person.pin == pin:
                return False
            else:
                return True 
    
    def __init__(self, name, age, pin):
        self._name = name
        self._age = age
        self.pin = pin
        
        if Person.check_pin_unique(pin):
            Person.all_person.append(self)
        else:
            raise Exception("Pin must be unique.")
    
    def __str__(self) -> str:
        return f"{self._name} is {self._age}."

    def can_open_account(self) -> bool:
        return self._age >= 16
    
    def set_name(self, name:str):
        if type(name) != str:
            raise TypeError("Name must be a string.")
        self._name = name

    def get_name(self):
        return self._name

    def set_age(self, value: int):
        if type(value) != int:
            raise TypeError("Age must be an inteager.")
        self._age = value
    
    def get_age(self):
        return self._age

p = Person("Peter", 45, 200)
p2 = Person("Sally", 42, 232)
p.age = "hello"
print(p.get_age())
p.set_name("King")

if p.can_open_account():
    print(f"{p.get_name()} can open account.")

for person in Person.all_person:
    print(person)

class Student(Person):
    def __init__(self, name, age, pin, school: str):
        super().__init__(name, age, pin)
        self.school = school

    def __str__(self) -> str:
        return f"{self._name} is a student of {self.school}."

