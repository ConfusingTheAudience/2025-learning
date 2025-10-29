# FORMAT SPECIFIERS = {value:flags} format a value based on what
#                     flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

# 14. Format specifiers examples

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f'Price 1 is ${price1:.2f}') # returns $3.14
print(f'Price 2 is ${price2:10}') # returns $   -987.65
print(f'Price 3 is ${price3:010}') # returns $0000012.34
print(f'Price 3 is ${price3:<10}') # returns $12.34     | (end)

print(f'Price 1 is ${price1:+}') # returns $+3.14159
print(f'Price 2 is ${price2:+}') # returns $-987.65
print(f'Price 3 is ${price3:+}') # returns $+12.34

price4 = 3000.14159
price5 = -9870.65
price6 = 1200.34

print(f'Price 4 is ${price4:+,.2f}') # returns $+3,000.14
print(f'Price 5 is ${price5:+,.2f}') # returns $-9,870.65
print(f'Price 6 is ${price6:+,.2f}') # returns $+1,200.34
