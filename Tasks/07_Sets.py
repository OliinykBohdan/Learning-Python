# Task 1: Create Unique List
#
# You have a list:
#
# numbers = [1, 2, 2, 3, 4, 4, 5]
#
# Get only unique values using set
# Convert it back to a list
# Print the result

print('\nTask 1:')

numbers = [1, 2, 2, 3, 4, 4, 5]
numbers_set = set(numbers)
numbers = list(numbers_set)

print(numbers)

# or
# unique_numbers = list(set(numbers))
#
# print(unique_numbers)

# Task 2: Add Elements
#
# You have a set:
#
# nums = {1, 2, 3}
#
# Add numbers 4 and 5
# Print the result

print('\nTask 2:')

nums = {1, 2, 3}

nums.add(4)
nums.add(5)

print(nums)

# Task 3: Remove Elements
#
# You have a set:
#
# nums = {1, 2, 3, 4, 5}
#
# Remove number 3
# Print the result

print('\nTask 3:')

nums = {1, 2, 3, 4, 5}
nums.remove(3)

print(nums)

# Task 4: Common Elements (Intersection)
# Task 4: Common Elements (Intersection)
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
#
# 👉 Find the common elements
#
# Find the common elements

print('\nTask 4:')

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = set1.intersection(set2)

print(set3)

# Task 5: Difference
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
#
# Find elements that are in set1 but not in set2

print('\nTask 5:')

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = set1.difference(set2)

print(set3)

# Task 6: Loop Through Set
#
# You have a set:
#
# nums = {10, 20, 30}
#
# Print all elements using a for loop

print('\nTask 6:')

nums = {10, 20, 30}

for num in nums:
    print(num)

# Task 7: Remove Duplicates WITHOUT set()
#
# You have a list:
#
# numbers = [1, 2, 2, 3, 4, 4, 5]
#
# Create a new list without duplicates
# do NOT use set()

print('\nTask 7:')

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)