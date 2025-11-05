# super() = function used in a child class to call methods
#           from a parent class (superclass)
#           Allows you to extend the functionality of the inherited methods

#           class Sub(Super)
#           child class is Sub class
#           parent class is Superclass

# 42. super()

class Shape:
    def __init__(self,color , is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f'It is {self.color} and {'filled' if self.is_filled else 'not filled'}')

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled) # super() = Shape
        self.radius = radius

    def describe(self):
        print(f'It is a circle with an area of {3.14 * self.radius * self.radius}')
        super().describe() # to access also method from parent

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle('green', True, 5)
square = Square('blue', False, 6)
triangle = Triangle('yellow', True, height=6, width=8) # as from prev lessons

print(circle.color)
print(circle.is_filled)
print(circle.radius)
print(square.width)
print(triangle.width)
print(triangle.height)

circle.describe() # returns override method so the one inside Circle class
                  # or if super().describe() is used then show both
square.describe()
triangle.describe()
