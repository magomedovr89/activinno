import sqlite3

db = sqlite3.connect('DataBaseTest.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS base(
    username TEXT,
    id BIGINT unique,
    city TEXT,
    active BOOLEAN
    )""")

db.commit()
