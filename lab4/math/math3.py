import math
n = int(input("Input number of sides:" ))
a = int(input("Input the length of a side:" ))
area = (n * a**2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:",int(area))