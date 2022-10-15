import sqlite3
db = sqlite3.connect('test.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS materials(
        id integer primary key autoincrement,
        name text not null
    ) """)
sql.execute(""" insert into materials(name) values('ДСП')  """)
sql.execute(""" select * from materials """)
rows = sql.fetchall()
for row in rows:
    print(row)
