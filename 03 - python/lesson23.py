# Polymorphism = Greek word that means to "have many forms or faces"
#                Poly = Many
#                Morphe = Form

#                TWO WAYS TO ACHIEVE POLYMORPHISM
#                1. Inheritance = An object could be treated of the same type
#                   as a parent class
#                2. "Duck typing" = Object must have necessary attributes/methods

# 43. Inheritance polymorphism

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5
    
class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

#shapes = [Circle(), Square(), Triangle()] # all of theese have 2 forms
                                           # first Circle is Circle
                                           # second Circle is also Shape
                                           # etc.

shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza('pepperoni', 15)]

for shape in shapes:
    print(f'{shape.area()}cm²')

# Pizza inherit from Circle made it 3 forms
# Pizza, Circle and Shape


# 44. Duck typing 

# "If it looks like a duck and quacks like a duck, it must be a duck"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print('Woof')

class Cat(Animal):
    def speak(self):
        print('Meow')

class Car:

    alive = False

    def speak(self):
        print('Honk')

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)

# if we do name method same name as Animals have like speak it will work
# also if we want to print alive attribute from Animal and we haven't it
# in Car class then we can write it to make it work
# that's the minimum necessary requirments to be considered as an Animal

