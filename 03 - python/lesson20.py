# CLASS VARIABLES = Shared among all instances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from
#                   that class

# 39. Class variavbles

class Student:

    class_year = 2024 # those are class variables
    num_students = 0  # those are class variables

    def __init__(self, name, age):
        self.name = name # those are instance variables
        self.age = age   # those are instance variables
        Student.num_students += 1 # self means like "student1"
                                  # that's why we use Student for class var...

student1 = Student('Mack', 30)
student2 = Student('Josh', 35)

print(student1.name)
print(student1.age)
print(student2.name)
print(student2.age)

# it does work however
print(student1.class_year)
print(student2.class_year)
# good practice to access class variables is by name of the class
print(Student.class_year)

print(Student.num_students) # returns 2 because we have 2 students

print(f'My graduating class of {Student.class_year} has {Student.num_students} students')