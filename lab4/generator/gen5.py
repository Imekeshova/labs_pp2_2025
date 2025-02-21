def gen_gen(n):
    for i in range(n, -1, -1):
        yield i
        
n = int(input("Enter n: "))
for j in gen_gen(n):
    print(j, end=" ")