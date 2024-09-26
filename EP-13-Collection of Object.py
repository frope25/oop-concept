"""
we can store object as collection in
list, dictionaries and tuples
"""

class Customer:
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender

    def display(self):
        print(f"{self.__name}'s age is {self.__age}, and gender is {self.__gender}")


c1 = Customer("Shaw", 23, 'male')
c2 = Customer("Lea", 26, 'female')
c3 = Customer("Joshua", 19, 'male')

# L1 = [c1, c2, c3] 
L1 = (c1, c2, c3)


for i in L1:
#     print(i._Customer__name, i._Customer__age, i._Customer__gender)
    print(i.display())
