def its_3_4_generator(n):
    for i in range(0, n):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter n: "))
for j in its_3_4_generator(n):
    print(j, end=" ")
