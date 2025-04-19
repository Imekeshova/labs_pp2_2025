import psycopg2
from db_config import load_config

def save_progress(user_id, level, score):
    params = load_config()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)",
                (user_id, level, score))
    conn.commit()
    cur.close()
    conn.close()
