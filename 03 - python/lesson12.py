# Iterables = An object/collectino that can return its elements
#             one at a time, allowing it to be iterated over in a loop

numbers = [1, 2 ,3 ,4 ,5]

for number in numbers:
    print(number)

for number in reversed(numbers):
    print(number, end=' ')
# list are iterable

numbers = (1, 2 ,3 ,4 ,5)

for number in numbers:
    print(number)

# tuples are iterable

fruits = {'apple', 'orange', 'banana', 'coconut'}

for fruit in fruits:
    print(fruit)

# set object is not reversible

name = 'Ash Sque'

for character in name:
    print(character, end=' ')

my_dictionary = {'A': 1, 'B': 2, 'C': 3}

for key in my_dictionary:
    print(key) # get the keys from dictionary

for value in my_dictionary.values():
    print(value) # get the values from dictionary

for key, value in my_dictionary.items():
    print(key, value) # get the key and values both from dictionary

