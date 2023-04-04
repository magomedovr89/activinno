import sqlite3



def connect_to_db():
    # con = sqlite3.connect('/home/magomedovr89/git/tbot/telegram_db.sqlite')
    con = sqlite3.connect('../db/telegram_db.sqlite')
    cur = con.cursor()
    return con, cur


def filled_db():
    con, cur = connect_to_db()
    cur.execute(f"""CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    telegram_id INTEGER NOT NULL,
                    text text NOT NULL
                    );""")
    con.commit()
    cur.execute(f"""CREATE TABLE IF NOT EXISTS user (
                    id INTEGER PRIMARY KEY,
                    is_bot BOOLEAN NOT NULL,
                    first_name text,
                    username text,
                    language_code text
                    );""")
    con.commit()
    con.close()


def insert_db_user_data(info):
    con, cur = connect_to_db()
    cur.execute(f"""INSERT OR IGNORE INTO user
                (id, is_bot, first_name, username, language_code)
                VALUES
                ('{info['id']}',
                '{info['is_bot']}',
                '{info['first_name']}',
                '{info['username']}',
                '{info['language_code']}');""")
    con.commit()
    con.close()


def insert_db_user_message(message):
    con, cur = connect_to_db()
    cur.execute(f"""INSERT INTO messages
                (telegram_id, text)
                VALUES
                ('{message['telegram_id']}',
                '{message['text']}');""")
    con.commit()
    con.close()


filled_db()


