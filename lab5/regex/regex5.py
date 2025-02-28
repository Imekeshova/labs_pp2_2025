import re

data = input()
pattern = r"\ba.+b\b"
matches = re.findall(pattern, data)
print(matches)
