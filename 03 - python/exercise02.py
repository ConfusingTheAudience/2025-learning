# Exercise 1 Calculate the circumference of a circle

import math

radius = float(input('Enter the radius of a circle: '))

circumference = 2 * math.pi * radius

print(f'The circumference is: {round(circumference, 2)}cm')



# Exercise 2 Calculate the area of a circle

radius2 = float(input('Enter the radius of a cricle: '))

area = math.pi * pow(radius2, 2)

print(f'The area of the circle is: {round(area, 2)}cm²')



# Exercise 3 Find the hypotenuse of a right trangle

a = float(input('Enter side A: '))
b = float(input('Enter side B: '))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f'Side C = {c}')