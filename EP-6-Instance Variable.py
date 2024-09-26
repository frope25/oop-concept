"""
Instance Variable is a Variable
for which the value of each object
is different
"""

class ATM:
    def __init__(self):
        print('In Constructor')
        # creating empty instances
        self.pin = ''
        self.balance = 0
        self.name = ''

    def add_details(self, user_name, user_pin, user_balance):
        self.pin = user_pin
        self.name = user_name
        self.balance = user_balance

    def display_details(self):
        print(f"{self.name}'s PIN is {self.pin}, and the balance is {self.balance}.")

# Creating Multiple users
user1 = ATM()
user2 = ATM()

# Assigning the Details
user1.add_details('Josh', 1234, 4500)
user2.add_details('Christ', 4321, 7000)

# Fetching Details
user1.display_details()
user2.display_details()