# Exercise 1

students = ['Bohdan', 'Anton', 'Dima', 'Victoria']

for st in students:
    print(f'Student: {st} is here!')

print('Done')

# Exercise 2

n = int(input('Enter a number: '))

for i in range(1, n + 1):
    if i % 2 == 1:
        print(i)

print('Done')

# Exercise 3

for i in range(1, 10):
    for j in range(1, 11):
        print(f'{i} x {j} = {i * j}')