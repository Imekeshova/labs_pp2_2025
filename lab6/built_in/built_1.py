import math

def multiply_list(nums):
    return math.prod(nums)

n = int(input("enter n:"))
nums = []  
for i in range(n):  
    num = int(input("element: "))  
    nums.append(num)  

print("product:", multiply_list(nums))  
