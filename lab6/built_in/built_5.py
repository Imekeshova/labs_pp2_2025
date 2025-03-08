size_mylist = input("Enter numbers separated by spaces: ")  
my_list = []  

for i in size_mylist.split():  
    if i.isdigit():  
        my_list.append(int(i))  
    else:
        my_list.append(bool(i))  

print("All elements are True:", all(my_list))
