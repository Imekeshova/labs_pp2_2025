import psycopg2
import csv
from config import load_config

params = load_config()
conn = psycopg2.connect(**params)
cur = conn.cursor()

filename = 'data.csv'

with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) >= 2:
            cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (row[0], row[1]))

conn.commit()
print("Данные из CSV успешно добавлены.")

cur.close()
conn.close()
