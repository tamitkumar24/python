"""project on file handling"""

from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items=list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1}: {items}")

def createfile():
    try:
        readfileandfolder()
        name=input("please tell your file name:- ")
        p=Path(name) 
        if not p.exists() and p.is_file():
            with open(p,'w') as fs:
                data=input("what you wnat to write in this file/folder")
                fs.write(data)
            print(f"File created successfully")
        else:
            print("this file already exist")
    except Exception as err:
        print(f"An error occurred as {err}")

def readfile():
        try:
            readfileandfolder()
            name=input("which file you want to read:- ")
            p=Path(name) 
            if  p.exists() and p.is_file():
                with open(p,'r') as fs:
                    data=fs.read()
                    print(data)
                print(f"Read successfully")
            else:
                print("this file doesnot exist")
        except Exception as err:
            print(f"An error occurred as {err}")


def updatefile():
    try:
        readfileandfolder()
        name= input("tell which file you want to update:- ")
        p=Path(name) 
        if  p.exists() and p.is_file():
            print("press 1 for changing the name of your file:-")
            print("press 2 for overwriting the data of your file:- ")
            print("press 3 for appending some content in your file")

            response=int(input("tell your response:- "))

            if response==1:
                name2=input("tell your new file name:- ")
                p2 = Path(name2)
                p.rename(p2)

            if response==2:
                with open(p, 'w') as fs:
                    data= input("tell what you want to write this is overwrite the data:- ")
                    fs.write(data)

            if response==3:
                with open(p, 'a') as fs:
                    data= input("tell what  you want to append:- ")
                    fs.write(" " +data)
    except Exception as err:
            print(f"An error occurred as {err}")


def deletefile():
    try:
         readfileandfolder()
         name= input("tell which file you want to delete :- ")
         p=Path(name) 

         if  p.exists() and p.is_file():
             os.remove(p)

             print("file remove successfully")
         else:
             print("NO such file exist")

    except Exception as err:
            print(f"An error occurred as {err}")

      


print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for  deletion a file")

check=int(input("please tell you response:-"))

if check==1:
    createfile()

if check ==2:
    readfile()

if check ==3:
    updatefile()

if check==4:
    deletefile()









