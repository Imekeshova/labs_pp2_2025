import psycopg2
import csv
import configparser

import psycopg2
from config import load_config

params = load_config()  # {'host': ..., 'database': ..., ...}
conn = psycopg2.connect(**params)
cur = conn.cursor()


# 1. Создание таблицы
def create_table():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        phone VARCHAR(20) NOT NULL
    );
    """)
    conn.commit()

# 2. Вставка из CSV
def insert_from_csv(filename):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("Данные из CSV загружены!")

# 2. Вставка вручную
def insert_from_console():
    name = input("Введите имя: ")
    phone = input("Введите телефон: ")
    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Данные добавлены!")

# 3. Обновление данных
def update_data():
    name = input("Введите имя пользователя, которого хотите обновить: ")
    print("Что вы хотите изменить?\n1. Имя\n2. Телефон")
    choice = input("Выберите (1/2): ")
    if choice == '1':
        new_name = input("Новое имя: ")
        cur.execute("UPDATE phonebook SET username = %s WHERE username = %s", (new_name, name))
    elif choice == '2':
        new_phone = input("Новый телефон: ")
        cur.execute("UPDATE phonebook SET phone = %s WHERE username = %s", (new_phone, name))
    else:
        print("Неверный выбор.")
        return
    conn.commit()
    print("Данные обновлены!")

# 4. Поиск данных
def query_data():
    print("Фильтр поиска:\n1. По имени\n2. По телефону\n3. Все записи")
    choice = input("Выберите: ")
    if choice == '1':
        name = input("Введите имя для поиска: ")
        cur.execute("SELECT * FROM phonebook WHERE username ILIKE %s", (f"%{name}%",))
    elif choice == '2':
        phone = input("Введите телефон: ")
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
    else:
        cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# 5. Удаление данных
def delete_data():
    print("Удалить по:\n1. Имени\n2. Телефону")
    choice = input("Выберите: ")
    if choice == '1':
        name = input("Введите имя для удаления: ")
        cur.execute("DELETE FROM phonebook WHERE username = %s", (name,))
    elif choice == '2':
        phone = input("Введите телефон для удаления: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    else:
        print("Неверный выбор.")
        return
    conn.commit()
    print("Данные удалены.")

# Меню
def menu():
    create_table()
    while True:
        print("\n📒 Телефонная книга:")
        print("1. Загрузить данные из CSV")
        print("2. Добавить пользователя вручную")
        print("3. Обновить данные")
        print("4. Найти пользователя")
        print("5. Удалить пользователя")
        print("6. Выход")
        choice = input("Выберите действие: ")
        if choice == '1':
            insert_from_csv("data.csv")
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_data()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_data()
        elif choice == '6':
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

# Запуск
menu()
cur.close()
conn.close()
