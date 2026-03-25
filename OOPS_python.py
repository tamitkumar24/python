"""OOPS in Python"""
#class
class Factory:
    a=12#attribute

    def what(self): #method  #to target the object location we use self keyword
        print("how are you")

    print("hello ho are you i am gettinng intialized ")

print(Factory().a) #calling attribute by the help of class
Factory().what()

#---------------------------------------------------------------------

#object
obj= Factory()
print(obj.a)
obj.what()

#constructor: A cintructor is a method that runs automatically when we call a class and this constructor funtion will target the object location
class Factory:
    def __init__(self,material,zips,pockets): #__init__ is called automatically,It is used to initialize object data,self refers to the current object,It is not a normal function, it’s a special method (dunder method)
        # print(self)
        self.material= material
        self.zips=zips
        self.pockets= pockets

    def show(self):
        print(f"your object detaila are {self.material} materials, {self.pockets} pockets, {self.zips} zips")


nikes= Factory("leather",3,2)

reebok = Factory("nylon",3,3)
reebok.show()


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
    def hello(cls):#cls target car not object so , we cannot access data from it
        print("how are you brother")
        #print(f"how are you brother what your age {cls.age}") #age not print
#static method- doesn't access class or instance directly it also uses a decorator @staticmethod it just acts like a regular function placed unside a class. 
    @staticmethod
    def static():
        print("how are you ")

obj = Car(12)
#instance method
obj.show()
#class method
obj.hello()
#static method
obj.static()


""" 4 Pillar of OOPs"""
""" inheritance
inheritance allows a class(child class) to inherit properties and behaviors(attributes and methods) from another class (parent class)
"""
class Factorymumbai:
    a="I'm an attribute mentioned inside factory"
    def details(self):
        print("i am gona provided you all information about my branch")

class Factorypune(Factorymumbai):
    pass

obj=Factorymumbai()
print(obj.a)
obj2= Factorypune()

print(obj2.details())
#---------------------------------------------------------------------

class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Hello your name is {self.name}")


class Human(Animal):
     def __init__(self, name,age):
         super().__init__(name)
         self.age=age

     def show(self):
         print(f"hello your name is {self.name}, {self.age}")
    


animal1 = Animal("lion")
animal1.show()

person1 = Human("Adrash",21)
person1.show()


"""Type of inheritance"""

#single inheritance already discuss:

#multiple inheritance now dealing: Notes:- The constructor function will be inheritance of the first class that has been inheritance . This is MRO(Method Resolution Order) folloed by python

class Animal:
    def __init__(self,name):
        pass

class Human:
    def __init__(self,name,age):
        pass
# class Robot(Animal,Human):
class Robot(Human,Animal):
    name3="charli123"

# obj= Robot("amit")
obj= Robot("amit",21)

#example:

class Father:
    def father_skills(self):
        return "coding"

class Mother:
    def mother_skills(self):
        return "cooking"

class Child(Father, Mother):
    def show(self):
        print(f"Skill of father: {self.father_skills()}")
        print(f"Skill of mother: {self.mother_skills()}")
        print("Child has multiple skills")


obj = Child()
obj.show()


class Father:
    def skills(self):
        return ["coding"]

class Mother:
    def skills(self):
        return ["cooking"]

class Child(Father, Mother):
    def show(self):
        skills = Father.skills(self) + Mother.skills(self)
        print("Child skills:", ", ".join(skills))


obj = Child()
obj.show()


#multilevel inheritance :

class Factory:
    def __init__(self, material, zips):
        self.material= material
        self.zips= zips

class BhopalFactory(Factory):
    def __init__(self, material, zips,color):
        super().__init__(material, zips)
        self.color= color

class PuneFactory(BhopalFactory):
    def __init__(self, material, zips, color,pockets):
        super().__init__(material, zips, color)
        self.pockets=pockets
    
    def show(self):
            print(f"material: {self.material} ,zips:- {self.zips}, color:- {self.color},pockets:- {self.pockets}")

obj= PuneFactory("nylon",1,"red",4)
obj.show()


""" Polymorphism :-
The word means " many form" and it allows the same interface or method name to behave differently depending on the object or context
Type of Polymorphism:
1-Methodoverriding:A child class overrides a method of the parent class and Python decide at runtime which method to call, bassed on the object type.
2-MethodOverloading: not exit in python
3-Duck typing: python follow the philosophy:"if it walk like a duck and question like a duck, it must be a duck"
""" 
#methodoverriding:
class Women:
    def show(self):
        print("hello i am Anjali's Parent class ")

class Human(Women):
    def show(self):
        super().show()   # call parent
        print("how are you Anjali ,i am your subclass")

obj=Human()
obj.show()

#DUCK Typing:

class Animal:
    def show(self):
        print("I am showing")

class human:
    def show(self):
        print("hello i am also showing ")

obj= Animal()
obj2= human()

obj.show()
obj2.show()


""" Encapsulation:
putting data(Variable) and code(function) together in one place- inside a class.
also means hidding the internal detail of how thngs work and only showing what is needed.
 """
""" Acess Modifiers
1:-Public:Till now every attrivute and method we creatinng are public
2:-Protected used symbol(_) but it still can be accessed from outside class so you might wounder what the point of using them.
3:-Private: it cannot be accessed from outside the class- only from inside the class where it is defined.We use two underscores(__) before the name to make it private.
"""

class Factory:
    __a= "Pune" #private

    def show(self):
        print(Factory.__a)

obj = Factory()
obj.show()

class Demo:
    def __init__(self):
      self.name = "Public Member"
      self._age =21
      self.__salary = 50000
    
    def show(self):
       print("inside the class:")
       print("public:", self.name)
       print("protected:", self._age)
       print("private", self.__salary)

obj=Demo()
obj.show()

""" Abstraction:
It does not exist in pyhton but we can achieve it using a library.It is used to simplifying complex system by focusing on essential featurenand hidding unnecssary details.
 """

from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Square(abstract):
    def __init__(self,side):
        self.side = side

    def perimeter(self):
        print(" i have created")

    def area(self):
        print("i have created")

class Circle(abstract):
    def __init__(self,radius):
        self.radius= radius

    def perimeter(self):
        print(" i have created")

    def area(self):
        print("i have created")

obj= Circle(7)
obj =Square(3)

   













