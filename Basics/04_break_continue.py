# Task 1

print('-' * 10, 'Task 1:', sep='\n')

students = ['Bohdan', 'Anton', 'Marina', 'Victoria', 'Oleg']

for i in students:
    if i == 'Victoria':
        print('Found')
        break
    else:
        print('This is not Victoria')

print('Result: done')

# Task 2

print('-' * 10, 'Task 2:', sep='\n')

students = ['Bohdan', 'Anton', 'Marina', 'Victoria', 'Oleg']

for i in students:
    if i == 'Victoria':
      continue
    print(i)

print('Result: done')

# Task 3

print('-' * 10, 'Task 3:', sep='\n')

for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)

print('Result: done')

# Task 4

print('-' * 10, 'Task 4:', sep='\n')

result = 0

while True:
    number = input('Enter a number or stop: ')
    if number == 'stop':
        print('Addition result:', result)
        break
    result += int(number)
