# Task 1: Print All Elements
#
# You have a list:
#
# numbers = [1, 2, 3, 4, 5]
#
# Print all elements of the list using a for loop

print('\nTask 1:')

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

# Task 2: Sum of List
#
# You have a list:
#
# numbers = [2, 4, 6, 8]
#
# Find the sum of all elements (without using sum())

print('\nTask 2:')

numbers = [2, 4, 6, 8]

total = 0

for number in numbers:
    total += number

print('Sum of all elements:', total)

# Task 3: Find Maximum
#
# You have a list:
#
# numbers = [10, 3, 7, 25, 1]
#
# Find the largest number (without using max())

print('\nTask 3:')

numbers = [10, 3, 7, 25, 1]

largest_number = numbers[0]

for number in numbers:
    if number > largest_number:
        largest_number = number

print('The largest of the number:', largest_number)

# Task 4: Filter Even Numbers
#
# You have a list:
#
# numbers = [1, 2, 3, 4, 5, 6]
#
# Create a new list with only even numbers

print('\nTask 4:')

numbers = [1, 2, 3, 4, 5, 6]

numbers_even = []

for number in numbers:
    if number % 2 == 0:
        numbers_even.append(number)

print('Even numbers of the list:', numbers_even)

# Task 5: Count Occurrences
#
# You have a list:
#
# numbers = [1, 2, 2, 3, 2, 4]
#
# Count how many times the number 2 appears

print('\nTask 5:')

numbers = [1, 2, 2, 3, 2, 4]

number2 = 0

for number in numbers:
    if number == 2:
        number2 += 1

print('Number 2 appears of the list:', number2)

# Task 6: Reverse List
#
# You have a list:
#
# numbers = [1, 2, 3, 4, 5]
#
# Create a new list in reverse order
# without using reverse() and without slicing [::-1]

print('\nTask 6:')

numbers = [1, 2, 3, 4, 5]

reversed_list = []

for number in range (4, -1, -1):
    reversed_list.append(numbers[number])

print('Reversed list:', reversed_list)