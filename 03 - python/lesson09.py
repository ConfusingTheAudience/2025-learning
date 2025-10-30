# COLLECTION = single "variable" used to store multiple values

# List    =  []  ordered and changeable. Duplicates OK
# Set     =  {}  unordered and immutable, but Add/Remove OK. NO duplicates
# Tuples  =  ()  ordered and unchangeable. Duplicates OK. FASTER


# 18. List []
fruits = ['apple', 'orange', 'banana', 'coconut']

print(fruits[0]) # returns apple
print(fruits[0:3]) # returns ['apple', 'orange', 'banana']
print(fruits[:3]) # returns ['apple', 'orange', 'banana']
print(fruits[::2]) # returns ['apple', 'banana']
print(fruits[::-1]) # returns list backwards

for fruit in fruits:
    print(fruit)

# print(dir(fruits)) # show methods
# print(help(fruits)) # these 2 works for all

print(len(fruits)) # show length of list
print('apple' in fruits) # to find something in list
#                          it's working in other collections too

fruits[0] = 'pineapple' # change one value working

fruits.append('pear') # add element to the end of the list
fruits.remove('pear') # remove the element from the list
fruits.insert(0, "grape") # add element on the specific index
fruits.sort() # sort list a-z
fruits.reverse() # it's reversed to the order we put them in list!
#                  or if we want to sort z-a we can first use .sort()
#                  and then use .reverse()
fruits.index('grape') # return index of element in list
fruits.count('banana') # count how many bananas are in list
fruits.clear() # clear list, elements are gone


# 19. Set {}

fruits = {'apple', 'orange', 'banana', 'coconut', 'coconut'}

print(fruits) # everytime I run program order would be diffrent
print(len(fruits)) # show length of set
print('apple' in fruits) # to find something in set

# print(fruits[0]) - This does not work in set

fruits.add("pinneaple") # add pinneaple to set
fruits.remove("pinneaple") # remove pinneaple from set
fruits.pop() # remove first element from set (it's random because
#              set first element is random every program start)
fruits.clear() # clear set, elements are gone

# if we have second coconut in set - on run it wouldn't be displayed!


# 20. Tuples ()

fruits = ('apple', 'orange', 'banana', 'coconut', 'coconut')

print(len(fruits)) # show length of tuple
print('apple' in fruits) # to find something in tuple

fruits.index('apple') # return index of element in tuple
fruits.count('coconut') # count how many coconuts are in tuple
# We can't append in tuples

for fruit in fruits:
    print(fruit)


# 21. 2D Collections

fruits = ['apple', 'orange', 'banana', 'coconut', 'coconut']
vegetables = ['celery', 'carrots', 'potatoes']
meats = ['chicken', 'fish', 'turkey']

groceries = [fruits, vegetables, meats]

print(groceries[0]) # returns only fruits row
print(groceries[0][0]) # returns apple

for collection in groceries:
    for food in collection:
        print(food) # return every single element of collection

# you can also mix 2d collections for example:
#groceries = [('apple', 'orange', 'banana', 'coconut', 'coconut'),
#             ('celery', 'carrots', 'potatoes'),
#             ('chicken', 'fish', 'turkey')]


# 22. Dictionary = a collection of {key:value} pairs
#                  ordered and changeable. NO duplicates

capitals = {'USA': 'Washington D.C', 
            'India': 'New Delhi', 
            'China':'Beijing', 
            'Russia': 'Moscow'}

capitals.get('USA') # get the value from dictionary
#                     if there is no such key it will return None

if capitals.get('Japan'):
    print('That capital exists')
else:
    print("That capital doesn't exist")

capitals.update({'Germany': 'Berlin'}) # update instert new pair
#                                        or update existing one
capitals.update({'USA': 'Detroit'}) # this is updated

capitals.pop('China') # remove key value pair
capitals.popitem() # remove latest key value pair
capitals.clear() # remove all key value pairs


capitals.keys() # get all the keys from dictionary
#                 it will return all keys but technically
#                 keys is an object which resembles list

for key in capitals.keys():
    print(key)


capitals.values() # get all values from dictionary
#                   return object which resembles list


for value in capitals.values():
    print(value)



capitals.items() # returns dicionary object which resembles
#                  2D list of tupples

for key, value in capitals.items():
    print(f'{key}: {value}')