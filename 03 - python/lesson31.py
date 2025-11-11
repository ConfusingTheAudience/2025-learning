# WRITING FILES (.txt, .json, .csv)

# 52. Write to .txt file


txt_data = 'added random text'

file_path = '03 - python/lesson31example1.txt'

try:
    with open(file_path, 'a') as file:
        file.write('\n' + txt_data)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print('That file already exists!')



# with is a statement it's used to wrap a block of code to execute
# if we open a file the with also close that file when we're done with it
# normally if we open a file we should make sure to close it but 
# with does it for us

# open function will return a file object
# first parameter is file path, second is the mode:
# w is write (will overwrite a file)
# x will also write if this file doesn't exist if file exist we receive error
# a is for append a file (everytime we add the text)
# r is to read

# we can also set these to be keyword arguments like:
# with open(file=file_path, mode='w') as file:

employees = ['Mark', 'Louis', 'Erwin']
file_path2 = '03 - python/lesson31example2.txt'

try:
    with open(file_path2, 'w') as file:
        for employee in employees:
            file.write(employee + '\n')
        print(f"txt file '{file_path2}' was created")
except FileExistsError:
    print('That file already exists!')

# write() argument must be str, not list - error we receive
# to write each item within a list we need to iterate over it
# using some sort of loop, we can't write a list or any
# other collection directly


# 53. Write to .json file

import json

employee = {
    'name': 'John',
    'age': 30,
    'job': 'chef'
}

file_path3 = '03 - python/lesson31example3.json'

try:
    with open(file_path3, 'w') as file:
        json.dump(employee, file, indent=4)
        print(f"json file '{file_path3}' was created")
except FileExistsError:
    print('That file already exists!')

# we need to import json module
# dump method convert our dictionary to a json string to output it
# indent keyword argument means for each key value pair how many
# spaces we want to indent each (spaces left side)


# 54. Write to .csv file

import json
import csv

employees = [['Name', 'Age', 'Job'], 
             ['Mark', 25, 'Pilot'], 
             ['Ron', 19, 'Driver'], 
             ['Bob', 31, 'Electrician']]

file_path4 = '03 - python/lesson31example4.csv'

try:
    with open(file_path4, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path4}' was created")
except FileExistsError:
    print('That file already exists!')

# writer is an object, it provides methods to writing data
# to a csv file
# newline keywrod prevents from space in csv file between records