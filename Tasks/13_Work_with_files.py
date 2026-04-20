# Task 1: Read File (Base)
# Description:
#
# Create a file data.txt:
#
# Hello
# World
# Python
#
# Task:
#
# open the file
# read all content
# print it
from itertools import count

print ('-' * 10, 'Task 1:', sep = '\n')

with open('C:\\Users\\Spirit\\PycharmProjects\\Python_learning\\Tasks\\work_with_files_(test)\\data.txt', 'r') as file:
    data = file.read()
print(data)

# Task 2: Read Line by Line
# Description:
#
# Task:
#
# read file using a loop
# print each line separately

print ('-' * 10, 'Task 2:', sep = '\n')

with open('C:\\Users\\Spirit\\PycharmProjects\\Python_learning\\Tasks\\work_with_files_(test)\\data.txt', 'r') as file:
    for i in file.read():
        print(i)

# Task 3: Write to File
# Description:
#
# Task:
#
# create output.txt
# write 3 lines into it

print ('-' * 10, 'Task 3:', sep = '\n')

with open('C:\\Users\\Spirit\\PycharmProjects\\Python_learning\\Tasks\\work_with_files_(test)\\output.txt', 'w') as file:
    file.write('Portfolio:\n' + 'Name Bohdan\n' + 'Age 30\n')

# Task 4: Append to File
# Description:
#
# Task:
#
# open output.txt
# add "New line"
# print updated content

print('-' * 10, '\nTask 4:')

with open('C:\\Users\\Spirit\\PycharmProjects\\Python_learning\\Tasks\\work_with_files_(test)\\output.txt', 'a') as file:
    file.write('Hobby football')

with open('C:\\Users\\Spirit\\PycharmProjects\\Python_learning\\Tasks\\work_with_files_(test)\\output.txt', 'r') as file:
    portfolio = file.read()
    print(portfolio)

# Task 5: Save User Input
# Description:
#
# Task:
#
# ask user for text
# save it to notes.txt
# loop until user enters "exit"
# each input → new line

print('-' * 10, '\nTask 5:')

with open('C:\\Users\\Spirit\\PycharmProjects\\Python_learning\\Tasks\\work_with_files_(test)\\notes.txt', 'a') as file:

    while True:
        notes = input('Notes or exit: ')
        if notes == 'exit':
            break
        else:
            file.write(notes + '\n')