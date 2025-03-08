import os

def del_func(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            if os.access(path, os.W_OK):
                os.remove(path)
                print("File deleted")
            else:
                print("No permission to delete the file")
        else:
            print("This isnt a file")
    else:
        print("Path doesnt exist")

path = input("Enter path for file: ")

del_func(path)