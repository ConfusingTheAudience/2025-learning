# MODULE = a file containing code you want to include in your program
#          use 'import' to include a module (build-in or your own)
#          useful to break up a large program reusable separate files

# 32. Modules

print(help('modules')) # to check all available modules

# first example on how to use modules

import math

math.pi

# second example

import math as m

m.pi

# third example (be aware of name problems)

from math import pi

pi

# to import your module and use it

import lesson16module

result = lesson16module.pi
result = lesson16module.square(3)
result = lesson16module.cube(3)
print(result)

