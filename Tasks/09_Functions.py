# Task 1: Simple Function
# Description:
#
# Create a function that:
#
# takes a name as a parameter
# prints: 'Hello, <name>!'

print('-' * 10, 'Task 1:', sep='\n')

def name(x):
    print(f'Hello, {x}!')

name('Bohdan')

# Task 2: Return Sum
#  Description:
#
# Create a function that:
#
# takes two numbers
# returns their sum
#
# Print the result outside the function

print('-' * 10, 'Task 2:', sep='\n')

def sum_numbers(x, y):
    return x + y

print(sum_numbers(7, 9))
print(sum_numbers(10, 2))

# Task 3: Even or Odd (Function)
# Description:
#
# Create a function that:
#
# takes a number
# returns 'even' or 'odd'
#
# Use return, not print

print('-' * 10, 'Task 3:', sep='\n')

def number(x):
    if x % 2 == 1:
        return 'odd'
    else:
        return 'even'

print(number(12))
print(number(11))

# Task 4: Max of Three
# Description:
#
# Create a function that:
#
# takes three numbers
# returns the largest number
#
# Do NOT use max()

print('-' * 10, 'Task 4:', sep='\n')

def largest_number (x, y, z):
    if x > y and x > z:
        return x
    elif y > z:
        return y
    else:
        return z

print(largest_number(50, 60, 100))
print(largest_number(10, 1700, 220))

# Task 5: Shopping Cart Total (Function)
# Description:
#
# You have:
#
# cart = {
#     'apple': 2,
#     'banana': 3
# }
#
# price = {
#     'apple': 3,
#     'banana': 2
# }
#
# Create a function that:
#
# takes cart and price
# returns total price
#
# Call the function and print result

print('-' * 10, 'Task 5:', sep='\n')

cart = {
    'apple': 2,
    'banana': 3
}
price = {
    'apple': 3,
    'banana': 2
}

def total_price(x, y):
    total = 0
    for key, value in x.items():
        total += value * y[key]
    return total

print (total_price(cart, price))

# Task 6: Password Check (Function + Loop)
# Description:
#
# Create a function that:
#
# asks the user for a password
# has 3 attempts
#
# Rules:
#
# correct → return 'Access granted'
# wrong → ask again
# after 3 attempts → return 'Access denied'

print('-' * 10, 'Task 6:', sep='\n')

def passwords ():
    attempts = 0
    while True:
        x = input('Enter password: ')

        if x == '1111':
            return 'Access granted'
        else:
            attempts += 1
            print('Incorrect password')

        if attempts == 3:
            return 'Access denied'

print(passwords())