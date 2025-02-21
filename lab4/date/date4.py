from datetime import datetime, timedelta

first_data = datetime.now() - timedelta(days = 1)
second_data = datetime.now() + timedelta(days = 2)

diffrence = (second_data - first_data).total_seconds()
print(int(diffrence))