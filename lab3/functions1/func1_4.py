def filter_prime(n):
    if n < 2:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

numbers = input().split()
num_list = []
for num in numbers:
    num_list.append(int(num))
    
primes = []
for num in num_list:
    if filter_prime(num):
        primes.append(num)
        
print(primes)