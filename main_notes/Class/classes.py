class Food:

    def __init__(self, name:str, cost:int, nutrition:int):
        self.name = name
        self.cost = cost
        self._nutrition = nutrition

    def set_nutrition(self, value):
        if type(value) != int:
            raise TypeError("Nutrition can only be of type int.")
        self._nutrition = value
    
    def get_nutrition(self):
        return self._nutrition

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
            self.happiness += (0.10 * Food._nutrition)
            return (f"{self.name}, eats {Food.name} for {self.happiness} happiness.")