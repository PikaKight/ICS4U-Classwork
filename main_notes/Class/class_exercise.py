"""
Person
======
name: str
height: int
strength: int
health_points: int = 100
---------
__str__(self) -> str
introduce(self) -> void
punch(Person) -> void
"""

class Person():

    def __init__(self, name: str, height: int, strength: int):
        self.name = name
        self.height = height
        self.strength = strength
        self.health_points = 100
        
    def __str__(self):
       return f"""
       {self.name}
       HP: {self.health_points}
       {self.introduce()}
       """
    
    def introduce(self):
        return (f"Hello, my name is {self.name}")
    
    def punch(self, Person):
        Person.health_points -= 10
        print(f"{Person.name}'s health is {Person.health_points}")

pikakight = Person("PikaKight", 161, 1)
mars = Person("Mars", 161, 1)

print(pikakight)
print(mars)

pikakight.punch(mars)
mars.punch(pikakight)
pikakight.punch(pikakight)
mars.punch(mars)
