import arcade, random, math


WIDTH = 640
HEIGHT = 480

class Sprite:
    
    def __init__(self, x: int, y:int, radius: int = 25, speed_x: int = 0, speed_y: int = 0):
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y =speed_y
        self.radius = radius

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.radius, arcade.color.AZURE)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        
        if self.x > WIDTH or self.x < 0:
            self.speed_x *= -1

        if self.y > HEIGHT or self.y < 0:
            self.speed_y *= -1

window = arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")

sprites = []

for _ in range(10):
    x = random.randrange(WIDTH)
    y = random.randrange(HEIGHT)
    r = random.randint
    dx = random.randint(-5, 5)
    dy = random.randint(-5, 5)
    s = Sprite(x, y, r, dx, dy)
    sprites.append(s)
    

def setup():
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)
    arcade.run()


def update(delta_time):
    for s in sprites:
        s.update()


@window.event
def on_draw():
    arcade.start_render()
    # # Draw in here...
    # arcade.draw_circle_filled(100, 100, 25, arcade.color.BLUE)
    for s in sprites:
        s.draw()


@window.event
def on_key_press(key, modifiers):
    pass


@window.event
def on_key_release(key, modifiers):
    pass


@window.event
def on_mouse_press(x, y, button, modifiers):
    for s in sprites:
        a = s.x - x
        b = s.y - y
        dist = math.sqrt(a**2 + b**2)

    if dist < s.radius:
        s.radius += 1
        if s.radius > 50:
            sprites.remove(s)

if __name__ == '__main__':
    setup()