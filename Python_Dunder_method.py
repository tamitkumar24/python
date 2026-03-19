""" Dunder methods:
are special methods in python that start and end with double underscores, like __init__,__str__etc.
Automatically get called when you perform certain action on an object.
 """

class Animal:
    def __init__(self, name):
       self.name=name

    def __str__(self):
        return f"hello how are you \nyour name is {self.name}"
    
obj = Animal("Lion")

print(obj)

#-----------------------------------------

class Animal:
    def __init__(self, name,age):
       self.name=name
       self.age=age

    def __str__(self):
        return f"hello how are you \nyour name is {self.name}"
    def __add__(self, other):
        return f"your sum of age are {self.age + other.age}"
    
obj = Animal("Lion",12)
obj2 = Animal("dolphin",14)

print(obj + obj2)


#----------------------------------------------

class Animal:
    def __init__(self, name,age):
       self.name=name
       self.age=age

    def __str__(self):
        return f"hello how are you \nyour name is {self.name}"
    def __add__(self, other):
        sum=0
        for i in other:
            sum=sum+i.age

        return f"your sum of age are {self.age + sum}"
    
obj = Animal("Lion",12)
obj2 = Animal("dolphin",14)
obj3 = Animal("tiger",34)

print(obj + {obj2,obj3})

#--------------------------------

class Lifecycle:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is initialized.")

    def __del__(self):
        print(f"{self.name} is being destroyed.")

# Example usage:
obj = Lifecycle("Robot") 
# Output: Robot is initialized.
del obj 
# Output: Robot is being destroyed.

#-----------------------------String Representation

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

my_book = Book("1984", "George Orwell")
print(str(my_book))   # Output: '1984' by George Orwell
print(repr(my_book))  # Output: Book('1984', 'George Orwell')

#--------------------------------Mathematical Operations

"""
__add__(self, other): For +

__sub__(self, other): For -

__mul__(self, other): For *

__truediv__(self, other): For /

"""
class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        # Allows us to add two Wallet objects together
        return Wallet(self.amount + other.amount)
        
    def __str__(self):
        return f"{self.amount}"

wallet1 = Wallet(50)
wallet2 = Wallet(25)
total_wallet = wallet1 + wallet2
print(total_wallet)  # Output: 75


#-------------------Comparison Operators

"""
__eq__(self, other): For == (Equal)

__ne__(self, other): For != (Not equal)

__lt__(self, other): For < (Less than)

__gt__(self, other): For > (Greater than)

"""
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __eq__(self, other):
        return self.celsius == other.celsius

    def __gt__(self, other):
        return self.celsius > other.celsius

temp1 = Temperature(20)
temp2 = Temperature(30)
print(temp1 == temp2)  # Output: False
print(temp2 > temp1)   # Output: True

#-----------------Containers and Sequences

"""
If you want your object to act like a list or dictionary, these are the methods you need.

__len__(self): Triggered by len(obj).

__getitem__(self, key): Triggered by obj[key].

__setitem__(self, key, value): Triggered by obj[key] = value.

__contains__(self, item): Triggered by the in keyword.

"""
class CustomCabinet:
    def __init__(self):
        self.items = ["plates", "cups", "bowls"]

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

cabinet = CustomCabinet()
print(len(cabinet))        # Output: 3
print(cabinet[1])          # Output: cups

#-------------------------Making Objects Callable

"""
__call__(self, *args, **kwargs): Allows an instance of a class to be called as if it were a function.

"""
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

times_three = Multiplier(3)
print(times_three(10))  # Output: 30

#------------Context Managers (with statement)
"""
These are used for setup and teardown actions, like opening and closing files or database connections safely.

__enter__(self): Setup code (e.g., opening a file).

__exit__(self, exc_type, exc_val, traceback): Teardown code (e.g., closing a file). It catches exceptions too.

"""
class SecretConnection:
    def __enter__(self):
        print("Opening secure connection...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing secure connection securely.")

with SecretConnection() as conn:
    print("Transmitting data...")
    
# Output:
# Opening secure connection...
# Transmitting data...
# Closing secure connection securely.








