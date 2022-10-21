import sqlite3
# db = sqlite3.connect('test.db')
# sql = db.cursor()
#
# sql.execute("""CREATE TABLE IF NOT EXISTS materials(
#         id integer primary key autoincrement,
#         name text not null
#     ) """)
# sql.execute(""" insert into materials(name) values('ДСП')  """)
# sql.execute(""" select * from materials """)
# rows = sql.fetchall()
# for row in rows:
#     print(row)
# db.close()

# region Create database
# --
# -- База данных: `industrial_wood`
# --
db = sqlite3.connect('industrial_wood')
sql = db.cursor()
# --
# -- Структура таблицы `types`
# --
sql.execute("""CREATE TABLE IF NOT EXISTS `types` (
  `id` integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  `type` varchar(1024) NOT NULL UNIQUE
)""")
# --
# -- Структура таблицы `sales`
# --
sql.execute("""CREATE TABLE IF NOT EXISTS `sales` (
  `id` integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  `customer` integer(11) NOT NULL,
  `status` boolean(1) NOT NULL DEFAULT 0
)""")
# --
# -- Структура таблицы `supliers`
# --
sql.execute("""CREATE TABLE IF NOT EXISTS `supliers` (
  `id` integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  `company` varchar(1024) NOT NULL,
  `location` varchar(1024) NOT NULL,
  `type_id` integer(11) NOT NULL,
   FOREIGN KEY ('type_id') REFERENCES 'types' ('id') ON DELETE CASCADE ON UPDATE CASCADE
)""")
# --
# -- Структура таблицы `customer_list`
# --
sql.execute("""CREATE TABLE IF NOT EXISTS `customer_list` (
    'id' integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    `customer_id` integer(11) NOT NULL ,
    `type_id` integer(11) NOT NULL,
    `count` integer(255) NOT NULL,
    FOREIGN KEY (`type_id`) REFERENCES `types` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (`customer_id`) REFERENCES `sales` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
    );""")
# endregion

sql.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = sql.fetchall()
for line in tables:
    print(line)
sql.close()
