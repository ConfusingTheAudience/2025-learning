# Exercise 1 Function to generate phone number

def get_phone(country, area, first, last):
    return f'{country}-{area}-{first}-{last}'

phone_num = get_phone(country=1, area=123, first=456, last=7890)

print(phone_num)

# Exercise 2 Args and kwargs togheter

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=' ')
    print()
    
    if 'apt' in kwargs:
        print(f'{kwargs.get('street')} {kwargs.get('apt')}')
    elif 'pobox' in kwargs:
        print(f'{kwargs.get('street')}')
        print(f'{kwargs.get('pobox')}')
    else:
        print(f'{kwargs.get('street')}')
        
    print(f'{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}')

shipping_label('Dr.', 'Ash', 'Sque', 'III',
               street='123 Fake St.',
               pobox='PO box #1001',
               city='Detroit',
               state='MI',
               zip='54321')