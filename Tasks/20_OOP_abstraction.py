# Task 1: Abstract Class (Basic)
# Description:
#
# Create an abstract base class
#
# Task:
#
# Create class:
#
# from abc import ABC, abstractmethod
# class Animal(ABC):
# Add:
# abstract method speak()
# Create:
# Dog → 'Woof'
# Cat → 'Meow'
# Call:
# animals = [Dog(), Cat()]
#
# Loop and print sounds

print('-' * 10, 'Task 1:', sep = '\n')

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
       pass

class Dog(Animal):
    def speak(self):
        return 'Woof'

class Cat(Animal):
    def speak(self):
        return 'Meow'

animals = [Dog(), Cat()]

for animal in animals:
    print(animal.speak())

# Task 2: Cannot Instantiate Abstract Class
# Description:
#
# Understand restriction
#
# Task:
#
# Try:
#
# a = Animal()
# Expected:
#
# Error
#
# Question:
#
# Why does this happen?

print('-' * 10, 'Task 2:', sep = '\n')

class Animal(ABC):
    @abstractmethod
    def speak(self):
       pass

try:
    a = Animal()

except TypeError:
    print('TypeError')

# Why does this happen? Because the speak method must be implemented (a subclass containing this method must be created)

# Task 3: Abstract Method with Multiple Methods
# Description:
#
# Multiple required methods
#
# Task:
#
# Create:
#
# class Shape(ABC):
# Methods:
# area()
# perimeter()
# Create:
# Rectangle
# Circle
# Print:
#
# area + perimeter

print('-' * 10, 'Task 3:', sep = '\n')

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 3.14 * 2 * self.radius

rectangle = Rectangle(10, 20)
circle = Circle(5)

print('Area rectangle:', rectangle.area())
print('Perimeter rectangle:', rectangle.perimeter())
print('Area circle:', circle.area())
print('Perimeter circle:', circle.perimeter())
