# Task 1
#
# Create a Dog class that:
#
# has the following attributes: name, age
#
# has a method called bark(), which prints:
#
# Woof! My name is <name>

print('-' * 10, 'Task 1:', sep = '\n')

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'Woof! My name is {self.name}')

animal = Dog('Rex', 1)

animal.bark()

# Task 2
#
# Make a small change right now:
#
# Task:
# Add the info() method
# It should output:
# Dog: Rex, age: 1

print('-' * 10, 'Task 2:', sep = '\n')

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'Dog: {self.name}, age: {self.age}')

dog = Dog('Rex', 2)

dog.info()

# Task 3
#
# Create 3 dogs with different details:
#
# Rex, 2 years old
# Bobby, 5 years old
# Luna, 1 year old
#
# And call info() for each one.

print('-' * 10, 'Task 3:', sep = '\n')

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'{self.name}, {self.age} years old')

dog1 = Dog('Rex', 2)
dog2 = Dog('Bobby', 5)
dog3 = Dog('Luna', 1)

dog1.info()
dog2.info()
dog3.info()

# Task 4
#
# Modify the class so that:
#
# the `age` variable cannot be modified directly
# create a method:
# `set_age(new_age)`
# And implement the following check:
# if `new_age` < 0 → display ‘Invalid age’
# and do not change the value

print('-' * 10, 'Task 4:', sep = '\n')

class Dog:
    def __init__(self, name, age):
        self.name = name
        if age < 0:
            print('Invalid age')
        else:
            self.__age = age

    def set_age (self, new_age):
        if new_age < 0:
            print('Invalid age')
        else:
            self.__age = new_age

    def info(self):
        print(f'{self.name}, {self.__age} years old')

dog1 = Dog('Rex', 2)
dog2 = Dog('Bobby', 5)
dog3 = Dog('Luna', 1)

dog1.set_age(19)

dog1.info()
dog2.info()
dog3.info()

# Task 5:
# Create a base class:
# class Animal:
#
# with a method:
#
# make_sound()
# Create:
# class Dog(Animal)
# class Cat(Animal)
# Implement:
# Dog → 'Woof'
# Cat → 'Meow'
# Create a list:
# animals
#
# and call:
#
# loop for

print('-' * 10, 'Task 5:', sep = '\n')

class Animal:
    def make_sound(self):
        print('Some sound')

class Dog(Animal):
    def make_sound(self):
        print('Woof')

class Cat(Animal):
    def make_sound(self):
        print('Meow')

animals = [Dog(), Cat()]

for animal in animals:
    animal.make_sound()

# Task 6
#
# Add:
#
# In 'Animal':
# def __init__(self, name):
#     self.name = name
# Use this name in 'Dog' and 'Cat'
# Modify 'make_sound()':
# print(f'{self.name}: Woof')
# Create:
# animals = [Dog('Rex'), Cat('Milo')]

print('-' * 10, 'Task 6:', sep = '\n')

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print('Some sound')

class Dog(Animal):
    def make_sound(self):
        print(f'{self.name}: Woof')


class Cat(Animal):
    def make_sound(self):
        print(f'{self.name}: Meow')

animals = [Dog('Rex'), Cat('Milo')]

for animal in animals:
    animal.make_sound()

# Task 7: Employee System
#
# Imagine you are building a system for a company.
#
# 1. Base class
#
# Create a class:
#
# Employee
# It must have:
# name
#
# Basic behaviour:
#
# calculate_salary()
#
# 2. Inheritance
#
# Create several types of employees:
#
# FullTimeEmployee
# PartTimeEmployee
# Freelancer
#
# 3. Salary logic (different for each)
# FullTimeEmployee:
# has a fixed monthly salary
# PartTimeEmployee:
# has an hourly rate
# and the number of hours worked
# Freelancer:
# is paid per project
# and the number of projects completed
# 4. Encapsulation (MANDATORY)
# make at least one variable ‘protected’
# add method(s) to modify data with validations
# (for example: negative hours / salary / projects cannot be set)
#
# 5. Polymorphism
#
# Create a list:
#
# employees = [...]
#
# with different types of employees
#
# And write a loop:
#
# for emp in employees:
#     print(emp.calculate_salary())

print('-' * 10, 'Task 7:', sep = '\n')

class Employee:

    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        raise NotImplementedError('Subclass must implement this method')

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return f'Employee {self.name}, salary: {3000}'

class PartTimeEmployee(Employee):
    def __init__(self, name, hours_worked):
        super().__init__(name)
        self.__hours_worked = hours_worked

    def calculate_salary(self):
        return f'Employee {self.name}, salary: {self.__hours_worked * 20}'

    def set_hours_worked(self, time):
        if time < 0:
            print('Enter positive integer')
        else:
            self.__hours_worked = time

class Freelancer(Employee):
    def __init__(self, name, number_project):
        super().__init__(name)
        self.number_project = number_project

    def calculate_salary(self):
        return f'Employee {self.name }, salary: {500 * self.number_project}'

employees = [FullTimeEmployee('John'), PartTimeEmployee('Will', 130), Freelancer('Martin', 3)]

for employee in employees:
    print(employee.calculate_salary())
