import psycopg2
from config import load_config as config

# Функция создания процедуры удаления
def create_procedure():
    with open('delete_user.sql', 'r', encoding='utf-8') as f:
        sql = f.read()

    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()

# Функция вызова удаления
def delete_user():
    username = input("Имя (или оставь пустым): ").strip()
    phone = input("Телефон (или оставь пустым): ").strip()
    username = username if username else None
    phone = phone if phone else None

    params = config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute("CALL delete_user(%s, %s);", (username, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Удалено")

# Запуск
create_procedure()
delete_user()
