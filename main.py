import sqlite3


def print_qsl_line(sql):
    lines = sql.fetchall()
    for line in lines:
        print(*line)
    print()


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

#region Inserts
# sql.execute("""INSERT INTO types(type) VALUES ('Брус'), ('Брусок'), ('Доска'), ('Штакетник'), ('Шпала'), ('Обапол'),
#                                               ('Горбыль'), ('Конструкционные'), ('Торцованные'), ('Неторцованные')""")
#
# sql.execute("""INSERT INTO supliers(company, location, type_id) VALUES ('SIBWD', 'Россия', '1'), ('SIBWD', 'Россия', '3'), ('SIBWD', 'Россия', '5'),
#                                                                        ('CALAMBER', 'Канада', '2'), ('CALAMBER', 'Канада', '6'), ('USWOOD', 'США', '7'),
#                                                                        ('USWOOD', 'США', '2'), ('USWOOD', 'США', '1'), ('SIBWD', 'Россия', '7'),
#                                                                        ('SIBWD', 'Россия', '2')""")
#
# sql.execute("""INSERT INTO sales(customer, status) VALUES (('IP_1'),('0')), (('IP_2'),('0')), (('IP_3'),('0')), (('IP_4'),('0')), (('IP_5'),('0')),
#                                                           (('IP_6'),('0')), (('IP_7'),('0')), (('IP_8'),('0')), (('IP_9'),('0')), (('IP_10'),('0'))""")
#
# sql.execute("""INSERT INTO customer_list(customer_id, type_id, count) VALUES (('1'), ('5'), ('1000')), (('2'), ('1'), ('10000')), (('3'), ('2'), ('3000')),
#                                                                              (('4'), ('7'), ('5000')), (('5'), ('3'), ('8000')), (('6'), ('5'), ('4000')),
#                                                                              (('7'), ('1'), ('500')), (('8'), ('3'), ('1000')), (('9'), ('5'), ('1000')),
#                                                                              (('10'), ('2'), ('1000'))""")
#
# db.commit()
# endregion

# region Selects
sql.execute("""SELECT * FROM types""")
print('Table types', 'id|type', sep='\n')
print_qsl_line(sql)

sql.execute("""SELECT * FROM supliers""")
print('Table supliers', 'id|company|location|type_id', sep='\n')
print_qsl_line(sql)

sql.execute("""SELECT * FROM customer_list""")
print('Table supliers', 'id|customer_id|type_id|count', sep='\n')
print_qsl_line(sql)

sql.execute("""SELECT * FROM sales""")
print('Table supliers', 'id|customer|status', sep='\n')
print_qsl_line(sql)

sql.execute("""SELECT * FROM storage""")
print('Table supliers', 'id|type_id|current_count', sep='\n')
print_qsl_line(sql)

sql.execute("""SELECT customer, type, count FROM customer_list c, types t, sales s WHERE c.customer_id = s.id and 
               c.type_id = t.id ORDER BY customer""")
print('Readable customer list', 'customer|type|count', sep='\n')
print_qsl_line(sql)

sql.execute("""SELECT type, current_count FROM storage s, types t WHERE s.type_id = t.id ORDER BY type""")
print('Readable storage list', 'type|current_count', sep='\n')
print_qsl_line(sql)

sql.execute("""SELECT company, location, type FROM supliers s, types t WHERE s.type_id = t.id ORDER BY company""")
print('Readable supliers', 'company|location|type', sep='\n')
print_qsl_line(sql)

sql.execute("""SELECT customer, type, count, current_count FROM sales s, customer_list c, types t, storage st 
               WHERE c.customer_id = s.id and c.type_id = t.id and st.type_id = c.type_id ORDER BY customer""")
print('Order', 'customer|type|order_count|current_count', sep='\n')
print_qsl_line(sql)

sql.execute("""SELECT customer, type, sp.company as supplier, count, current_count FROM sales s, customer_list c, types 
               t, storage st, supliers sp WHERE c.customer_id = s.id and c.type_id = t.id and st.type_id = c.type_id 
               and sp.type_id = c.type_id ORDER BY customer""")
print('Order and suppliers for choose', 'customer|type|supplier|count|current_count', sep='\n')
print_qsl_line(sql)
# endregion

## TODO: Updates and Deletes

# region Updates

# endregion

# region Deletes

# endregion

sql.close()
