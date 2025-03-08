import os

def wr_list(filename, data_list):
    with open(filename, "w", encoding="utf-8") as file:
        for item in data_list:
            file.write(item + "\n")

filename = input("your file: ")
data_list = input().split(",")
wr_list(filename, data_list)
