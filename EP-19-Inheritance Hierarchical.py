# HIERARCHICAL INHERITANCE

"""
Hierarchical Inheritance is a type of Inheritance in which
a single base class is Inherited by multiple derived classes.

            --------A--------
            |       |       |
            |       |       |
            B       C       D

"""

class User:
    def register(self):
        print('Register in user Class')

    def login(self):
        print('Login in User Class')

class Student(User):
    def enroll(self):
        print('Enroll in Student Class')

    def checkout(self):
        print('Checkoutt in Student Class')

class Instructor(User):
    def create_course(self):
        print('Create Course in Instructor Class')
    
    def earnings(self):
        print('Earnings in Instructor Class')


stud = Student()
stud.checkout()
stud.login()

inst = Instructor()
inst.create_course()
inst.login()