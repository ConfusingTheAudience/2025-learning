# INHERITANCE = Allows a class to inherit attributes and methods
#               from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

#               also known as class Sub(Super)

# 40. Inheritance

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')

class Dog(Animal):
    def speak(self):
        print('Woof')

class Cat(Animal):
    def speak(self):
        print('Meow')

class Mouse(Animal):
    def speak(self):
        print('Squeek')

dog = Dog('Scooby')
cat = Cat('Garfield')
mouse = Mouse('Jerry')

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

mouse.speak()


# 41. Multiple and multilevel inheritance

# multiple inheritance   = inherit from more than one parent class
#                          C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')

class Prey(Animal):
    def flee(self):
        print(f'{self.name} is fleeing')

class Predator(Animal):
    def hunt(self):
        print(f'{self.name} is hunting')

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator): # multiple inheritance
    pass

# order:
# Animal is parent of Prey and Predator
# Prey is parent of Rabbit and Fish
# Predator is parent of Hawk and Fish

# so Rabbit Fish and Hawk are able to sleep and eat now since they inherit it
# from Prey and Predator which inherit it from Animal

rabbit = Rabbit('Bugs')
hawk = Hawk('Tony')
fish = Fish('Nemo')

fish.flee()
fish.hunt()

rabbit.eat()
hawk.sleep()