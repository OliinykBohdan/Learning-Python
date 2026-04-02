# # Exercise 1

number = 1

while number <= 10:
    print(number)
    number += 1

# # Exercise 2

t_water = 30

while t_water < 100:
    print('Wait')
    t_water += 1
    print(t_water)

print('The water boiled')

# Exercise 3

result = 0

number_or_stop = input('Enter a number or stop: ')

while number_or_stop != 'stop':
    result += int(number_or_stop)
    number_or_stop = input('Enter a number or stop: ')

print(result)
