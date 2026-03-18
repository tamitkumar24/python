"""conditional statement"""
"""
a=1
if a>10:
    print("i will do task 1") #identation means 5 space after if ,for and etc; 
else:
    print("i will do task 2")
"""

# money=int(input("please provide me the money: "))

# if money==10:
#     print("i will have a choco bar icecream")
# elif money==20:
#     print("i will have a mongo dolly")
# else:
#    print("i will have a cone")


# year=int(input("tell you year:- "))

# if year%100==0 and year%400==0:
#     print("its a leap year")
# elif year%100 !=0 and year%4==0:
#     print("its a leap year")
# else:
#     print("its a normal year")

""" LOOP """
#for loop work when you know the number of iteration 
# while loop work on condition that determine when to stop

"""range"""
# a=range(1,20,2) #start with 1 and go upto 20 and jump 2 step
# for i in a:
#     print(i*2)

# for i in range(16,1,-1):
#     print(i*2)
# print("okk1")
# for i in range(-16,1,1):
#     print(i*2)
# print("okk2")

# n=int(input("which table you want to print : "))
# for i in range(1,11,1):#range(n,(n*10)+1,n)
#     print(i*n)#print(i)
# print("okk3")

""" loops for strings"""
#you can iterate through a string in twwo ways:using index values and iterating directly over the string

# a="Amit are going to do something crazy"
#method1
# for i in range(len(a)):
#     print(a[i])
#method2
# for i in a:
#     print(i)

"""break and continue"""
# for i in range(1,21):
#     # if i==15:
#     #     break
#     if i==20:
#       continue
#     else:
#         print(i)

""" for with else"""
# for i in range(1,21):
#     if i==56:
#         print("break is executed")
#         break
#     print(i)

# else:
#     print("break statement is not executed")

"""factorial of number """
# n=int(input("enter the number :- "))
# fact=1

# for i in range(1,n+1):
#     fact*=i

# print(f" factorial of number {fact}")

# n=int(input("tell your number:- "))
# even=0
# odd=0
# for i in range(1,n+1):
#     if i%2==0:
#         even+=i
#     else:
#         odd+=i

# print(f" even sum {even} and odd sum {odd}")

# n=int(input("check your perfect number as you want"))
# sum=0

# for i in range(1,n):
#     if n%i==0:
#         sum+=i

# if sum==n:
#     print("perfect number")
# else:
#     print("not a perfect number")

# n=int(input("enter the number to check for prime number :- "))

# count=0

# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print("prime number")
# else:
#     print("not prime number")

"""to reverse the string """

# s="amit kumar"
# # print(s[::-1]) #but we need logic to solve the question
# p=""
# for i in range(len(s)-1,-1,-1):
#     # print(s[i])
#    p+=s[i]

# print(p)

# """is this palindron or not"""

# s=str(input("neter string to check palindrome:- "))
# p=""
# for i in range(len(s)-1,-1,-1):
#    p+=s[i]

# if s==p:
#    print("palindrome")
# else:
#    print("not palindrome")

# a=str(input("enter mixture of alpha,character and number for counting:- "))

# char=0
# dig=0
# spchar=0

# for i in a:
#     if i.isdigit():
#         dig+=1
#     elif i.isalpha():
#         char+=1
#     else:
#         spchar+=1

# print(f"digit are: {dig} , alpha are: {char} and spchar are: {spchar}")

"""While loop"""

# a=0

# while a<=30:
#     print(a)
#     a+=1

# a=int(input("enter the number for reverse"))
# rev=0
# while a>0:
#     # print(a%10)
#     rev=rev*10 + a%10
#     a=a//10

# print(rev)


















