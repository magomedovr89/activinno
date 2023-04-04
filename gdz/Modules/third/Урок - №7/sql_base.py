import sqlite3

con = sqlite3.connect('Homework.db')
cur = con.cursor()

cur.execute(f"""CREATE TABLE IF NOT EXISTS homework (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id BIGINT UNIQUE NOT NULL,
            username text,
            first_name text NOT NULL
            );""")


def insert(message) -> cur.execute:
    telegram_id = message['from']['id']
    username = message['from']['username']
    first_name = message['from']['first_name']
    cur.execute(f"""INSERT INTO homework
    (telegram_id, username, first_name) 
    VALUES 
    ('{telegram_id}',
    '{username}',
    '{first_name}');""")
    return con.commit()


con.commit()
