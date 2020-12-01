import pandas as pd
from esipy import EsiApp
from esipy import EsiClient
from esipy import EsiSecurity
from resources import scopes
import numpy as np
import json

app = EsiApp().get_latest_swagger

# replace the redirect_uri, client_id and secret_key values
# with the values you get from the STEP 1 !
security = EsiSecurity(
    redirect_uri="http://localhost:5000/eve_callback",
    client_id="0eeaaa5cec934a60a99f412d43cf387b",
    secret_key="3b5NR5uXW6hcGwT9H2gVMvKlp3NtCDk7zTBBt4cn",
    headers={"User-Agent": "munroa.alex@gmail.com"},
)

# and the client object, replace the header user agent value with something reliable !
client = EsiClient(
    retry_requests=True, headers={"User-Agent": "Corel Dahken"}, security=security,
)


"""type_ids = []
market_groups = app.op["get_markets_groups"]()
group_ids = client.request(market_groups)
print(group_ids)

for group in group_ids.data:
    print(group)
    market_ids = app.op["get_markets_groups_market_group_id"](market_group_id=group)
    groups = client.request(market_ids)
    group_ids = groups.data["types"]
    for id in group_ids:
        if id == None:
            pass
        else:
            type_ids.append(id)

df = pd.DataFrame(
    columns=["Name", "Jita_Price", "Amarr_Price", "Margin", "Percent", "ISK_Volume"],
    index=type_ids,
)
df.to_csv("type_ids.csv", index=True)"""
df = pd.read_csv("type_ids.csv", index_col=0)


def average(lists):
    average = sum(lists) / len(lists)
    return average


##############################################################################################################
def jita_prices():
    op = app.op["get_markets_region_id_orders"](
        region_id=10000002, page=1, order_type="sell",
    )
    res = client.head(op)
    jita_order_book = []
    # if we have HTTP 200 OK, then we continue
    if res.status == 200:
        number_of_page = res.header["X-Pages"][0]
        print(number_of_page)

        # now we know how many pages we want, let's prepare all the requests

        for page in range(1, number_of_page + 1):
            print(page)
            market_order_operation = app.op["get_markets_region_id_orders"](
                region_id=10000002, page=page, order_type="sell",
            )
            response = client.request(market_order_operation, raw_body_only=True)
            # limit orders to Jita station

            orders = json.loads(response.raw)

            for order in orders:
                if order["location_id"] == 60003760:
                    jita_order_book.append(order)

    print(len(jita_order_book))

    for index, row in df.iterrows():
        print(index)
        temp = []
        for order in jita_order_book:
            if order["type_id"] == index:
                temp.append(order)
        # print(temp)
        try:
            price = [x["price"] for x in temp]
            minimum_price = min(price)
            df["Jita_Price"][index] = minimum_price
        except:
            pass


##############################################################################################################

jita_prices()
print(df)

##############################################################################################################
def amarr_prices():
    op = app.op["get_markets_region_id_orders"](
        region_id=10000043, page=1, order_type="sell",
    )
    res = client.head(op)
    amarr_order_book = []
    # if we have HTTP 200 OK, then we continue
    if res.status == 200:
        number_of_page = res.header["X-Pages"][0]
        print(number_of_page)

        # now we know how many pages we want, let's prepare all the requests

        for page in range(1, number_of_page + 1):
            print(page)
            market_order_operation = app.op["get_markets_region_id_orders"](
                region_id=10000043, page=page, order_type="sell",
            )
            response = client.request(market_order_operation, raw_body_only=True)
            # limit orders to Jita station

            orders = json.loads(response.raw)

            for order in orders:
                if order["location_id"] == 60008494:
                    amarr_order_book.append(order)

    print(len(amarr_order_book))

    for index, row in df.iterrows():
        print(index)
        temp = []
        for order in amarr_order_book:
            if order["type_id"] == index:
                temp.append(order)
        # print(temp)
        try:
            price = [x["price"] for x in temp]
            minimum_price = min(price)
            df["Amarr_Price"][index] = minimum_price
        except:
            pass


##############################################################################################################

amarr_prices()
print(df)
##############################################################################################################
def get_history_amarr_price(item):
    # get type_id of mineral input
    type_id = item
    print(type_id)

    # create request to swagger interface
    price_list = []

    volume_list = []

    ###Forge Region Request###
    market_history_operation = app.op["get_markets_region_id_history"](
        region_id=10000043, type_id=type_id,
    )
    res = client.head(market_history_operation)
    # if status 200 all good to go
    if res.status == 200:
        # make request
        response = client.request(market_history_operation, raw_body_only=True)
        response = json.loads(response.raw)
        month = response[-30:]
        for date in range(len(month)):
            price = month[date]["average"]

            volume = month[date]["volume"]
            price_list.append(price)

            volume_list.append(volume)
        try:
            df["ISK_Volume"][index] = average(price_list) * average(volume_list)
        except:
            pass
        print(df["ISK_Volume"][index])


for index, row in df.iterrows():
    get_history_amarr_price(index)

df.to_csv("prices.csv", index=True)
