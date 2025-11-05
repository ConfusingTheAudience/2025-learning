# STATIC METHODS = A method that belong to a class rather than any
#                  object from that class (instance)
#                  Usually used for general functions

# Instance methods = Best for operation on instances of the class (objects)
# Static methods   = Best for utility functions that do not need access to class data


#INSTANCE METHOD
# def get_info(self):
#     return f'{self.name} = {self.position}'

# STATIC METHOD
# @staticmethod
# def km_to_miles(kilometers):
#     return kilometers * 0.621371


# 45. Static method

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f'{self.name} = {self.position}'
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ['Manager', 'Cashier', 'Cook', 'Janitor']
        return position in valid_positions

employee1 = Employee('Eugene', 'Manager')
employee2 = Employee('Sque', 'Cashier')
employee3 = Employee('Amber', 'Cook')
    
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
# for instance methods we need to access the object like employee1
# then call the instance method
print(Employee.is_valid_position('Cook'))
# for static method you only need to access that class
# you don't need to create any object for that class like employee1
# it's general utility method