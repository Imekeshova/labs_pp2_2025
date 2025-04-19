import psycopg2
from config import load_config

params = load_config()
conn = psycopg2.connect(**params)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        phone VARCHAR(20) NOT NULL
    );
""")

conn.commit()
print(" Таблица phonebook успешно создана.")

cur.close()
conn.close()
