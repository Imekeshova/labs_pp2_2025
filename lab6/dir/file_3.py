import os

def check_path(path):
    if os.path.exists(path):
        print("path exists")
        print("directory: ", os.path.dirname(path))
        print("file: ", os.path.basename(path))
    else:
        print("path does not exist")

path = input("Path: ")
check_path(path)
