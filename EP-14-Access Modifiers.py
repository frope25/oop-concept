"""
accessing public variables 
public :- methodName
protected :- _methodName
private :- __methodName
"""

# class Phone:
#     def __init__(self, price, brand, version):
#         print('In Phone Constructor')
#         self.price = price
#         self.brand = brand
#         self.version = version

# class SmartPhone(Phone):
#     pass

# apple = SmartPhone(150000, 'Apple', 15)
# print(apple.brand, apple.price, apple.version)



# ACCESSING PRIVATE VARIABLES

class Phone:
    def __init__(self, price, brand, version):
        print('In Phone Constructor')
        self.__price = price # -> Private Variable
        self.brand = brand # -> Public Variable
        self._version = version # -> Protected Variable

class SmartPhone(Phone):
    pass

apple = SmartPhone(150000, 'Apple', 15)
print(apple.brand) # to access Public Variable
print(apple._version) # to access Protected Variable
print(apple._Phone__price) # to access Private Variable