# INTRODUCTION TO POLYMORPHISM

"""
POLYMORPHISM :- Geeks word (Having multiple form)

Man - Father, Employee, Husband, Brother
Women - Mother, Employee, Wife, Sister

Types of Polymorphism

Method Overriding:- Method Overriding involves creating a method in the child class
that has the same name, parameters, and return type as a method in the parent class.
class A:
    area(p1):
class B:
    area(p1)

Method Overloading:- Method Overloading refers to defining multiple methods with 
the same name but different parameters within the same class.
area(p1, p2)
area(p1)
area(p1, p2, p3)

Operator Overloading:- Operator Overloading is a feature that allows you to 
define custom behavior for built in operators.

"""

# class Phone():
#     def __init__(self, price, brand, version):
#         print('In Constructor')
#         self.price = price
#         self.brand = brand
#         self.version = version

#     def buy(self):
#         print('Buy method in Phone Class')

# class SmartPhone(Phone):
#     def buy(self):
#         print('Buy Method in SmartPhone Class')

# apple = SmartPhone(150000, 'Apple', 15)
# print(apple.brand, apple.price, apple.version)

# apple.buy()

# Some Traps

class Parent():
    def __init__(self, age):
        print('In Constructor')
        self.__age = age

    def get_age(self):
        return self.__age

class Child(Parent):
    def __init__(self, name, age):
        self.name = name
        # super().__init__(age)

    def get_name(self):
        return self.__name
    
ch = Child('Raffa', 20)
print(ch.get_age()) # Error Chile object has no attribute '_Parent__age()'