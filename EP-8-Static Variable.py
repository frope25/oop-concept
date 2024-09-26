# STATIC VARIABLE (Class Variable)

"""
Task 
In ATM machine code we should assign 
serial number to every customer/object

u1-1
u2-2
u3-3

Static variables comes in picture
when every object require a shared value

ex1-
IFSC code of bank branch will same for all customers
pin, balance will be different for each customer(stored in instance variable)

ex2 - degree name will same for every student in particular college
(CGPA will be different for each student(stored in instance variable) )

"""

class ATM:
    serial_num = 1
    def __init__(self):
        print('In constructor')
        # creating empty instances
        self.pin = ''
        self.balance = 0
        self.name = ''

        # declaring static variable
        self.serial_num = ATM.serial_num
        ATM.serial_num += 1

    def add_details(self, user_name, user_pin, user_balance):
        self.pin = user_pin
        self.name = user_name
        self.balance = user_balance

    def display_details(self):
        print(f"{self.serial_num}. {self.name}'s pin is {self.pin}, and the balance is {self.balance}.")


# Creating Multiple Users
user1 = ATM()
user2 = ATM()

# Assigning details 
user1.add_details('Jack', '1234', 4500)
user2.add_details('Shaw', '3456', 2500)

# Fetching details
user1.display_details()
user2.display_details()