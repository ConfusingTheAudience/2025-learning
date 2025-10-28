# STRING METHODS

# 12 String methods

name = input('Enter your full name: ')

len(name) # returns 4 if user typed "John"
name.find('o') # returns 1 if user typed "Johno"
name.rfind('o') # returns 4 if user typed "Johno"
name.capitalize()
name.upper()
name.lower()
name.isdigit()
name.isalpha()
name.count('a')
name.replace('a', 'b')

# len() function gives length of a string (func returns integer)
#       it includes spaces too
# find() this method returns the first occurence of
#        a given character, the position of it
#        first character have index of 0
#        if there is no given character it returns -1
# rfind() this method returns the last occurence of
#        a given character, the position of it
#        if there is no given character it returns -1
# capitalize() this method capitalize first letter
# upper() this method uppercase all letters
# lower() this method lowercase all letters
# isdigit() returns true or false if a string contains only digits
# isalpha() returns true or false if a string contains only a-z
#           spacebar isn't alphabetical character!
#           it also return false if name have some digits
# count() counts how many times a given character occurs
# replace() replace any given charater to another

# type print(help(str)) to see full helpful string methods


# 13 String indexing = accessing elements of a sequence using []
#                      (indexing operator) [start : end : step]

credit_number = "1234-5678-9012-3456"

credit_number[0] # returns 1
credit_number[4] # returns -
credit_number[0:4] # returns 1234
credit_number[:4] # returns 1234 works same
# start index is always included (it gives 1)
# end index isn't included (it gives -)
credit_number[5:] # returns 5678-9012-3456
credit_number[-1] # returns 6 (the one in the end)
credit_number[-2] # returns 5 (the one on the end)
credit_number[::2] # returns 13-6891-46 (every second thing)