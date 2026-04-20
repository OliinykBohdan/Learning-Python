# Task 1
print('-' * 10, 'Task 1:', sep = '\n')

with open('C:\\Users\\Spirit\\PycharmProjects\\Python_learning\\Basics\\work_with_files_(test)\\test_1.txt', 'r') as file:
    data = file.read()
print(data)

# Task 2
print('-' * 10, 'Task 2:', sep = '\n')

file = open('C:\\Users\\Spirit\\PycharmProjects\\Python_learning\\Basics\\work_with_files_(test)\\test_2.txt', 'a')
hobby = input('Hobby: ')
file.write(hobby + '\n')
file.close()