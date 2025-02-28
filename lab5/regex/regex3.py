import re

data = input()
pattern = r"\b[a-z]+_[a-z]+\b"
matches = re.findall(pattern, data)
print(matches)
