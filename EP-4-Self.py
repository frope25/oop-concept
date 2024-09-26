"""
A function created inside class
is called method
"""

class Person:
    # constructor
    def __init__(self):
        print('Constructor called !')

    def display_info(self):
        print('In Display info function')

# Create an object ofo the Person Class
person1 = Person()
person2 = Person()

"""
In python when we call a method,
The method gets default argument as method
"""

# Access object attributes and methods 
person1.display_info()
person2.display_info()