"""
Getters and Setters are standart/profesional
way to update private variables
"""

class ATM:
    def __init__(self):
        self.__pin = ''
        self.__balance = 0
        self.name = ''

    def get_pin(self):
        print(f"{self.name}'s PIN is {self.__pin}")

    def set_pin(self, new_pin):
        # self.__pin = new_pin
        # print(f'PIN updated to {self.__pin} !')

        if type(new_pin) == str:
            self.__pin = new_pin
            print(f'PIN updated to {self.__pin} !')
        else:
            print('Permission denied')

    def add_details(self, user_name, user_pin, user_balance):
        self.name = user_name
        self.__pin = user_pin
        self.__balance = user_balance

    def display_details(self):
        print(f"{self.name}'s PIN is {self.__pin}, and the  balance is {self.__balance}.")


# Creating multiple users
user1 = ATM()
user2 = ATM()

# Assigning details
user1.add_details('Jack', '1234', 4500)
user2.add_details('Shaw', '4321', 7500)

# Fetching the details
user1.display_details()
user2.display_details()

user1.get_pin()
user1.set_pin(6789)

user1.display_details()