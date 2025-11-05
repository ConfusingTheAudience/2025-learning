# OBJECT ORIENTED PROGRAMMING

# object = A "bundle" of related attributes (variables)
#          and methods (functions) Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

# 38. Class

# this could be in another file like car.py
class Car:
    def __init__(self, model, year, color, for_sale): # constructor
                                                      # self tells right now
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f'You drive the {self.model}') # referring to the object
                                             # we currently working with
    def stop(self):
        print(f'You stop the {self.model}')

    def describe(self):
        print(f'{self.year} {self.color} {self.model}')
# and then remember to make import like
# import car import Car

car1 = Car('Mustang', 2024, 'red', False)
car2 = Car('Corvette', 2025, 'blue', True)

print(car1) # returns memory address of this car object

print(car1.model) # returns Mustang
print(car1.year) # returns 2024
print(car1.color) # returns red
print(car1.for_sale) # returns False

car1.drive() # I don't need to print this because it's method
car2.stop()
car2.describe()
