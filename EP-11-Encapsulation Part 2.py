"""
Nothing in Python  is Truly Private
"""

class ATM:
    def __init__(self):
        print('In constructor')
        # creating empty instances
        self.pin = ''
        self.balance = 0
        self.name = ''

    def add_details(self, user_name, user_pin, user_balance):
        self.__pin = user_pin
        self.name = user_name
        self.__balance = user_balance

    def display_details(self):
        print(f"{self.name}'s pin is {self.__pin}, and the balance is {self.__balance}.")


# creating multiple users
user1 = ATM()
user2 = ATM()

# Assigning details
user1.add_details('Jack', '1234', 4500)
user2.add_details('Shaw', '4321', 7500)

# Fetching the details
user1.display_details()
user2.display_details()

# trap 1
print('\nIn Trap 1')
user1.name = 'John' # how to get access for public variable
user1.display_details()

"""
How private variable get store

__variableName = _className__variableName
__pin = _ATM__pin
"""

# trap 2
print('\nIn Trap 2')
user2._ATM__pin = '9876' # how to get access for private variable
user2.display_details()


"""
Reason of being not Private
"""