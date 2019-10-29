"""
- class field (variable)
- class method

- Inheritance
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
    
    pizza_num = 1

    def __init__(self, name: str, toppings: List[str]):
        self.name = name
        self.toppings = toppings
        self.order_number = Pizza.pizza_num
        Pizza.pizza_num += 1

    def __str__(self) -> str:
        return f"Order Number: {self.order_number} {self.name}, toppings: {self.toppings}"

def main():
    
    p1 = Pizza("Extra Chesse Pepperoni", ["Mozzarella", "White Cheddar", "Pepperonis"])

    p2 = Pizza("Hawaiian", ["Mozzarella", "White Cheddar", "Beacon", "Ham", "Pineapple" ])

    p3 = Pizza("Cheese", ["Mozzarella", "White Cheddar"])

    print(p1)
    print(p2)
    print(p3)

main()