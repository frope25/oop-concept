# MULTILEVEL INHERITANCE

"""
Multilevel Inheritance in Python is a type of Inheritance that involves
inhering a class that has already inherited some other class

        Product             -> Product is not always Phone and not always SmartPhone 
           |
         Phone              -> Phone is always Product, Phone is not always SmartPhone
           |
      Smart Phone           -> SmartPhone is always Phone 

"""

# class Product():
#     def product_method(self):
#         print('In Product Method')

# class Phone(Product):
#     def phone_method(self):
#         print('In Phone Method')

# class SmartPhone(Phone):
#     def smart_phone(self):
#         print('In SmartPhone Method')

# s1 = SmartPhone()
# s1.smart_phone()
# s1.phone_method()
# s1.product_method()

# s2 = Phone()
# s2.phone_method()
# s2.product_method()


class A():
    def a(self):
        print("a")
class B(A):
    def b(self):
        print("b")
class C(B):
    def c(self):
        print("c")
class D(C):
    def d(self):
        print("d")
class E(D):
    def e(self):
        print("e")
class F(E):
    def f(self):
        print("f")
class G(F):
    def g(self):
        print("g")
class H(G):
    def h(self):
        print("h")
class I(H):
    def i(self):
        print("i")
class J(I):
    def j(self):
        print("j")
class K(J):
    def k(self):
        print("k")


obj = K()
obj.a()
obj.b()
obj.c()
obj.d()
obj.e()
obj.f()
obj.g()
obj.h()
obj.i()
obj.j()
obj.k()