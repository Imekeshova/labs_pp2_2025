import os

def copy_con(filename, newfile):
    with open(filename, "r") as file:
        data = file.read()
    with open(newfile, "w") as copy_of_file:
        copy_of_file.write(data)

filename = input("Input source file: ")
newfile = input("Input destination file: ")

copy_con(filename, newfile)
print("File copied")
