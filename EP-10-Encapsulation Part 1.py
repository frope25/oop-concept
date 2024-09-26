"""
Encapsulation means simply hiding
irrelevant details from user/other developer 
"""

class ATM:
    def __init__(self):
        print('In Constructor')
        # creating empty instances
        self.pin = ''  # public access variable 
        self.__balance = 0 # private access variable "start with double underscore (__)"
        self.__name = ''

    def add_details(self, user_name, user_pin, user_balance):
        self.pin = user_pin
        self.__name = user_name
        self.__balance = user_balance

    def display_details(self):
        print(f"{self.__name}'s pin is {self.pin}, and the balance is {self.__balance}.")

    
# creating multiple users
user1 = ATM()
user2 = ATM()

# Assigning details
user1.add_details('Jack', '1234', 5500)
user2.add_details('Shaw', '4321', 7500)

# Fetching details 
user1.display_details()
user2.display_details()

# trap
print("\nIn Trap 1")
user1.pin = '2345'
user1.display_details()