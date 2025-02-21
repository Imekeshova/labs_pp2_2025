#squares until n
def squares_gen(n):
    for i in range(1, n + 1):
        yield i ** 2

n = int(input("Enter n: "))
for j in squares_gen(n):
    print(j)