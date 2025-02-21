from datetime import datetime, timedelta
yesterday = datetime.today() - timedelta(days = 1)
today = datetime.today()
tomorrow = datetime.today() + timedelta(days = 1)

print("yesterday", yesterday.strftime("%Y-%m-%d"))
print("today", today.strftime("%Y-%m-%d"))
print("tomorrow", tomorrow.strftime("%Y-%m-%d"))