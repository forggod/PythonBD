import sqlite3

# region Create database
# --
# -- База данных: `industrial_wood`
# --
db = sqlite3.connect('industrial_wood.db')
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

# sql.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = sql.fetchall()
# for line in tables:
#     print(line)

# sql.execute("""INSERT INTO types(type) VALUES ('Брус'), ('Брусок'), ('Доска'), ('Штакетник'), ('Шпала'), ('Обапол'),
#                                               ('Горбыль'), ('Конструкционные'), ('Торцованные'), ('Неторцованные')""")

# sql.execute("""INSERT INTO supliers(company, location, type_id) VALUES ('SIBWD', 'Россия', '1'), ('SIBWD', 'Россия', '3'), ('SIBWD', 'Россия', '5'),
#                                                                        ('CALAMBER', 'Канада', '2'), ('CALAMBER', 'Канада', '6'), ('USWOOD', 'США', '7'),
#                                                                        ('USWOOD', 'США', '2'), ('USWOOD', 'США', '1'), ('SIBWD', 'Россия', '7'),
#                                                                        ('SIBWD', 'Россия', '2')""")

sql.execute("""""")

db.commit()

sql.close()
