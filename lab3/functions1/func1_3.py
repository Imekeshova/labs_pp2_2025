numheads = 35
numlegs = 94
def solve(numheads, numlegs): #цикл перебирает количечство кроликов  
    for rabbits in range (numheads + 1):
        chickens = numheads - rabbits #остальные это курицы
        if 4 * rabbits + 2 * chickens == numlegs: #проверка совпадает ли условие    
            return rabbits, chickens
    return "No solution"

print(solve(numheads, numlegs))
    