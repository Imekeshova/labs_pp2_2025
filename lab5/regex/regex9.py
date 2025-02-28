import re

data = input()
pattern = r'(?<!^)(?<!\s)([A-ZА-Я])'
splitted = re.sub(pattern, r' \1', data)
print(splitted)
