"""
INHERITANCE

Dog
===
name: str
breed: str
----
__str__() -> str #just the name
make_sound() -> void

Squirrel
========
name: str
nuts_collected: int
-----
__str__() -> str #just the name
make_sound() -> void
"""
class Animal:
    sound = "General sound"

    def __init__(self, name:str):
        self.name = name

    def __str__ (self):
        return self.name
    @classmethod
    def make_sound(cls):
        return cls.sound

class Dog(Animal):
    sound = "Woof"

    def __init__(self, name: str, breed: str):
        super().__init__(name)
        self.breed = breed

class Squirrel(Animal):
    sound = "Squeak"

class Cat(Animal):
    sound = "Meow"

def main():
    shiro = Dog("Shiro", "Husky")
    noir = Cat("Noir")
    sam = Squirrel("Sam")

    print("\n", shiro, shiro.make_sound(), "\n", noir, noir.make_sound(), "\n", sam, sam.make_sound())

if __name__ == "__main__":
    main()