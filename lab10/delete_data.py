import psycopg2
from config import load_config

params = load_config()
conn = psycopg2.connect(**params)
cur = conn.cursor()

print("Удаление по:\n1 — Имени\n2 — Телефону")
choice = input("Ваш выбор: ")

if choice == '1':
    name = input("Введите имя: ")
    cur.execute("DELETE FROM phonebook WHERE username = %s", (name,))
elif choice == '2':
    phone = input("Введите телефон: ")
    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
else:
    print("Неверный выбор")

conn.commit()
print("Данные удалены.")

cur.close()
conn.close()
