class Food:
    """ This is a Food Class

    Attributes:
        name (str): The name of the food
        cost (int): Cost of the food
        nutrition (int): The nutrition value of the food
    """

    def __init__(self, name:str, cost:int, nutrition:int):
        """
        Args: 
            name: Food name
            cost: cost of the food
            nutrition: how nutritious is the food
        """
        self.name = name
        self.cost = cost
        self.nutrition = nutrition

class Dog:
    """ Dog class
    Attributes:
        breed (str): 
    """
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
            return (f"{self.name}, eats {Food.name} for {self.happiness} happiness.")

def main():
    fluffy = Dog("Husky", "Fluffy")
    apple = Food("apple", 1.50, 95)

    print(fluffy, "\n", fluffy.bark())
    print(fluffy.eat(apple))
    print(fluffy)

if __name__ == "__main__":
    main()