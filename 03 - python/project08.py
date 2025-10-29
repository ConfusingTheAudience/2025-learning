# Compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input('Enter the principle amount: '))
    if principle <= 0:
        print("principle can't be less than or equal to zero")

while rate <= 0:
    rate = float(input('Enter the interest rate: '))
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero")

while time <= 0:
    time = int(input('Enter the time in years: '))
    if time <= 0:
        print("Time can't be less than or equal to zero")

total = principle * pow((1 + rate / 100), time)

print(f'Balance after {time} years/s: ${total:.2f}')

# another version 
# I need to break out of the loop to prevent infinite loop
# benefit is that I can enter 0

# while True:
#     time = int(input('Enter the time in years: '))
#     if time < 0:
#         print("Time can't be less than zero")
#     else:
#         break



# Countdown timer

import time

# time.sleep(3)          program sleep for 3 seconds
# print('Time is up!')   it shows after 3 seconds


my_time = int(input('Enter the time in seconds: '))

for x in range(my_time, 0, -1): # technique to count backwads
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) # % 24 if we have days available
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
    time.sleep(1)

print('Time is up!')




# Rectangle with nested loops

rows = int(input('Enter the number of rows: '))
columns = int(input('Enter the number of columns: '))
symbol = input('Enter a symbol to use: ')

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
