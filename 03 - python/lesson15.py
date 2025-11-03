# MATCH-CASE STATEMENT (switch)

# 31. Switch

# example with if

def day_of_week(day):
    if day == 1:
        return 'It is Sunday'
    elif day == 2:
        return 'it is Monday'
    elif day == 3:
        return 'it is Tuesday'
    elif day == 4:
        return 'it is Wednesday'
    elif day == 5:
        return 'it is Thursday'
    elif day == 6:
        return 'it is Friday'
    elif day == 7:
        return 'it is Saturday'
    else:
        return 'Not valid day'
    
print(day_of_week(1))

# same example with switch

def day_of_week(day):
    match day:
        case 1:
            return 'It is Sunday'
        case 2:
            return 'it is Monday'
        case 3:
            return 'it is Tuesday'
        case 4:
            return 'it is Wednesday'
        case 5:
            return 'it is Thursday'
        case 6:
            return 'it is Friday'
        case 7:
            return 'it is Saturday'
        case _:
            return 'Not valid day'

print(day_of_week(7))

# match and _ to remember

# second example

def is_wekeend(day):
    match day:
        case 'Saturday' | 'Sunday':
            return True
        case 'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday':
            return False
        case _:
            return False
        
print(is_wekeend('Sunday'))