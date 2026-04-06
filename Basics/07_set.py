# Methods covered: add(), remove(), intersection(), symmetric_difference(), difference()

numbers1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numbers2 = {4, 3433, 23, 32, 1, 34, 8, 6, 2, 3}

numbers1.add(11)
numbers2.remove(4)

print(numbers1)
print(numbers2)

# Elements present in both sets
result = numbers1.intersection(numbers2)
print(result)

# Elements unique to each set
result = numbers1.symmetric_difference(numbers2)
print(result)

# Elements only in numbers1
result = numbers1.difference(numbers2)
print(result)