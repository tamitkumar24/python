"""project on file handling"""

from pathlib import Path

def readfileandfolder():
    path=path('')
    item=list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1}: {items}")

def createfile():
    try:
        readfileandfolder()
        name=input("please tell your file name:- ")
        p=Path(name) 
        if not p.exists():
            with open(p,'w') as fs:
                data=input("what you wnat to write in this file/folder")
                fs.write(data)
            print(f"File created successfully")
        else:
            print("this file already exist")
    except Exception as err:
        print(f"An error occurred as {err}")







print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for  deletion a file")

check=int(input("please tell you response:-"))

if check==1:
    createfile()




