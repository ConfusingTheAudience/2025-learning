# IF STATEMENT

# 9. If, elif, else

age = int(input('Enter your age: '))

if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print('You are now signed up!')
elif age < 0:
    print("You haven't been born yet!")
else:
    print('You must be 18+ to sign up')

# You should be aware of if elif order to execute properly

name = input('Enter your name: ')

if name == "":
    print('You did not type in your name!')
else:
    print(f'Hello {name}')
