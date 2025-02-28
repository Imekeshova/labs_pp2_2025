import re

data = input()
pattern = r"[ ,.]"
replaced = re.sub(pattern, ":", data)
print(replaced)
