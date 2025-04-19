import psycopg2
from config import load_config

# Читаем SQL-процедуру из файла
def create_procedure(filename):
    with open(filename, 'r', encoding='utf-8') as file:  # Явно указываем UTF-8
        sql = file.read()

    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            conn.commit()
            print("Процедура успешно создана.")

# Вызываем SQL-процедуру insert_many_users
def insert_many_users(usernames, phones):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_many_users(%s::TEXT[], %s::TEXT[]);", (usernames, phones))
            conn.commit()
            print("Добавление завершено.")

# Ввод данных с консоли
def get_input():
    usernames = []
    phones = []
    while True:
        name = input("Введите имя пользователя (или 'стоп' для завершения): ").strip()
        if name.lower() == 'стоп':
            break
        phone = input(f"Введите номер телефона для {name}: ").strip()
        usernames.append(name)
        phones.append(phone)
    insert_many_users(usernames, phones)

# Запуск
if __name__ == '__main__':
    create_procedure('insert_many_users.sql')  # Создаём процедуру из файла
    get_input()  # Ввод данных с консоли
