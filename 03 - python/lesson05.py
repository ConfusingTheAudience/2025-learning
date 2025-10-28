# CONDITIONAL EXPRESSION = A one line shortcut for the if else statement (ternary operator)

# 11. Conditional Expression = X if condition else Y

num = 5
a = 6
b = 7

print('Positive' if num > 0 else 'Negative') # returns Positive
max_num = a if a > b else b
print(max_num) # returns 7