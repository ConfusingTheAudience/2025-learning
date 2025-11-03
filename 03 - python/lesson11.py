# FUNCTION - 1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

# 23. Basic functions - def to define function and () to invoke

def simple_message():
    print('First message')
    print('Second message')

simple_message()
simple_message()

def happy_birthday(name, age):
    print(f'Hello {name}')
    print('Happy birthday')
    print(f'You are {age} years old')

happy_birthday('Ron', 30)
happy_birthday('Steve', 20)
# order with passing arguments to function is important

# 24. return statement

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1,2))
print(subtract(1,2))
print(multiply(1,2))
print(divide(1,2))


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + ' ' + last

full_name = create_name('ash', 'sque')

print(full_name) # returns Ash Sque

# 25. Default arguments

def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 0.1, 0))
# when you pass arguments you can switch the deafult ones with yours


import time

def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print('DONE!')

count(10)
# you need to make sure you do default arguments after positional arguments

# 26. Keyword arguments = an argument preceded by an indentifier
#                         helps with readability
#                         order of arguments doesn't matter

def hello(greeting, title, first, last):
    print(f'{greeting} {title} {first} {last}')

hello('Hello', first='Adam', last='Smith', title='Mr.')
# you need to make sure position arguments are first
# if you mix it with keywords

# examples of keywords
for x in range(1, 11):
    print(x, end=' ') # in this example end is a keyword

print('1', '2', '3', '4', '5', sep='-') # in this example sep is a keyword

# 27. Arbitrary arguments

# *args                  = allows you to pass multiple non-key arguments
# **kwargs               = allows you to pass multiple keyword-arguments
#                        * unpacking operator

# args

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(1, 2, 3))
# when I'm using args it becomes tuple

def display_name(*args):
    for arg in args:
        print(arg, end = ' ')

display_name('Dr.', 'Ash', 'Sque', 'III')

# kwargs

def print_address(**kwargs):
    for  key, value in kwargs.items():
        print(f'{key}: {value}')

print_address(street='123 Fake St.',
              apt='100',
              city='Detroit',
              state='MI',
              zip='54321')
# when I'm using kwargs it becomes dictionary


# both in args and kwargs you can put your own name like nums etc