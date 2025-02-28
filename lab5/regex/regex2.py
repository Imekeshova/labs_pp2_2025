import re

data = input()
pattern = r"ab{2,3}"
matches = re.findall(pattern, data)
print(matches)
