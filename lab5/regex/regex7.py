import re

data = input()
pattern = r"_(\w)" 
converted = re.sub(pattern, lambda match: match.group(1).upper(), data)
print(converted)
