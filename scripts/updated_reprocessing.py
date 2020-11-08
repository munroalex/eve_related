#imports
from esipy import EsiApp
from esipy import EsiClient
from resources import type_ids, reprocessed_ores, reprocessing_yield, ore_list
import sys
import json
#create app
esi_app = EsiApp()
app = esi_app.get_latest_swagger
#create client
client = EsiClient(
    retry_requests=True,  # set to retry on http 5xx error (default False)
    headers={'User-Agent': 'Something CCP can use to contact you and that define your app'},
    raw_body_only=False,  # default False, set to True to never parse response and only return raw JSON string content.
)

#function for getting the minimum price of items in Jita
def get_min_jita_price(item):
    #get type_id of mineral input
    type_id = type_ids.get(item)
    #create request to swagger interface
    market_order_operation = app.op['get_markets_region_id_orders'](
        region_id=10000002,
        type_id=type_id,
        order_type='sell',
    )
    #make request
    response = client.request(market_order_operation, raw_body_only=True)
    #limit orders to Jita station
    station = []
    orders = json.loads(response.raw)
    for order in orders:
        if order["location_id"] == 60003760:
            station.append(order)
    # Find minimum sell price
    try:
        price = [x['price'] for x in station]
        minimum_price = min(price)
        #find total volume within 5% of minimum price
        volume = []
        for order in station:
            if order['price'] <= minimum_price*1.05:
                volume.append(order['volume_remain'])
        sum_volume = sum(volume)
    
        #add item price and volume to dictionary
        price_list[item] = {"Price":minimum_price,"Volume":sum_volume}
    except:
        pass
    
#create empty dictionary for all prices and volumes
price_list = {}
#loop through items and grab prices and volumes
for key in type_ids:
    get_min_jita_price(key)

for ore in ore_list:
    try:
        total_mineral_value = []
        ore_value = price_list[ore]["Price"] * 100
        total_mineral_mass = []
        for key in reprocessed_ores[ore]:
            mineral_price = price_list[key]["Price"]
            mineral_value = mineral_price * reprocessed_ores[ore][key] * reprocessing_yield
            mineral_mass = reprocessed_ores[ore][key] * reprocessing_yield * volumes[key] * price_list[ore]["Volume"]
        
            total_mineral_mass.append(mineral_mass)
            total_mineral_value.append(mineral_value)
        profit = (price_list[ore]["Volume"] / 100) * ((sum(total_mineral_value) - (sum(total_mineral_value) * broker_fee) - (sum(total_mineral_value) * sales_tax)) - ore_value)
        if profit > 25000000:
            print('Ore to purchase: ' + ore)
            print('Volume to purchase: ' + '{:,.0f}'.format(price_list[ore]["Volume"]))
            print('Max purchase price: $' + '{:,.2f}'.format(price_list[ore]["Price"]))
            print('Total cost: $' + '{:,.2f}'.format(price_list[ore]["Volume"] * price_list[ore]["Price"]))
            print("Profit: $" + '{:,.2f}'.format(profit))
            for key in reprocessed_ores[ore]:
                print('Min sell price: ' + key + ': $' + '{:,.2f}'.format(price_list[key]["Price"]))
            print('------------------------------')
            
    except:
        pass

