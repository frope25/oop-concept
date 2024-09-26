"""
Class : It's a blueprint
object : Instance of class

A single class can have many objects
"""
# a = 2 
# b = 3
# c = 1
# print(type(a))

items = ['bat', 'ball', 'stumps']
#items.

"""
In simple terms 
datatype is class
and when we create a variable, it becomes object of that class
"""

class Person:
    # consructor
    def __init__(self):
        print('Constructor called !')

    def display_info(self):
        print('In Display info Function')

# create an object of the Person class
person1 = Person()

# access object attributes and methods
person1.display_info()