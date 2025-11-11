# READING FILES (.txt, .json, .csv)

# 55. Read from .txt file

file_path = '03 - python/lesson31example1.txt'

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('That file was not found')
except PermissionError:
    print('You do not have permission to read that file')


# 56. Read from .json file

import json

file_path2 = '03 - python/lesson31example3.json'

try:
    with open(file_path2, 'r') as file:
        content = json.load(file)
        print(content)
        print(content['name'])
except FileNotFoundError:
    print('That file was not found')
except PermissionError:
    print('You do not have permission to read that file')

# you can get key value from json


# 57. Read from .csv file

import csv

file_path3 = '03 - python/lesson32example4.csv'

try:
    with open(file_path3, 'r') as file:
        content = csv.reader(file)
        for line in content:
            # print(line)
            print(line[1])
except FileNotFoundError:
    print('That file was not found')
except PermissionError:
    print('You do not have permission to read that file')

# content = csv.reader(file) this gives us memory address
# print(line[0]) to display only one column