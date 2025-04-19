import psycopg2
from config import load_config

params = load_config()
conn = psycopg2.connect(**params)
cur = conn.cursor()

print("Выберите фильтр:\n1 — По имени\n2 — По телефону\n3 — Показать всё")
choice = input("Ваш выбор: ")

if choice == '1':
    name = input("Введите имя для поиска: ")
    cur.execute("SELECT * FROM phonebook WHERE username ILIKE %s", (f"%{name}%",))
elif choice == '2':
    phone = input("Введите телефон для поиска: ")
    cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
elif choice == '3':
    cur.execute("SELECT * FROM phonebook")
else:
    print(" Неверный выбор")

rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()
