""" DAY 1"""

#print("hey , i am amit ")

AmitTiwari="BHU" #pascal case

amitTiwari="Student" #camel case

amit_tiwari="MCA" #snake case

#Variable store data type

a=34
print(type(a))
b=56.5
print(type(b))
c=76/4
print(type(c))
d=34j
print(type(d))

#string in pyhton used to store anything 
st='122344 hrhf !@#$%^&*'
print(type(st))

#boolean give true and false

g=True
h=False
print(type(g))

""" String"""

#string take extra space , every character have an unicode to store it string used extra space
#ord used to convert character to unicode
i="A"
print(ord(i))

j="😊"
print(ord(j))

#chr used to convert unicode to character
k=65
print(chr(k))

""" So in string there are to way of indexing first fron start i.e positve indexing and second fron end i.e neative indexing  """

l = "Amit"
#print(a[4]) #out of bound because index at only 0-2
print(l[3])
print(l[-3])

""" String slicing """
m="sher coder"
print(m[0:3:1]) #form 0 we start go upto lesser 3 and take 1 step at a time

print(m[5::]) #this work similar as above we just not write it fully 
#if we want to print all string then we only write this and print print(m[::]) and also their is no need to give step count it automatically start at 1 step only

""" type conversion function
it is used to convert from one data type to another data type just like int to float and float to string
"""
n=4
n=str(n)
print(type(n))

o="123"
o=float(o)
print(type(o))

"""boolean 
fasle value that convert into false and viseversa true
falsy value are : 0,0.0," ", [ ],( ),{ }
truety value are: expect this all
"""
p=0
print(bool(p))
q=123
print(bool(q))

"""Type conversion type
implicit: in this python automatically convert data from one data type to another
explicit: in tis type as a user use in build function to convert one data type to another
example are int , float, complex, str, list,tuple,set,dict,bool are of explicit 
"""
"""input"""
# college=input("which college do you study: ")
# print(college)
#make it more uniform that help us to read its data type we used as like this also
# college=str(input("which college do you study: "))
# print(college)
"""output"""
name="Amit"
age="21"

print(name,age)
print("hello my name is",name,"and my ae is",age)
#insist of using above one we used formatted string 
print(f"my name is {name} and my age is {age}")



""" DAY 2"""

#operators
""" Arithmatic Operators"""
z=16
y=8
print(z+y)
print(z-y)
print(z*y)
print(z/y) #output : 2.0 flaot division
print(z//y) #output : 2 int division
print(5**2) # ** this is used for power of anything 
print(32%5) # remainder provide

"""Assignment Operator
used to assign value to variable
                                  """
#compound assignment operations
aa=20
aa+=40
aa+=60
aa-=20
aa*=2
aa/=2
aa//=3
aa**=2
print(aa)

#comparison operator:woek with number and also with string
BB=12.1
bb=12
print(BB==bb)
print(BB!=bb)
print(BB>bb)
print(45<67)
print(33>44)
print(23>=23)
print(45<=45)

print(ord("A"))#that help to print ascii value of A i.e 65
print(ord("B")) #i.e 66
print("A">"B")#false
print("ABC">"ACD") #checking on the basis of precedemce of character i.e reslut is false because A both equal but B and C are different ascii vlaue and C is greater than B

"""logical  operator: AND, OR , NOT"""

print(123>100 and 34==34)
print(12 !=12 or 23==45 or 67==57 or 10>5)
print(not 12==12)









