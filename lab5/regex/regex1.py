import re

n = input("ENTER test: ").split()

print("Task 1")

for string in n:
    if re.search(r"ab*", string):
        print(string, end=" ")