class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f'Name: {self.name}, Age: {self.age}')

# Create an Object of the Person Class
person1 = Person('John', 30)
person2 = Person('Jack', 23)

# Access Object Attributes and Methods
person1.display_info()
person2.display_info()