from typing import *
class Food:
    """
    """
    def __init__(self, name: str, cost: int, nutrition: int):
        self.name = name
        self.cost = cost
        self.nutrition = nutrition

class Dog:

    def __init__(self, breed: str, name: str, happiness: int, food):
        self.breed = breed
        self.name = name
        self.happiness = happiness
        self.eat(food)
        self.bark()

    def __str__(self) -> str:
        return(f"{self.name}: {self.happiness}")

    def eat(self,Food):
        self.happiness += (0.10 * Food.nutrition)

    def bark(self):
        return("RUFF RUFF!")

food = Food("apple", 1, 50)

dog = Dog("Husky", "Fenrir", 100, food)

print(dog, dog.bark())