# MULTIPLE INHERITANCE 

"""
Multiple Inheritance in Python is a feature that allows
a class to inherit from multiple base classes.
"""
###################### Multiple Inheritance ######################

"""

            parent1         parent2
               |               |
               |               |
               ------child------

""" 

# class Parent1:
#     def __register(self):
#         print('register in user class')

#     def login(self):
#         print('login in user class')

# class Parent2:
#     def enroll(self):
#         print('Enroll in student class')

#     def checkout(self):
#         print('Checkout in student class')

# class child(Parent1, Parent2):
#     def create_course(self):
#         print('create course in Instructor class')

#     def earning(self):
#         print('Earnings in Instructor class')

# ch = child()
# ch.create_course()
# ch.enroll()
# ch._Parent1__register()


"""
MRO :- Method resolution Order
"""

class Product1():
    def buy(self):
        print('In Product 1')

class Product2():
    def buy(self):
        print('In Product 2')

class client(Product1, Product2):
    pass

c = client()
c.buy()