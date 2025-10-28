# Exercise 1 Validate user input
# * username is no more than 12 characters
# * username must not contain spaces
# * username must not contain digits

username = input('Enter your username: ')

username_length = len(username)
username_spaces = username.count(" ")
username_noDigits = username.isalpha()

if username_length <= 12 and username_spaces == 0 and username_noDigits:
    print(f'Hello {username}')
else:
    print('Try again')


# Exercise 2 Show last 4 digits of credit card number

credit_number = "1234-5678-9012-3456"

last_digits = credit_number[15:]

print(f'XXXX-XXXX-XXXX-{last_digits}')

# Exercise 3 Reverse characters in the string

credit_number2 = "1234-5678-9012-3456"

credit_number2 = credit_number2[::-1]

print(credit_number2)