"""
- class field (variable)
- class method
"""

"""
Pizza
====
name: str
toppings: list[str]
-----
__str__ -> str

- __str__ format: "{name}, toppings: {toppings}"
- create main function and create some pizzas, print pizzas out.
"""

from typing import *

class Pizza:
    
    pizza_num = 1 #Class Variable

    def __init__(self, name: str, toppings: List[str]):
        self.name = name
        self.toppings = toppings
        self.order_number = Pizza.pizza_num
        Pizza.pizza_num += 1

    def __str__(self) -> str:
        return f"Order Number: {self.order_number} {self.name}, toppings: {self.toppings}"
   
    @classmethod
    def pepperoni(cls) -> "Pizza":
        return cls("Pepperoni", ["Mozzarella", "White Cheddar", "Pepperonis"])
   
    @classmethod
    def hawaiian(cls) -> "Pizza":
        return cls("Hawaiian", ["Mozzarella", "White Cheddar", "Beacon", "Ham", "Pineapple" ])
    
    @classmethod 
    def cheese(cls) -> "Pizza":
        return cls("Cheese", ["Mozzarella", "White Cheddar"])
        

def main():
    
    p1 = Pizza.pepperoni()

    p2 = Pizza.hawaiian()

    p3 = Pizza.cheese()

    print(p1)
    print(p2)
    print(p3)

main()