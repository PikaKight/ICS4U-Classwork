class Person():
    pass

class Chair():
    """
    Attrs:
        colour: str
        legs: int
        dimensions: list
        materials: list
        max_weight: int
        occupant: Object
    """

    def __init__(self, colour: str, legs: int, dimensions: list, materials: list, max_weight: int):
        self.colour = colour
        self.legs = legs
        self.dimensions = dimensions
        self.materials = materials
        self.max_weight = max_weight
        self.occupant: None

c1 = Chair("Blue", 4, [100, 50], ["Plastic", "Metal"], 200)
c2 = Chair("Green", 4,[100, 75], ["Plastic", "Metal"], 200)
jeff = Person()

c1.occupant = c2
c2.occupant = jeff

print(c1.colour, c1.legs, c1.dimensions, c1.materials, c1.max_weight, c1.occupant)

print(c1.occupant.colour, c1.occupant.legs, c1.occupant.dimensions, c1.occupant.materials, c1.occupant.max_weight, c1.occupant.occupant)

