import sqlite3

db = sqlite3.connect('DataBaseTest.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS base(
    id BIGINT unique,
    username TEXT
    )""")

db.commit()
