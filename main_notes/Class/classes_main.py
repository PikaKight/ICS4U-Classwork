from classes import *

def main():
    fluffy = Dog("Husky", "Fluffy")
    print(fluffy, "\n", fluffy.bark())
    
    apple = Food("apple", 1.50, 95)
    apple.set_nutrition(50)
    print(apple.get_nutrition())
    
    print(fluffy.eat(apple))
    print(fluffy)

if __name__ == "__main__":
    main()