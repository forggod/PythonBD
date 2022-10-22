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
# -- Структура таблицы `sales`
# --
sql.execute("""CREATE TABLE IF NOT EXISTS `sales` (
  `id` integer NOT NULL PRIMARY KEY AUTOINCREMENT,
  `customer` integer(11) NOT NULL,
  `status` boolean(1) NOT NULL DEFAULT 0
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


sql.execute("SELECT type, company, location FROM types, supliers WHERE types.id = supliers.type_id order by type")
tables = sql.fetchall()
for line in tables:
    print(*line)
print()

# sql.execute("SELECT customer, status, type, count, company, location FROM types, supliers, sales, "
#             "customer_list WHERE sales.id = customer_list.customer_id and customer_list.type_id = types.id;")
# tables = sql.fetchall()
# for line in tables:
#     print(line)

# sql.execute("""INSERT INTO types(type) VALUES ('Брус'), ('Брусок'), ('Доска'), ('Штакетник'), ('Шпала'), ('Обапол'),
#                                               ('Горбыль'), ('Конструкционные'), ('Торцованные'), ('Неторцованные')""")

# sql.execute("""INSERT INTO supliers(company, location, type_id) VALUES ('SIBWD', 'Россия', '1'), ('SIBWD', 'Россия', '3'), ('SIBWD', 'Россия', '5'),
#                                                                        ('CALAMBER', 'Канада', '2'), ('CALAMBER', 'Канада', '6'), ('USWOOD', 'США', '7'),
#                                                                        ('USWOOD', 'США', '2'), ('USWOOD', 'США', '1'), ('SIBWD', 'Россия', '7'),
#                                                                        ('SIBWD', 'Россия', '2')""")

# sql.execute("""INSERT INTO sales(customer, status) VALUES (('IP_1'),('0')), (('IP_2'),('0')), (('IP_3'),('0')), (('IP_4'),('0')), (('IP_5'),('0')),
#                                                           (('IP_6'),('0')), (('IP_7'),('0')), (('IP_8'),('0')), (('IP_9'),('0')), (('IP_10'),('0'))""")

# sql.execute("""INSERT INTO customer_list(customer_id, type_id, count) VALUES (('1'), ('5'), ('1000')), (('2'), ('1'), ('10000')), (('3'), ('2'), ('3000')),
#                                                                              (('4'), ('7'), ('5000')), (('5'), ('3'), ('8000')), (('6'), ('5'), ('4000')),
#                                                                              (('7'), ('1'), ('500')), (('8'), ('3'), ('1000')), (('9'), ('5'), ('1000')),
#                                                                              (('10'), ('2'), ('1000'))""")

# db.commit()

sql.close()
