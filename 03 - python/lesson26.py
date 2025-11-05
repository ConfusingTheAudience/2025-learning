# MAGIC METHODS = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of Python's built-in operations
#                 They allow developers to define or customize the behavior of objects

# 47. Magic method

class Student:

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __str__(self):
        return f'name: {self.name} gpa: {self.gpa}'
    
    def __eq__(self, other):
        return self.name == other.name
    
    def __lt__(self, other):
        return self.gpa > other.gpa
    
    def __gt__(self, other):
        return self.gpa > other.gpa
    
    def __add__(self, other):
        return self.gpa + other.gpa
    
    def __contains__(self, keyword):
        return keyword in self.name
    
    def __getitem__(self, key):
        if key == 'name':
            return self.name
        elif key == 'gpa':
            return self.gpa
        else:
            return f'Key {key} was not found'


student1 = Student('John', 3.2)
student2 = Student('Jimmy', 2.0)
# __init__ is like constructor and let's us assign values
print(student1)
# __str__  is controlling the output from print(student1)
#          normally we would get memory address
print(student1 == student2)
# __eq__   checks if both objects are equal
#          we could check if both students have same name and gpa so
#          they are equal and it will return True otherwise False
print(student1 < student2)
print(student1 > student2)
print(student1 + student2)
# __lt__   checks if for example gpa of one object is less than other
# __gt__   checks if for example gpa of one object is greater than other
# __add__  add two values togheter
print('Jo' in student1)
print(student2['name'])
# __contains__ checks if keyword exist in object
# __getitem__  returns existing value, if it doesn't exist returns None
