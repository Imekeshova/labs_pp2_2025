def squares(a,b):
    for i in range(a,b):
        yield i ** 2
        
a = int(input("Enter a: "))
b = int(input("Enter b: "))
for j in squares(a,b):
    print(j, end=" ")