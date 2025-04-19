import psycopg2
from config import load_config  # Загружаем параметры подключения из файла database.ini

# Создаём SQL-функцию в базе, которая ищет пользователей по букве "a" в имени
def create_search_function():
    sql = """
    -- Удаляем функцию, если она уже существует
    DROP FUNCTION IF EXISTS search_contacts();

    -- Создаём новую функцию search_contacts
    CREATE OR REPLACE FUNCTION search_contacts() 
    RETURNS TABLE(username VARCHAR, phone VARCHAR) AS $$
    BEGIN
        -- Возвращаем строки, где имя пользователя содержит букву 'a'
        RETURN QUERY
        SELECT phonebook.username, phonebook.phone
        FROM phonebook
        WHERE phonebook.username ILIKE '%a%';
    END;
    $$ LANGUAGE plpgsql;
    """
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            print("Функция search_contacts() создана или обновлена.")

# Вызываем SQL-функцию и печатаем найденные контакты
def call_search_contacts():
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM search_contacts();")
            results = cur.fetchall()

            print("\n Найденные контакты с буквой 'a' в имени:")
            for username, phone in results:
                print(f"Имя: {username}, Телефон: {phone}")

# Запускаем всё, когда файл запускается напрямую
if __name__ == '__main__':
    create_search_function()   # Сначала создаём или обновляем функцию
    call_search_contacts()     # Потом вызываем и выводим результат
