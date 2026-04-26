# Task 1 Create variables:
# a = 2 (int)
# b = 5.3 (float)
# c = '5' (str)
# Print the type of each variable using type()
# Perform operations:
# a + b
# a - b
# a * b
# a / b
#
# Question:
# What is the result type in each operation?

a = 2
b = 5.3
c = '5'

print('Integer: ', type(a), 'Float: ', type(b), 'String: ', type(c), sep='\n')
print('Addition: ', a+b, 'Subtraction: ', a-b, 'Multiplication: ', a*b, 'Division: ', a/b, sep='\n')

# What is the result type in each operation? Float


# Task 2 Convert:
# c (string '5') to a number
# a to float
#
# Perform calculation:
# result = a + int(c)
#
# Question:
# What happens if you do a + c without conversion?

Add = float(a) + int(c)

print(Add)

# What happens if you do a + c without conversion? There will be a "TypeError"


# Task 3 Given:
# x = 10
# y = 3
#
# Find:
# regular division /
# floor division //
# remainder %
# power
#
# Explain the difference between:
# / and //
# % and //

x = 10
y = 3

print('Division: ', x / y, 'Division to an integer: ', x // y, 'Remainder from division: ', x % y, '', 'Power: ', x ** y, sep='\n')

# Explanation of the difference between:
# / and // - the first is regular division, the second is floor division (rounds down)
# % and // - the first shows the remainder of division, the second shows how many times one number fits into another