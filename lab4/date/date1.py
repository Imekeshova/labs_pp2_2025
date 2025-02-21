from datetime import datetime, timedelta

today = datetime.today()
five_days_ago = today - timedelta(days = 5)

print("Current time: ", today.strftime("%Y-%m-%d"))
print("Date 5 days ago: ", five_days_ago.strftime("%Y-%m-%d"))

