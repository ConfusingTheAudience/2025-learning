# if __name__ == __main__   = (this script can be imported OR run standalone)
#                             functions and classes in this module can be
#                             reused without the main block of code executing

# 37. __name__ == __main__

def main():
    # Your program goes here

if __name__ == '__main__':
    main()

# __main__ is the name of the environment where top-level code is run

# EXAMPLE what is __main__ in two scenarios

# -------- script1.py file
# from script2 import *
# print(__name__)

# -------- script2.py file
# print(__name__)

# run script1 directly => __name__ is __main__
# run script2 directly => __name__ is script2

# **********************************************

# -------- script1.py file
# print(__name__)

# -------- script2.py file
# from script1 import *
# print(__name__)

# run script1 directly => __name__ is script1
# run script2 directly => __name__ is __main__

# **********************************************

# In Short: It Allows You to Execute Code When the File Runs as a Script, but Not When It’s Imported as a Module

# It’s useful for adding script-specific logic, such as user input or test cases, without affecting module imports



# EXAMPLE

# -------- name.py file

# me = "Mark"

# if __name__ == "__main__":
#     me = "I'm not real Mark"
#     print(me)

# -------- myname.py file
# import name

# print(name.me)

# --------

# execute name.py directly returns I'm not real Mark
# execute myname.py directly returns Mark


