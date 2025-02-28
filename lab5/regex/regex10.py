import re

data = input()
matches = re.sub(r"([A-Z])", r"_\1", data).lower()
print(matches)
