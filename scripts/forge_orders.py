from esipy import EsiApp, EsiClient
import json, itertools, time, sqlite3, datetime

start = time.time()
conn = sqlite3.connect('orders.db')
c = conn.cursor()
esi_app = EsiApp()
app = esi_app.get_latest_swagger
client = EsiClient(
    retry_requests=True,
    headers={'User-Agent':'CorEl Dahken'},
    raw_body_only=False,
)
op = app.op['get_markets_region_id_orders'](
    region_id=10000002,
    page=1,
    order_type='all',
)
res = client.head(op)

if res.status == 200:
    number_of_page = res.header['X-Pages'][0]
print(number_of_page)

results = []
page = 1
while page <= number_of_page:
    market_order_operation = app.op['get_markets_region_id_orders'](
        region_id=10000002,
        page=page,
        order_type='all',
    )
    raw_response = client.request(market_order_operation, raw_body_only=True)
    print("Page Number:", page)
    forge_orders_json = json.loads(raw_response.raw)
    results.extend(forge_orders_json)
    page += 1

for order in results:
    table_name = 'orders'
    attrib_names = ", ".join(order.keys())
    attrib_values = ", ".join("?" * len(order.keys()))
    sql = f"REPLACE INTO {table_name} ({attrib_names}) VALUES ({attrib_values})"
    c.execute(sql, list(order.values()))

select = c.execute("SELECT count(*) FROM orders")
print(c.fetchall())

hour_ago = datetime.datetime.now() - datetime.timedelta(minutes=60)
query = "DELETE from orders WHERE last_seen < ?"
c.execute(query, (hour_ago,))
conn.commit()
conn.close()

end = time.time()
print(end - start)
