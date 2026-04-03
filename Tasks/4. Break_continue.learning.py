# Task 1: Stop at Number (break)
# #
# # Print numbers from 1 to 10.
# # When the number equals 5 — stop the loop.

for i in range(1, 11):
    if i == 5:
        break
    print(i)

# # Task 2: Skip Number (continue)
# #
# # Print numbers from 1 to 10,
# # but skip number 5.

for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# Task 3: First Negative Number (break)
#
# You have a list:
#
# numbers = [3, 7, 2, -5, 10, -1]
# #
# # Go through the list and:
# #
# # when you find the first negative number
# # print it and stop the loop

numbers = [3, 7, 2, -5, 10, -1]

for number in numbers:
    if number < 0:
        print(number)
        break


# # Task 4: Skip Negative Numbers (continue)
# #
# # You have a list:
# #
# # numbers = [3, -2, 5, -1, 7]
# #
# # You need to print only positive numbers

numbers = [3, -2, 5, -1, 7]

for number in numbers:
    if number < 0:
        continue
    print(number)

# Task 5: Password with Limit (break)
#
# Password: '1234'
#
# The user has 3 attempts:
#
# if the password is correct → print 'Access granted' and stop (break)
# if not → print 'Wrong password'
# if all 3 attempts are used → print 'Access denied'


attempts = 0
password = '1234'

while attempts < 3:
    passw = input('Enter your password: ')

    if passw == password:
        print ('Access granted')
        break
    else:
        print('Wrong password')
    attempts += 1

if attempts == 3:
    print('Access denied')

# Task 6 (challenge): Guess with Exit
#
# Set a number (for example 7).
# The user tries to guess it:
#
# if the user enters 'exit' → stop the program (break)
# if the guess is wrong → print 'Too high' or 'Too low'
# if correct → print 'You win!'

secret = '7'

while True:
    number = input('Enter a number or exit: ')
    if number == 'exit':
        break
    elif number == secret:
        print('You win!')
        break
    elif int(number) > int(secret):
        print('Too high')
    elif int(number) < int(secret):
        print('Too low')


