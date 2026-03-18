"""Function:- 
its a block of reusable code that we create whenever we want to call it then only it executed/run  """

# def greet():
#     print("hello, welcome to python")
 
# greet()

""" The thing you accept is parameters, The thing you provide to parameters is argument"""

# def sum(a,b):
#     print(f"The sum of your number is {a+b}")

# sum(12,34)
# sum(56,98)

# def hello(name,age):
#     print(f"your name is {name} and you age is {age}")

# hello("Amit",21)
# hello(age=21,name="Ashish")

# def sum(a,b=45):
#     print(f"The sum of your number is {a+b}")

# sum(22)
# sum(23,47)#47 replace defalut argument b=45 to 47


"""skip code """
# d1={10:100,20:200,40:300}
# d2={40:400,50:500,60:600}

# for i in d2:
#     if i in d1.keys():
#         d1[i]+=d2[i]
       
#     else:
#         d1[i]=d2[i]

# print(d1)

"""exception handling """

# a=int(input("tell your number:- "))
# try:
#     print(10/a)

# except ZeroDivisionError:
#     print("Sorry you cannot divide by 0")

# print("ok i have one the division")
      


# a = int(input("tell your number:- "))
# try:#wrap the block of code that might cause an exception
#     print(10/a)
# except Exception as err:#handle the exception if it occurs
#     print(f"sorry there is an error as {err}")
# else:#run cdoe only if no exception occurs
#     print("good there is no exception")

# finally:#run code no matter what,whether there's an exception or not
#     print("i will run no matter what")

# print("ok i have done the division")

#raise:- manually throw an exception

# age=int(input("tell your age:- "))
# try:
#     if age<10 or age >18:
#         raise ValueError("your age must be between 10 and 18")
#     else:
#         print("welcome to the club")
# except Exception as err:
#     print(f"an error occured as {err}")


# print("The lab will start soon")

"""File Handling"""
# q=open(r'C:\Users\tamit\Downloads\bhu practical.txt')
# print(q.read())

# p=open('pythontutorial2.py')
# print(p.read())

""" So in file handling we usually deal with CRUD and there are multiple modes to open the files are : r-read(default)-file must exist, w-write-create file or overwrites, a - append -add to end of file, x- create-create a new file.fail if iit exits"""
#write inside file
# r=open("superman.txt",'w')

# r.write("hello this akarsh and i am writting inside this file")
# # r.close()
# #append i.e i gona add inside it some more content
# r=open("superman.txt",'a')

# r.write("\n hello bro i just need to follow the part of y life , can you please help me to follow")
# r.close()

































