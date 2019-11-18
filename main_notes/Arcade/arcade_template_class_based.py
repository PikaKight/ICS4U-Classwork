import arcade, random

WIDTH = 800
HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.WHITE)

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        # Create your sprites and sprite lists here
        self.all_sprites = arcade.SpriteList()
        for _ in range(100):
            sprite = arcade.Sprite(filename="main_notes/Arcade/playerShip1_blue.png", 
                                    center_x=random.randrange(WIDTH), 
                                    center_y=random.randrange(HEIGHT), 
                                    scale=0.5)
            sprite.change_x = random.randint(-6, 6)
            sprite.change_y = random.randint(-6, 6)
            self.all_sprites.append(sprite)
            
        
        
     
    def on_draw(self):
        arcade.start_render()  # keep as first line
        # Draw everything below here.
        self.all_sprites.draw()

    def update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.all_sprites.update()
    
    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        print (key, key_modifiers)
        if key == arcade.key.D:
            self.all_sprites.change_x = 1
        if key == arcade.key.A:
            self.all_sprites.change_x = -1
        if key == arcade.key.W:
            self.all_sprites.change_y = 1
        if key == arcade.key.S:
            self.all_sprites.change_y = -1

        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    game = MyGame(WIDTH, HEIGHT, "My Game")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()