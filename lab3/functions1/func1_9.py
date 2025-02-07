def sphere_volume(radius): 
    pi = 3.14
    return (4/3) * pi * (radius ** 3)

radius = float(input())
print(sphere_volume(radius))
