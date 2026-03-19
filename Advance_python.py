""" Decorator :
It is just a function that modifies another function without chaning its actual code.
For creating a decorator you first have to create a decorator function and then inside that we will create a wrapper.
"""

#Example: By the use of @property we only used obj.show to get answer insist of obj.show()

class Animal:
    @property
    def show(self):
        print("hello how are you")

obj = Animal()
# obj.show()
obj.show

#----------------------Decorator example:

def decorator(func):
    def wrapper():
        print("I will print myself before the function hello")
        func()
        print("i will print after the function")
    return wrapper

@decorator
def hello():
    print("hello i am akarsh vyas")

hello()

#------
def decorator(func):
    def wrapper(a,b):
        print("The addition to your number are:")
        func(a,b)
        print("thankyou i hope you like it")
    return wrapper

@decorator
def addition(a,b):
    print(f"your total is {a + b}")

addition(12,13)


""" ARGS AND KWARGS : 
For making the decorator with Argument it is tough for this we will movetoward our next avandece stuff .
This is used in function definitions to accept a flexible number of argument.
So *args ae used for multiple positional arguments, and **kwargs are uesd for multiple key word arguments.
And the *args become a tuple and **kwargs becomes a dictionary.

"""
#Example: 

def addition(*args):
    print(args)
    sum=0
    for i in args:
        sum = sum +i

    print(sum)

addition(12,13,11,45,34,78,98,98)

#-----------------

def addition(**kwargs):
    print(kwargs)


addition(a=12, b=56,c=45)   

#------------

def information(**kwargs):
    print("your information is \n\n ")

    for i in kwargs:
        print(f"{i}: {kwargs[i]}")

information(name = "Amit tiwari", age = 21 , designation="Software Engineer")
information(name = "Ashish", age = 19 , designation="AI/ML")
information(name = "Ayush Kumar", age = 22 , designation="Software Engineer")
information(name = "Ritesh sharma", age = 21 , designation="web dev")
information(name = "Mohit", age = 25 , designation="hum sab ka kaam krne wala")


#---------------both 

def decorator(func):
    def wrapper(*args,**kwargs):
        print("The addition to your number are:")
        func(*args,**kwargs)
        print("thankyou i hope you like it")
    return wrapper

@decorator
def addition(a,b,c,e,r,w,f,s,g):
    print(f"your total is {a + b + c + e + r + w + f + s + g}")

addition(12,13,32,43,21,54,65,76,76)

#-----
def decorator(func):
    def wrapper(*args, **kwargs):
        print("The addition to your numbers are:")
        result = func(*args, **kwargs)
        print("thank you, I hope you like it")
        return result
    return wrapper


@decorator
def addition(*numbers):
    return sum(numbers)


print("Total:", addition(12, 13, 32, 43, 21, 54, 65, 76, 76))

""" LIST, DICTIONARY and SET Comphrehension:
All of these are used to create list , distionary and set. But you donot have to use multiple lines of code for loop and if-else statement

"""
#list
""" even number print"""
l=[i for i in range(1,21) if i%2==0]
print(l)

#dict

d={i : i**2 for i in range(1,10)}
print(d)


"""  Lambda Function:
inline functiondefined using the lambda keyword.
used for short, simple function that are sued only once or temporarily.
you have multiple argument but there will be only one expression.
 """
addition = lambda a,b : a+b 
print(addition(12,13))


evenAndodd= lambda a: "even" if a%2 ==0 else "odd"
print(evenAndodd(12))


""" Map , Filter  and Zip """

#example : double list element
a=[1,2,3,4,5]
result= map(lambda x : x*2,a)
print(list(result))
