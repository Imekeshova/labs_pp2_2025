from config import load_config
import psycopg2

# Функция для выполнения SQL-файла
def execute_sql_file(filename):
    with open(filename, 'r') as file:
        sql_code = file.read()

    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(sql_code)
            conn.commit()
            print("SQL процедура успешно создана из файла.")

# Функция для вызова процедуры с параметрами
def insert_or_update_user(name, phone):
    config = load_config()

    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
            conn.commit()
            print(f"Пользователь '{name}' добавлен или обновлён.")

# Запуск
if __name__ == '__main__':
    # Создаём SQL-процедуру (один раз, можно убрать после первого запуска)
    execute_sql_file('insert_or_update.sql')

    # Ввод данных с консоли
    username = input("Введите имя пользователя: ")
    phone = input("Введите номер телефона: ")

    # Вызов процедуры с введёнными данными
    insert_or_update_user(username, phone)
