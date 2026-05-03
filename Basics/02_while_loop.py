# Task 1

print('-' * 10, 'Task 1:', sep='\n')

number = 1

while number <= 10:
    print(number)
    number += 1

print('Result: done')

# Task 2

print('-' * 10, 'Task 2:', sep='\n')

t_water = 30

while t_water < 100:
    print('Wait')
    t_water += 1
    print(t_water)

print('The water boiled')

# Task 3

print('-' * 10, 'Task 3:', sep='\n')

result = 0

number_or_stop = input('Enter a number or stop: ')

while number_or_stop != 'stop':
    result += int(number_or_stop)
    number_or_stop = input('Enter a number or stop: ')

print('Addition result:', result)
