class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError("Subclasses must implement abstract method move()")


class Dog(Animal):
    def move(self):
        print(f"{self.name} is running")


class Bird(Animal):
    def move(self):
        print(f"{self.name} is flying")


class Snake(Animal):
    def move(self):
        print(f"{self.name} is slithering")


# Demonstrating polymorphism
animals = [Dog("Rex"), Bird("Tweety"), Snake("Snakie")]

for animal in animals:
    animal.move() 

# Explanation:
# This program defines an `Animal` base class with a `move()` method that doesn't do anything,
# but it's marked as `NotImplementedError` to ensure subclasses implement it.
# Each subclass (Dog, Bird, Snake) implements `move()` differently to showcase polymorphism.
# When we loop through a list of these animal objects and call `move()`, each animal behaves according to its type.

# This demonstrates the flexibility and power of polymorphism in object-oriented programming.
# It allows us to treat objects of different classes uniformly (through `move()`) while allowing each class
# to define its own unique behavior for that method, enhancing code readability and maintainability.