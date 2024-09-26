# SINGLE INHERITANCE

class User:
    def register(self):
        print('register in user class')

    def login(self):
        print('login in user class')

class Student(User):
    def enroll(self):
        print('enroll in student class')

    def checkout(self):
        print('checkout in student class')

# creating Student class object
print('\n Student Class Object \n')
stud = Student()
stud.checkout()
stud.enroll()
stud.login()
stud.register()

# # Creating User Class Object
# print('\n User Class Object \n')
# user1 = User()
# user1.login()
# user1.register()