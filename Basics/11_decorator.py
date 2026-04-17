# Task 1

def decorator (func):
    def inner ():
        print('start')
        func()
        print('end')
    return inner

@decorator
def say_name1 ():
    print('Bohdan')

@decorator
def say_name2 ():
    print('Vika')

say_name1()

say_name2()

# Task 2

def decorator_1(func):
    def inner():
        print(10 * '~')
        func()
        print(10 * '~')
    return inner

def decorator_2(func):
    def inner():
        print(10 * '#')
        func()
        print(10 * '#')
    return inner

@decorator_2
@decorator_1
def func_1():
    print('Main content')

func_1()