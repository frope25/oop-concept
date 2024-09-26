# SUPER KEYWORD

"""
Using super keyword we can call/invoke 
parent class methods
It doesn't work outside class
"""

# Code 1
# class Phone():
#     def __init__(self, price, brand, version):
#         print('In Constructor')
#         self.price = price
#         self.brand = brand
#         self.version = version

#     def buy(self):
#         print('By Method in Phone Class')

# class SmartPhone(Phone):
#     def buy(self):
#         print('Buy method in SmartPhone Class')
#         super().buy() # Super Keyword Declaration

# apple = SmartPhone(150000, 'Apple', 15)
# apple.buy()


# Code 2
class Phone():
    def __init__(self, price, brand, version):
        print('In Phone Constructor')
        self.price = price
        self.brand = brand
        self.version = version

class SmartPhone(Phone):
    def __init__(self, price, brand, version):
        self.price = price
        print('Inside SmartPhone Conostructor')
        super().__init__(price, brand, version)

apple = SmartPhone(150000, 'Apple', 15)

