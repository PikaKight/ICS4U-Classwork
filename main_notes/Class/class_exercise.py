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

    def __init__(self, name: str, height: int, strength: int, defense: int):
        self.name = name
        self.height = height
        self.strength = strength
        self.defense = defense
        self.health_points = 100
        
    def __str__(self):
       return f"""
       {self.name}
       HP: {self.health_points}
       {self.introduce()}
       """
    
    def introduce(self):
        return (f"Hello, my name is {self.name}")
    
    def punch(self, Person, times):
        if Person == self:
            Person.health_points -= ((10 * 0.25) * times)* ((self.strength - Person.defense) / 100)

        else:
            Person.health_points -= ((10 * times) * ((self.strength - Person.defense) / 100))

        print(f"{Person.name}'s health is {Person.health_points}")

    def eat(self):
        self.health_points = 100
        print (f"{self.name}'s health is back to {self.health_points}")

pikakight = Person("PikaKight", 161, 1, 100)
mars = Person("Mars", 161, 1, 50)

print(pikakight)
print(mars)


pikakight.punch(mars, 1)
mars.punch(pikakight, 1)
pikakight.punch(pikakight, 10)
mars.punch(mars, 10)

pikakight.eat()
mars.eat()

