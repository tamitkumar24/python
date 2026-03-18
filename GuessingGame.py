""" Guessing Game by using While loop """

import random
num=random.randint(1,10)
tries=0
print(num)

while True:
     guess=int(input("please enter the number for guessing it:- "))

     if num==guess:
        print(f"you are right, you guess the number is {tries} tries")
        tries+=1
        break
     elif num<guess:
        print("go a little lower")
        tries+=1
     elif num>guess:
         print("go a little higher")
         tries+=1
     else:
        print("sorry you are wrong")
        tries+=1