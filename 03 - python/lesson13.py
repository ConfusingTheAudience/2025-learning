# Membership operators = used to test whetever a value or variable is found
#                        in a sequence (string, list, tuple, set or dictionary)
#                        1. in
#                        2. not in

#29. Membership operators

# example 1

word = 'APPLE'

letter = input('Guess a letter in the secret word: ')

# if in use
if letter in word:
    print(f'There is a {letter}')
else:
    print(f'{letter} was not found')

# if not in use
if letter not in word:
    print(f'{letter} was not found')
else:
    print(f'There is a {letter}')


# example 2

grades = {'Sandy': 'A',
          'Sque': 'B',
          'Ron': 'C'}

student = input('Enter the name of a student: ')

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f'{student} was not found')

#example 3

email = 'randomemail@gmail.com'

if '@' in email and '.' in email:
    print('Valid email')
else:
    print('Invalid email')


