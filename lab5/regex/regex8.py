import re

data = input()
pattern = r"(?=[A-ZА-Я])"  # Разбиваем перед заглавной буквой
matches = re.split(pattern, data)
print(matches)
