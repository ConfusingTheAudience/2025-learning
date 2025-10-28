# ARITHMETICS & MATH

# 6. To add value to number you can simply do
friends = 0
friends = friends + 1
# or you can use add-and-assign operator instead
friends += 1
# these operators works for all others
friends -= 1
friends *= 3
friends /= 2
friends **= 2 # ** is exponentiation operator
remainder = friends % 2 # % is modulo operator

print(friends)
print(remainder)

# 7. Build in math related functions

x = 3.14
y = -4
z = 5

result = round(x) # returns 3
result2 = abs(y) # returns 4
result3 = pow(4, 3) # returns 64 (4*4*4)
result4 = max(x, y, z) # returns 5
result5 = min(x, y, z) # returns -4

# round() function rounds a value to the nearest  integer
#         If a second argument is given, it specifies
#         the number of decimal places
# abs() function find absolute value, value is the distance from 0 to that number
# pow() function returns the value of a number raised to the power of another number
# max() function gives us max value
# min() function gives us min value



# 8. Some useful values and functions from math class

# we need to import math module at the top

import math

x2 = 9
y2 = 9.1

print(math.pi) # pi value
print(math.e) # e value
result6 = math.sqrt(x2) # returns 3.0
result7 = math.ceil(y2) # returns 10
result8 = math.floor(y2) # returns 9

# ceil() function will always round floating number up
# floor() function will always round floating number down