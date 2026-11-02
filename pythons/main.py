"""
mkdir -> to create a new folder/directory
rmdir -> to remove any folder/directory



files 
x -> This mode will only create the file and file and if already exist we will get an error back 

w -> agar file exists nahi kar rahi hai so this mode will create one and insert the content inside the file .

a
r
#mode 1: x-> just to create the file 
#open ("Garba.txt","x")

#mode 2: w-> if there is nay content inside the file so the new one will replace the old one.

# file = open("Garba.txt","w")
# file.write("enjoy karo job hi job hai")

# #Mode 3: a-> add the text at the last \.
# file = open ("Graba .txt","a")
# file.write("\n This message is newly added")

#Mode 4:
file = open("garba.txt","r")
print(file.read())
"""




# with open("sample.txt","w") as file:
#     file.write("This isnnew file")


#CRUD - CREATE,READ,UPDATE,DELETE
# os.remove("garba.txt")

from pathlib import Path
import os

def create_folder():
    name = input("Tell your folder name:-")
    p = Path(name)

    if p.exists():
        print("this folder name already exist please try again")
        create_folder()
    else:
        p.mkdir()
        print("folder created successfully !")

def read_folder():
    p = Path("")
    names = list(p.rglob("*"))

    for i in range(len(names)):
        print("{i+1} : {names[i]}")

def f update_folder()

print("Press 1 for creating a folder")
print("press 2 for reading a folder")
print("press 3 for updating a folder")
print("press 4 for deleting a folder")
print("press 5 for creating a file")
print("press 6 for readong a file:")
print("press 7 for updating a file:")
print("press 8 for deleting a file:")

res = int(input("Tell your response:-"))

if res == 1:
    create_folder()

if res == 2:
