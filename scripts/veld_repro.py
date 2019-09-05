import sys
import json
from operator import itemgetter

from esipy import EsiApp, EsiClient

# create Esipy app and client
esi_app = EsiApp()
app = esi_app.get_latest_swagger
client = EsiClient(
    retry_requests=True,
    headers={
        "User-Agent": "Something CCP can use to contact you and that define your app"
    },
    raw_body_only=False,
)
# check response status
op = app.op["get_markets_region_id_orders"](
    region_id=10000002, type_id=34, order_type="sell"
)
res = client.head(op)
if not res.status == 200:
    sys.exit()
# market call for tritanium
market_order_operation = app.op["get_markets_region_id_orders"](
    region_id=10000002, type_id=34, order_type="sell"
)
raw_response = client.request(market_order_operation, raw_body_only=True)
# limit to Jita station
jita = []
orders = json.loads(raw_response.raw)
for order in orders:
    if order["location_id"] == 60003760:
        jita.append(order)
# Find minimum sell price
min_order = min(jita, key=itemgetter("price"))
min_price = min_order.get("price")
print("Tritanium Minimum-Sell:")
print(min_price)
# print("Minimum Price:")(min_price)
###-----------------------------------------------------------------------------###
### type id reference
###-----------------------------------------------------------------------------###
# type id reference
# 34 = Tritanium
# 28432 = Compressed Veldspar
# 46705 = Compressed Stable Veldspar
# 28431 = Compressed Dense Veldspar
# 28430 = Compressed Concentrated Veldspar
###-----------------------------------------------------------------------------###
###Refining Reference
###-----------------------------------------------------------------------------###
# 0.7977 = Refining Rate
# 331 = Compressed Veldspar
# 380 = Compressed Stable Veldspar
# 364 = Compressed Dense Veldspar
# 347 = Compressed Concentrated Veldspar
be_veldspar = 331 * min_price - ((331 * min_price) * 0.05)
be_stable = 380 * min_price - ((380 * min_price) * 0.05)
be_dense = 364 * min_price - ((364 * min_price) * 0.05)
be_concentrated = 347 * min_price - ((347 * min_price) * 0.05)
print("Maximum ore prices to break even.")
print("Compressed Veldspar:")
print(float("{0:.2f}".format(be_veldspar)))
print("Compressed Stable Veldspar:")
print(float("{0:.2f}".format(be_stable)))
print("Compressed Dense Veldspar:")
print(float("{0:.2f}".format(be_dense)))
print("Compressed Concentrated Veldspar:")
print(float("{0:.2f}".format(be_concentrated)))
