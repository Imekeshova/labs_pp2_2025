def even_gen(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i 

n = int(input("Enter n: "))

first = True
for j in even_gen(n):
    if not first:
        print(", " , end="")
    print(j, end="")
    first = False