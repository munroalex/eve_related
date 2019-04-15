import sqlite3
import datetime
from time import gmtime, strftime
now = datetime.datetime.now()
conn = sqlite3.connect('orders.db')

delta = datetime.timedelta(minutes=60)

c = conn.cursor()

hour_ago = datetime.datetime.now() - datetime.timedelta(minutes=1)
c.execute("SELECT count(*) FROM orders")


conn.commit()

#print(c.fetchone())
