# List comprehension  = A concise way to create lists in Python
#                       Compact and easier to read than traditional loops
#                       [expression for value in iterable if condition]

# 30. List comprehension

# normally we can do it like this
doubles = []
for x in range(1,11):
    doubles.append(x * 2)

print(doubles)

# list comprehension is shorter way instead to have same result
doubles = [x * 2 for x in range(1,11)]
print(doubles)

fruits = [fruit.upper() for fruit in ['apple', 'orange', 'banana']]
print(fruits)
# you can cut down one of the steps

fruits = ['apple', 'banana', 'orange', 'coconut']
fruits_char = [fruit[0] for fruit in fruits]
print(fruits_char)

numbers = [1, -2, 3, -4, 5, -6]
positive_nums = [num for num in numbers if num >= 0]
print(positive_nums)
negative_nums = [num for num in numbers if num < 0]
print(negative_nums)
even_nums = [num for num in numbers if num % 2 == 0]
print(even_nums)
# even if we didn't modife expression we still need to use it like just
# by saying num
# on the other hand if condition is optional