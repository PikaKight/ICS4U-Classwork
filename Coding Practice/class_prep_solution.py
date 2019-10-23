class Food:

    def __init__(self, name:str, cost:int, nutrition:int):
        self.name = name
        self.cost = cost
        self.nutrition = nutrition

class Dog:

    def __init__(self, breed: str, name: str):
        self.breed = breed
        self.name = name
        self.happiness = 100

    def __str__(self) -> str:
        return (f"{self.name}, Happiness: {self.happiness}")

    def bark(self):
        return("RUFF RUFF!")

    def eat(self,Food):
            self.happiness += (0.10 * Food.nutrition)

fluffy = Dog("Husky", "Fluffy")
apple = Food("apple", 1.50, 95)

print(fluffy, "\n", fluffy.bark())
fluffy.eat(apple)
print(fluffy)