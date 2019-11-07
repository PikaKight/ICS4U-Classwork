# method overloading
import arcade, random

""" In Java, you can create many functions that are the same, but have different parameter. Java will choose the one that is best to use.  
def draw_rectangle(x: int, y: int):
    pass

def draw_rectangle(x: int, y: int, w: int, h: int):
    pass

def draw_rectangle(x: int, y: int, w: int, h: int, color):
    pass
"""

def draw_rectangle(x: int, y: int, w = 50, h = 50, color = arcade.color.BLACK):
    pass

draw_rectangle(56, 56, 15651, 15651, arcade.color.BLUE)
draw_rectangle(56, 56, 15651, 15651)
draw_rectangle(56,56)

def draw_circle(x, y, r=50):
    print(f"Drawing Circle at {x}, {y} with radius of {r}.")

draw_circle(100, 100, 10)
draw_circle(200, 200, 20)
draw_circle(300, 300, 30)
draw_circle(500,500)

def draw_circle_ran(x, y, r=None):
    if r == None:
        r = random.randint(0, 99)
    print(f"Drawing Circle at {x}, {y} with radius of {r}.")

draw_circle_ran(100, 100)
draw_circle_ran(200,200)
draw_circle_ran(300,300, 300)