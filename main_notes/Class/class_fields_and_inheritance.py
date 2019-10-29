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
    
    def __init__(self, name: str, toppings: List[str]):
        self.name = name
        self.toppings = toppings

    def __str__(self) -> str:
        return f"{self.name}, toppings: {self.toppings}"

def main():
    
    p1 = Pizza("Extra Chesse Pepperoni", ["Mozzarella", "White Cheddar", "Pepperonis"])

    p2 = Pizza("Hawaiian", ["Mozzarella", "White Cheddar", "Beacon", "Ham", "Pineapple" ])

    print(p1)
    print(p2)

main()