import os

for i in range(26):
    letters = chr(65+ i)
    filename = letters + ".txt"
    with open (filename, "w") as file:
        file.write(filename)
    print("generated file", filename)