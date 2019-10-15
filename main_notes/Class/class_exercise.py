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
        return ("Hello, my name is {}".format(self.name))

pikakight = Person("PikaKight", 161, 243)
mars = Person("Mars", 161, 243)

print(pikakight)
print(mars)
