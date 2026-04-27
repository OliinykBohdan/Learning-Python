# Task 1: Method Overriding (Basic)
#
# Description:
#
# Create a base class Animal
#
# Task:
#
# method speak() → prints 'Some sound'
#
# Create:
#
# Dog → 'Woof'
# Cat → 'Meow'
#
# Create objects and call speak()

print('-' * 10, 'Task 1:', sep = '\n')

class Animal:
    def speak(self):
        print('Some sound')

class Dog(Animal):
    def speak(self):
        print('Woof')

class Cat(Animal):
    def speak(self):
        print('Meow')

pet1 = Dog()
pet2 = Cat()

pet1.speak()
pet2.speak()

# Task 2: Same Method – Different Behavior
#
# Description:
#
# Polymorphism = same method, different behaviour
#
# Task:
#
# Create class Shape
#
# method area()
#
# Create:
#
# Rectangle → width, height
# Circle → radius
#
# Each class must implement its own area()
#
# Print areas

print('-' * 10, 'Task 2:', sep = '\n')

import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

figure1 = Rectangle(5, 8)
figure2 = Circle(8)

print(figure1.area())
print(figure2.area())

# Task 3: Loop Polymorphism
#
# Description:
#
# Use polymorphism in loop
#
# Task:
#
# Create:
#
# Dog → speak()
# Cat → speak()
# Cow → speak()
#
# Store objects in list
#
# Loop and call speak()

print('-' * 10, 'Task 3:', sep = '\n')

class Animal:
    def speak(self):
        print('Some sound')

class Dog(Animal):
    def speak(self):
        print('Woof')

class Cat(Animal):
    def speak(self):
        print('Meow')

class Cow(Animal):
    def speak(self):
        print('Myy')

creatures = [Dog(), Cat(), Cow()]

for creature in creatures:
    creature.speak()

# Task 4: Function Polymorphism
#
# Description:
#
# Function works with different objects
#
# Task:
#
# Create function:
#
# def make_sound(animal):
#     animal.speak()
#
# Pass:
#
# Dog
# Cat

print('-' * 10, 'Task 4:', sep = '\n')

class Dog:
    def speak(self):
        print('Woof')

class Cat:
    def speak(self):
        print('Meow')

def make_sound(animal):
    animal.speak()

creature1 = Dog()
creature2 = Cat()

make_sound(creature1)
make_sound(creature2)

# Task 5: Without Inheritance (Duck Typing)
#
# Description:
#
# Polymorphism without inheritance
#
# Task:
#
# Create:
#
# class Car → method move()
# class Bird → method move()
#
# Car → 'Driving'
# Bird → 'Flying'
#
# Call both using a single function

print('-' * 10, 'Task 5:', sep = '\n')

class Car:
    def move(self):
        print('Driving')

class Bird:
    def move(self):
        print('Flying')

def movement(unit):
    unit.move()

car = Car()
bird = Bird()

movement(car)
movement(bird)
