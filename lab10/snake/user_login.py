import psycopg2
from db_config import load_config

def get_or_create_user(username):
    params = load_config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    result = cur.fetchone()

    if result:
        user_id = result[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()

    cur.execute("SELECT level, score FROM user_score WHERE user_id = %s ORDER BY id DESC LIMIT 1", (user_id,))
    progress = cur.fetchone()
    cur.close()
    conn.close()
    return user_id, (progress if progress else (1, 0))  # уровень, счёт
