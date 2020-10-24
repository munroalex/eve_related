#imports
from esipy import EsiApp
from esipy import EsiClient
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

#type_id dictionary
type_ids = {"Veldspar":1230,"Scordite":1228, "Pyroxeres":1224, "Plagioclase":18, "Omber":1227, "Kernite":20,
           "Jaspet":1226, "Hemorphite":1231,"Hedbergite":21, "Gneiss":1229, "Dark Ochre":1232, "Crokite":1225,
           "Bistot":1223, "Arkonor":22, "Mercoxit":11396,"Spodumain":19, "Bezdnacine":52316, "Rakovene":52315,
           "Talassonite":52306,"Tritanium":34,"Pyerite":35,"Mexallon":36,"Isogen":37,"Nocxium":38,"Zydrine":39,
           "Megacyte":40,"Morphite":11399}
#mineral content in reprocessed ores nested dictionary
reprocessed_ores = {"Veldspar": {"Tritanium":400},
                    "Scordite": {"Tritanium":150,"Pyerite":90},
                    "Pyroxeres": {"Pyerite":90,"Mexallon":30},
                    "Plagioclase": {"Tritanium":175,"Mexallon":70},
                    "Omber": {"Pyerite":90,"Isogen":75},
                    "Kernite": {"Mexallon":60,"Isogen":120},
                    "Jaspet": {"Mexallon":150,"Nocxium":50},
                    "Hemorphite": {"Isogen":240,"Nocxium":90},
                    "Hedbergite": {"Pyerite":450,"Nocxium":120},
                    "Gneiss": {"Pyerite":2000,"Mexallon":1500,"Isogen":800},
                    "Dark Ochre": {"Mexallon":1360,"Isogen":1200,"Nocxium":320},
                    "Crokite": {"Pyerite":800,"Mexallon":2000,"Nocxium":800},
                    "Bistot": {"Pyerite":3200,"Mexallon":1200,"Zydrine":160},
                    "Arkonor": {"Pyertie":3200,"Mexallon":1200,"Megacyte":120},
                    "Mercoxit": {"Morphite":140},
                    "Spodumain": {"Tritanium":48000,"Isogen":1000,"Nocxium":160,"Zydrine":80,"Megacyte":40},
                    "Bezdnacine": {"Tritanium":40000,"Isogen":4800,"Megacyte":128},
                    "Rakovene": {"Tritanium":40000,"Isogen":3200,"Zydrine":200},
                    "Talassonite": {"Tritanium":40000,"Nocxium":960,"Megacyte":32}      
                    }

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
    
    #create empty dictionary
price_list = {}
#loop through items and grab prices
for key in type_ids:
    get_min_jita_price(key)

print(price_list)

#Reprocessing modifiers
rig_modifier = {"No Rig":0,"T1 Rig":0.01,"T2 Rig":0.03}
sec_modifier = {"High Sec":0,"Low Sec":0.06,"Null Sec":0.12}
struct_modifier = {"Athanor":0.02,"Tatara":0.04}
reprocessing_skill = {"0":0.00,"1":0.03,"2":0.06,"3":0.09,"4":0.12,"5":0.15}
reprocessing_efficiency_skill = {"0":0.00,"1":0.02,"2":0.04,"3":0.06,"4":0.08,"5":0.10}
ore_skill = {"0":0.00,"1":0.02,"2":0.04,"3":0.06,"4":0.08,"5":0.10}
implant_modifier = {"801":0.01,"802":0.02,"804":0.04}
#reprocessing yield calculation
reprocessing_yield=(0.5 + rig_modifier["T2 Rig"] * ( 1 + sec_modifier["High Sec"])) * (1 + struct_modifier["Tatara"]) * (1 + (reprocessing_skill["5"])) * (1 + (reprocessing_efficiency_skill["5"])) * (1 + (ore_skill["5"])) * (1 + implant_modifier["804"])

#test profit calculation
profit = (price_list["Veldspar"]["Volume"] / 100) * (price_list["Tritanium"]["Price"] * (400 * reprocessing_yield)) - (price_list["Veldspar"]["Price"] * 100) 
print(profit)

