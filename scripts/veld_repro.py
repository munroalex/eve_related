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
tritanium_order_operation = app.op["get_markets_region_id_orders"](
    region_id=10000002, type_id=34, order_type="sell"
)
tritanium_response = client.request(tritanium_order_operation, raw_body_only=True)
# limit to Jita station
jita = []
tritanium_orders = json.loads(tritanium_response.raw)
for order in tritanium_orders:
    if order["location_id"] == 60003760:
        jita.append(order)
# Find minimum sell price
min_order = min(jita, key=itemgetter("price"))
min_price = min_order.get("price") - 0.05
print("Tritanium Minimum-Sell:")
print(min_price)
be_veldspar = 331 * min_price - ((331 * min_price) * 0.053)
be_stable = 380 * min_price - ((380 * min_price) * 0.053)
be_dense = 364 * min_price - ((364 * min_price) * 0.053)
be_concentrated = 347 * min_price - ((347 * min_price) * 0.053)

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
###-----------------------------------------------------------------------------###
# market call for ores
###-----------------------------------------------------------------------------###
# veldspar
veldspar_order_operation = app.op["get_markets_region_id_orders"](
    region_id=10000002, type_id=28432, order_type="sell"
)
veldspar_response = client.request(veldspar_order_operation, raw_body_only=True)
veldspar_orders = json.loads(veldspar_response.raw)
veldspar = []
for order in veldspar_orders:
    if order["price"] < be_veldspar:
        veldspar.append(order)
sum_veld = 0
for order in veldspar:
    sum_veld = sum_veld + order["volume_remain"]


# stable_veldspar
stable_veldspar_order_operation = app.op["get_markets_region_id_orders"](
    region_id=10000002, type_id=46705, order_type="sell"
)
stable_veldspar_response = client.request(
    stable_veldspar_order_operation, raw_body_only=True
)
stable_veldspar_orders = json.loads(stable_veldspar_response.raw)
stable_veldspar = []
for order in stable_veldspar_orders:
    if order["price"] < be_stable:
        stable_veldspar.append(order)
sum_stable = 0
for order in stable_veldspar:
    sum_stable = sum_stable + order["volume_remain"]


# dense_veldspar
dense_veldspar_order_operation = app.op["get_markets_region_id_orders"](
    region_id=10000002, type_id=28431, order_type="sell"
)
dense_veldspar_response = client.request(
    dense_veldspar_order_operation, raw_body_only=True
)
dense_veldspar_orders = json.loads(dense_veldspar_response.raw)
dense_veldspar = []
for order in dense_veldspar_orders:
    if order["price"] < be_dense:
        dense_veldspar.append(order)
sum_dense = 0
for order in dense_veldspar:
    sum_dense = sum_dense + order["volume_remain"]


# concentrated_veldspar
conc_veldspar_order_operation = app.op["get_markets_region_id_orders"](
    region_id=10000002, type_id=28430, order_type="sell"
)
conc_veldspar_response = client.request(
    conc_veldspar_order_operation, raw_body_only=True
)
conc_veldspar_orders = json.loads(conc_veldspar_response.raw)
conc_veldspar = []
for order in conc_veldspar_orders:
    if order["price"] < be_concentrated:
        conc_veldspar.append(order)
sum_conc = 0
for order in conc_veldspar:
    sum_conc = sum_conc + order["volume_remain"]

###-----------------------------------------------------------------------------###


print("Maximum ore prices to break even.")
print("Compressed Veldspar:")
print("Volume below threshold:")
print(sum_veld)
print("Price:")
print(float("{0:.2f}".format(be_veldspar)))
print("#------------------------------------#")
print("Compressed Stable Veldspar:")
print("Volume below threshold:")
print(sum_stable)
print("Price:")
print(float("{0:.2f}".format(be_stable)))
print("#------------------------------------#")
print("Compressed Dense Veldspar:")
print("Volume below threshold:")
print(sum_dense)
print("Price:")
print(float("{0:.2f}".format(be_dense)))
print("#------------------------------------#")
print("Compressed Concentrated Veldspar:")
print("Volume below threshold:")
print(sum_conc)
print("Price:")
print(float("{0:.2f}".format(be_concentrated)))
