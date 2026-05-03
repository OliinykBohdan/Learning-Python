# Task 1

print('-' * 10, 'Task 1:', sep='\n')

students = ['Bohdan', 'Anton', 'Dima', 'Victoria']

for st in students:
    print(f'Student: {st} is here!')

print('Result: done')

# Task 2

print('-' * 10, 'Task 2:', sep='\n')

n = int(input('Enter a number: '))

for i in range(1, n + 1):
    if i % 2 == 1:
        print(i)

print('Result: done')

# Task 3

print('-' * 10, 'Task 3:', sep='\n')

for i in range(1, 10):
    for j in range(1, 11):
        print(f'{i} x {j} = {i * j}')

print('Result: done')
