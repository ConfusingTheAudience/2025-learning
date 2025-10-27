# 1. This is comment in python

# 2. Print message to the console
print('Hello World')

# 3. Variables - (string, integer, float, boolean)

# string
first_name = 'Tod'
# integer
my_age = 20
# float
price = 9.80
# boolean
is_legal = True
is_adult = False

# to print value
print(first_name)
# if statement example with boolean values
if is_legal:
    print('This is legal')
else:
    print('This is not legal')

# 3.1 - fstring (let you add variables to the text)
print(f'My name is {first_name}')

# 4. Typecasting - the process of converting a variable from one data type to another str(), int(), float(), bool()

name = 'Daniel Carter'
sec_name = ''
age = 25
gpa = 2.1
is_student = True

print(type(name)) # returns <class 'str'>
print(type(age)) # returns <class 'int'>
print(type(gpa)) # returns <class 'float'>
print(type(is_student)) # returns <class 'bool'>

# converting to another type
gpa = int(gpa)
print(gpa) # returns 2
age = float(age)
print(age) # returns 25.0
name = bool(name)
sec_name = bool(sec_name)
print(name) # returns True when string isn't empty
print(sec_name) # returns False if string have no characters

# 5. input() - A function that prompts the user to enter data
#              Returns the entered data as a string

your_name = input('What is your name?: ')
your_age = input('How old are you?: ')

# your_age is returned as string and we cannot add string to integer so we need to typecast it to integer
your_age = int(your_age)
your_age = your_age + 1

# another shorter way to typecast is to do:
# your_age = int(input('How old are you?: '))

print(f'Hello {your_name}')
print('HAPPY BRITHDAY')
print(f'You are {your_age} years old')

