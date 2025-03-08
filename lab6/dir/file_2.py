import os

def check(path):
    if not os.path.exists(path):
        print("The specified path does not exist")
        return
    
    print("The path exists")
    print("Readable:", "Yes" if os.access(path, os.R_OK) else "No")
    print("Writable:", "Yes" if os.access(path, os.W_OK) else "No")
    print("Executable:", "Yes" if os.access(path, os.X_OK) else "No")

path = input("Enter the directory path: ")
check(path)
