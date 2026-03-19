"""OOPS in Python"""
#class
# class Factory:
#     a=12#attribute

#     def what(self): #method  #to target the object location we use self keyword
#         print("how are you")

#     print("hello ho are you i am gettinng intialized ")

# print(Factory().a) #calling attribute by the help of class
# Factory().what()


# #object
# obj= Factory()
# print(obj.a)
# obj.what()

#constructor: A cintructor is a method that runs automatically when we call a class and this constructor funtion will target the object location
# class Factory:
#     def __init__(self,material,zips,pockets): #__init__ is called automatically,It is used to initialize object data,self refers to the current object,It is not a normal function, it’s a special method (dunder method)
#         # print(self)
#         self.material= material
#         self.zips=zips
#         self.pockets= pockets

#     def show(self):
#         print(f"your object detaila are {self.material} materials, {self.pockets} pockets, {self.zips} zips")


# nikes= Factory("leather",3,2)

# reebok = Factory("nylon",3,3)
# reebok.show()

"""types of Attribute and types of method """

#class attribute- a normal variable create inside a class is a class attribute.
class Car:
    name= "lion"
    
    def __init__(self,age):
        #instance attributes- created using an instance like self.name, self.age etc.it is known as instance attribute
        self.age= age
        
#instance method- method works with instance {onject} of the class. This method can access and modify instance attribute
    def show(self):
        print(f"that instance method and age of object is {self.age} ")

#class method- this method works with the class itself it will not target the instance(object).we have to use @classmethod decorator for creating the class method and it takes cls as their first parameter and its target the class directly .   
    @classmethod
    def hello(cls):
        print("how are you brother")
#static method- doesn't access class or instance directly it also uses a decorator @staticmethod it just acts like a regular function placed unside a class. 
    @staticmethod
    def static():
        print("how are you ")











