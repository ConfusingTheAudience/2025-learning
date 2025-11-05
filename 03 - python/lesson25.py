# CLASS METHODS = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class iself

# 46. Class method

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #INSTANCE METHOD
    def get_info(self):
        return f'{self.name} {self.gpa}'
    
    #CLASS METHOD
    @classmethod
    def get_count(cls):
        return f'Total number of students: {cls.count}'
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f'Average gpa: {cls.total_gpa / cls.count:.2f}'
    
student1 = Student('Amber', 3.2)
student2 = Student('Sque', 2.4)
student3 = Student('Mark', 3.7)

print(Student.get_count()) # that's how to call class method
print(Student.get_average_gpa())

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data
# Class methods = Best for class-level data or require access to the class itself