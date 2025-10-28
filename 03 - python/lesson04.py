# LOGICAL OPERATORS

# 10. Or, and, not

# or = at least one condition must be True
# and = both conditions must be True
# not = inverts the condition (not False, not True)

temp = 30
is_raining = False
is_sunny = True

# or
if temp > 35 or temp < 0 or is_raining:
    print('The outdoor event is cancelled')
else:
    print('The outdoor event is still sheduled') # returns this
    
# and
if temp >= 28 and is_sunny:
    print('It is sunny') # returns this
else:
    print('It is not sunny')
    
# not
if temp >= 28 and not is_sunny:
    print('It is sunny')
else:
    print('It is not sunny') # returns this