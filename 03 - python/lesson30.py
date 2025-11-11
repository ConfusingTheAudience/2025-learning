# BASIC FILE DETECTION

# 51. File detection

# to work with files we import os (operating system) module
import os

file_path = '03 - python/lesson30.txt'


# for file detection we can use:
# Relative file path = folder/lesson30.txt
# Absolute file path = C:/Users/User/Desktop/lesson30.txt
# to solve \ problem we can double it like \\ or use /

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print('That is a file')
    elif os.path.isdir(file_path):
        print('That is a directory')
else:
    print("That location doesn't exist")

# built-in methods to check if our file_path exist
# or our path is a file or directory
