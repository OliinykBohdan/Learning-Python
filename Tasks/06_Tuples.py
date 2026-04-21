# Task 1: Access Elements
#
# You have a tuple:
#
# data = (10, 20, 30, 40)
#
# Print:
#
# the first element
# the last element

print('-' * 10, 'Task 1:', sep='\n')

data = (10, 20, 30, 40)

print('The first/last elements:', data[0], data[3])

# Task 2: Length
#
# You have a tuple:
#
# data = (5, 15, 25, 35, 45)
#
# Print the length of the tuple

print('-' * 10, 'Task 2:', sep='\n')

data = (5, 15, 25, 35, 45)

print('Length:', len(data))

# Task 3: Loop Through Tuple
#
# You have a tuple:
#
# data = ('a', 'b', 'c')
#
# Print all elements using a for loop

print('-' * 10, 'Task 3:', sep='\n')

data = ('a', 'b', 'c')

for i in data:
    print(i)

# Task 4: Count Element
#
# You have a tuple:
#
# data = (1, 2, 2, 3, 2, 4)
#
# Count how many times the number 2 appears
# without using .count()

print('-' * 10, 'Task 4:', sep='\n')

data = (1, 2, 2, 3, 2, 4)

number_2 = 0

for number in data:
    if number == 2:
        number_2 += 1

print('Number 2 appears:', number_2)

# Task 5: Find Maximum
#
# You have a tuple:
#
# data = (10, 5, 20, 3)
#
# Find the largest number
# without using max()

print('-' * 10, 'Task 5:', sep='\n')

data = (10, 5, 20, 3)

largest_number = data[0]

for number in data:
    if number > largest_number:
        largest_number = number

print('Largest number:', largest_number)

# Task 6: Tuple → List
#
# You have a tuple:
#
# data = (1, 2, 3, 4)
#
# Convert it to a list
# Add number 5
# Print the result

print('-' * 10, 'Task 6:', sep='\n')

data = (1, 2, 3, 4)

list1 = []

for number in data:
    list1.append(number)

list1.append(5)

print('Converted list:', list1)

# or
#
# list1 = list(data)
#
# list1.append(5)
#
# print('Converted list:', list1)

# Task 7: Unpack Tuple
# Given a tuple:
# (10, 20, 30)
#
# Task:
# unpack into variables:
# a, b, c

print('-' * 10, 'Task 7:', sep='\n')

numbers = (10, 20, 30)
a, b, c = numbers

print('a:', a,'b:',  b, 'c:', c)

# Task 8: Swap Values
# Given:
# a = 5
# b = 10
#
# Task:
# swap values
# without using a temporary variable

print('-' * 10, 'Task 8:', sep='\n')

a = 5
b = 10

a, b = b, a

print('a:', a, 'b:', b)