import psycopg2
from config import load_config

params = load_config()
conn = psycopg2.connect(**params)
cur = conn.cursor()

name = input("Введите имя: ")
phone = input("Введите номер телефона: ")

cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (name, phone))

conn.commit()
print(" Данные добавлены в phonebook.")

cur.close()
conn.close()
