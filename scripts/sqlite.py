import sqlite3

conn = sqlite3.connect('orders.db')

c = conn.cursor()

c.execute("""CREATE TABLE orders (
                duration integer,
                is_buy_order integer,
                issued text,
                location_id integer,
                min_volume integer,
                order_id integer primary key unique,
                price real,
                range text,
                system_id integer,
                type_id integer,
                volume_remain integer,
                volume_total integer,
                last_seen text default (datetime(current_timestamp))
               )""")

#c.execute("INSERT INTO orders VALUES")

conn.commit()

conn.close()