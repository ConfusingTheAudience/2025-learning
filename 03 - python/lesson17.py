# VARIABLE SCOPE = where a variable is visible and accessible
# scope resolution = (LEGB rule) Local -> Enclosed -> Global -> Built-in

# 33. Local

def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

func1() # returns 1
func2() # returns 2
# a is local to func1, b is local to func2
# they don't know about each other


# 34. Enclosed

def func1():
    x = 1

    def func2():
        x = 2
        print(x)
    func2()

func1() # returns 2


# 35. Global

def func1():
    print(x)

def func2():
    print(x)

x = 3

func1() # returns 3
func2() # returns 3


# 36. Built-in

from math import e

def func1():
    print(e)

e = 3

func1() # returns 3
# as in the order global is first instead of built-in

