from itertools import permutations

string = input()
for i in permutations(string):
    print("".join(i))