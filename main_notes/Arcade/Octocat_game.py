import arcade, random, math

HEIGHT = 600 
WIDTH = 800

class Main(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.AZURE)


def main():
    game = Main(WIDTH, HEIGHT, "Octocat")
    arcade.run()

main()