
def count_lines(filename):
    counter = 0  
    with open(filename, "r", encoding="utf-8") as file:  
        for line in file:  
            counter += 1  
    print("Number of lines:", counter)

filename = input("Enter file name: ")  
count_lines(filename)  
