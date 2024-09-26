"""
If we can give nteger, string, float etc
argument to function, then we can also give
object as argument to function
"""

## part 1

# class Customer:
#     # method
#     def __init__(self, name):
#         self.name = name 

# # function
# # passing object as argument in function greet
# def greet(customer_name):
#     print(f'hello {customer_name.name}')


# cust1 = Customer('Raffa')
# greet(cust1)


## part 2
class Customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender.lower()

# function
def greet(customer_name):
    if customer_name.gender == 'male':
        print(f'Hello Mr.{customer_name.name} !')
    elif customer_name.gender == 'female':
        print(f'Hello Mrs.{customer_name.name} !')

cust1 = Customer('Raffa', 'male')
cust2 = Customer('Eve', 'Female')

greet(cust1)
greet(cust2)