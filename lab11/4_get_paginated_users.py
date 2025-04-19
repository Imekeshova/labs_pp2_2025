import psycopg2
from config import load_config

# Создание функции из SQL-файла
def create_function(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        sql = file.read()

    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            conn.commit()
            print("Функция успешно создана.")

# Вызов функции с параметрами
def get_paginated_users(limit, offset):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM get_paginated_users(%s, %s);", (limit, offset))
            results = cur.fetchall()
            print("\nПолученные записи:")
            for row in results:
                print(row)

# Запуск
if __name__ == '__main__':
    create_function('get_paginated.sql')  # Сначала создаём функцию

    # Получаем лимит и смещение от пользователя
    lim = int(input("Сколько записей хочешь получить? "))
    off = int(input("С какого места начать (offset)? "))

    get_paginated_users(lim, off)  # Вызываем функцию
