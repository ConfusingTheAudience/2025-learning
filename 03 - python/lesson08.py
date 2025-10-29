# LOOPS

# 15. While loop examples

name = input('Enter your name: ')

while name == '':
    print('You did not enter your name')
    name = input('Enter your name: ')
print(f'Hello {name}')



age = int(input('Enter your age: '))

while age <= 0:
    print("Age can't be negative")
    age = int(input('Enter your age: '))

print(f'You are {age} years old')



food = input('Enter a food you like (q to quit): ')

while not food == 'q':
    print(f'You like {food}')
    food = input('Enter another food you like (q to quit): ')

print('bye')



num = int(input('Enter a number between 1 - 10: '))

while num < 1 or num > 10:
    print(f'{num} is not valid')
    num = int(input('Enter a number between 1 - 10: '))

print(f'Your number is {num}')

# 16. For loop examples

for x in range(1, 11):
    print(x) # returns 1 to 10

for x in reversed(range(1, 11)):
    print(x) # returns 10 to 1 

for x in range(1, 11, 2):
    print(x) # returns 1,3,5,7,9 (because step 2 used)



for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x) # returns numbers 1 to 20 but skip 13

for x in range(1,21):
    if x == 13:
        break
    else:
        print(x) # returns numbers 1 to 12

# 17. Nested Loops



for x in range(3):
    for y in range(1,10):
        print(y, end="") # returns 123456789
    print() # returns 123456789 3 times in new line

# I need to rename second counter to have diffrent name (x, y)
# end="" specifies what will be printed at the end of each print call
# By default, print() ends with a newline "\n"
# It's necessary for drawing shapes like rectangles in nested loops