import os

BASE_DIR = os.path.dirname(__file__)
FILES_DIR = os.path.join(BASE_DIR, 'work_with_files_(test)')

data_file = os.path.join(FILES_DIR, 'data.txt')
output_file = os.path.join(FILES_DIR, 'output.txt')
notes_file = os.path.join(FILES_DIR, 'notes.txt')

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

print ('-' * 10, 'Task 1:', sep = '\n')

with open(data_file, 'r') as file:
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

with open(data_file, 'r') as file:
    for line in file:
        print(line)

# Task 3: Write to File
# Description:
#
# Task:
#
# create output.txt
# write 3 lines into it

print ('-' * 10, 'Task 3:', sep = '\n')

with open(output_file, 'w') as file:
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

with open(output_file, 'a') as file:
    file.write('Hobby football')

with open(output_file, 'r') as file:
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

with open(notes_file, 'a') as file:

    while True:
        notes = input('Notes or exit: ')
        if notes == 'exit':
            break
        else:
            file.write(notes + '\n')

# Task 6: Count Lines (Function)
#  Description:
#
# Create:
#
# def count_lines(filename):
#
#  Task:
#
# return number of lines

print('-' * 10, '\nTask 6:')

def count_lines(file_path):
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            count += 1
    return count

print('Number of lines:', count_lines(notes_file))

# Task 7: Count Words (Function)
# Description:
#
# Create:
#
# def count_words(filename):
#
#  Task:
#
# count all words in file
#  Hint:
# .split()

print('-' * 10, '\nTask 7:')

def count_words(filename):

    with open(filename, 'r') as file:
        text = file.read()
    words = text.split()
    return len(words)

print('Number of words:', count_words(notes_file))