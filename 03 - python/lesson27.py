# @property = Decorator used to define a method as a property (it can be accesssed like an attribute)
#             Benefit: Add additional logic when read, write or delete attributes
#             Gives you getter, setter and deleter method

# 48. @property - GETTER, SETTER, DELETER

class Rectangle:
    def __init__(self, width, height):
        self._width = width # _ mean these attributes need to be protected
        self._height = height # _ mean private attribute

    # GETTER
    @property
    def width(self):
        return f'{self._width:.1f}cm'

    @property
    def height(self):
        return f'{self._height:.1f}cm'
    
    # SETTER
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print('Width must be greater than zero')

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print('Height must be greater than zero')

    # DELETE
    @width.deleter
    def width(self):
        del self._width
        print('Width has been deleted')

    @height.deleter
    def height(self):
        del self._height
        print('Height has been deleted')
    
rectangle = Rectangle(3, 4)

# GET
print(rectangle.width) # because of _ this print returns None
print(rectangle._height) # however this is working
                         # but we shouldn't get it like that when we
                         # have private attributes in class
print(rectangle.height)  # after @property use this is correct way

# SET
rectangle.height = 3
print(rectangle.height)

# DELETE
del rectangle.width
del rectangle.height