# Calculator

operator = input('Enter an operator (+ - * /): ')
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))

if operator == '+':
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
    pass
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f'{operator} is not a valid operator')



# Weight converter

weight = float(input('Enter your weight: '))
unit = input('Kilograms or Pounds? (K or L): ')

if unit == 'K':
    weight = weight * 2.205
    unit = 'Lbs.'
    print(f'Your weight is: {round(weight, 1)} {unit}')
elif unit == 'L':
    weight = weight / 2.205
    unit = 'Kgs.'
    print(f'Your weight is: {round(weight, 1)} {unit}')
else:
    print(f'{unit} was not valid')



# Temperature converter

unit2 = input('Is this temperature in Celcius or Farenheit (C/F): ')
temp = float(input('Enter the temperature: '))

if unit2 == 'C':
    temp = round((9 * temp) / 5 + 32, 1)
    print(f'The temperature in Farenheit is: {temp}F')
elif unit2 == 'F':
    temp = round((temp - 32) * 5 / 9, 1)
    print(f'The temperature in Celsius is: {temp}C')
else:
    print(f'{unit2} is an invalid unit of measurement')