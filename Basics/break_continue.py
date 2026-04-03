# Exercise 1

students = ['Bohdan', 'Anton', 'Marina', 'Victoria', 'Oleg']

for i in students:
    if i == 'Victoria':
        print('Found')
        break
    else:
        print('This is not Victoria')

print('Done')

# Exercise 2

students = ['Bohdan', 'Anton', 'Marina', 'Victoria', 'Oleg']

for i in students:
    if i == 'Victoria':
      continue
    print(i)

print('Done')

# Exercise 3

for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)

# Exercise 4

result = 0

while True:
    number = input('Enter a number or stop: ')
    if number == 'stop':
        print(result)
        break
    result += int(number)
