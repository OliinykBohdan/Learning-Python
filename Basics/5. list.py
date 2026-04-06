numbers = [1,2,3,4,5,6,7,8,9]

print(numbers)

numbers.append(10)

print(numbers)

numbers.pop(0)

print(numbers)

other = [11,22,33]

del numbers[0]

numbers.extend(other)
# seems to work:
# numbers = numbers + other
print(numbers)

print(numbers[0])

numbers1 = [2,66,9,0,7,22,8,32]

numbers1.sort()

print(numbers1)

numbers1.reverse()

print(numbers1)