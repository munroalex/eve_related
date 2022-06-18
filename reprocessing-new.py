import requests
import json

ore = {
    "Compressed Veldspar": {
        "Tritanium": 400
    },
    "Compressed Concentrated Veldspar":{
        "Tritanium": 420
    },
    "Compressed Dense Veldspar":{
        "Tritanium":440
    },
    "Compressed Stable Veldspar":{
        "Tritanium": 460
    },
    "Compressed Talassonite":{
        "Tritanium": 40000,
        "Nocxium": 960,
        "Megacyte": 32
    },
    "Compressed Hadal Talassonite":{
        "Tritanium": 44000,
        "Nocxium": 1056,
        "Megacyte": 35
    },
    "Compressed Abyssal Talassonite":{
        "Tritanium": 42000,
        "Nocxium": 1008,
        "Megacyte": 34
    },
    "Compressed Spodumain":{
        "Tritanium": 48000,
        "Isogen": 1000,
        "Nocxium": 160,
        "Zydrine": 80,
        "Megacyte": 40
    },
    "Compressed Bright Spodumain":{
        "Tritanium": 50400,
        "Isogen": 1050,
        "Nocxium": 168,
        "Zydrine": 84,
        "Megacyte": 42
    },
    "Compressed Gleaming Spodumain":{
        "Tritanium": 52800,
        "Isogen": 1100,
        "Nocxium": 176,
        "Zydrine": 88,
        "Megacyte": 44
    },
    "Compressed Dazzling Spodumain":{
        "Tritanium": 55200,
        "Isogen": 1150,
        "Nocxium": 184,
        "Zydrine": 92,
        "Megacyte": 46
    },
    "Compressed Scordite":{
        "Tritanium": 150,
        "Pyerite": 90
    },
    "Compressed Condensed Scordite":{
        "Tritanium": 158,
        "Pyerite": 95
    },
    "Compressed Massive Scordite":{
        "Tritanium": 165,
        "Pyerite": 99
    },
    "Compressed Glossy Scordite":{
        "Tritanium": 173,
        "Pyerite": 104
    },
    "Compressed Rakovene":{
        "Tritanium": 40000,
        "Isogen": 3200,
        "Zydrine": 200
    },
    "Compressed Abyssal Rakovene":{
        "Tritanium": 4200,
        "Isogen": 3360,
        "Zydrine": 210
    },
    "Compressed Hadal Rakovene":{
        "Tritanium": 44000,
        "Isogen": 3520,
        "Zydrine": 220
    },
    "Compressed Pyroxeres":{
        "Pyerite": 90,
        "Mexallon": 30
    },
    "Compressed Solid Pyroxeres":{
        "Pyerite": 95,
        "Mexallon": 32
    },
    "Compressed Viscous Pyroxeres":{
        "Pyerite": 99,
        "Mexallon": 33
    },
    "Compressed Opulent Pyroxeres":{
        "Pyerite": 104,
        "Mexallon": 35
    },
    "Compressed Plagioclase":{
        "Tritanium": 175,
        "Mexallon": 70
    },
    "Compressed Rich Plagioclase":{
        "Tritanium": 193,
        "Mexallon": 77
    },
    "Compressed Azure Plagioclase":{
        "Tritanium": 184,
        "Mexallon": 74
    },
    "Compressed Sparkling Plagioclase":{
        "Tritanium": 201,
        "Mexallon": 81
    },
    "Compressed Omber":{
        "Pyerite": 90,
        "Isogen": 75
    },
    "Compressed Silvery Omber":{
        "Pyerite": 95,
        "Isogen": 79
    },
    "Compressed Golden Omber":{
        "Pyerite": 99,
        "Isogen": 83
    },
    "Compressed Platinoid Omber":{
        "Pyerite": 104,
        "Isogen": 86
    },
    "Compressed Mercoxit":{
        "Morphite":140
    },
    "Compressed Magma Mercoxit":{
        "Morphite":147
    },
    "Compressed Viteous Mercoxit":{
        "Morphite":154
    },
    "Compressed Kernite":{
        "Mexallon": 60,
        "Isogen": 120
    },
    "Compressed Luminous Kernite":{
        "Mexallon": 63,
        "Isogen": 126
    },
    "Compressed Fiery Kernite":{
        "Mexallon": 66,
        "Isogen": 132
    },
    "Compressed Resplendant Kernite":{
        "Mexallon": 69,
        "Isogen": 138
    },
    "Compressed Jaspet":{
        "Mexallon": 150,
        "Nocxium": 50
    },
    "Compressed Pure Jaspet":{
        "Mexallon": 158,
        "Nocxium": 53
    },
    "Compressed Pristine Jaspet":{
        "Mexallon": 165,
        "Nocxium": 55
    },
    "Compressed Immaculate Jaspet":{
        "Mexallon": 173,
        "Nocxium": 58
    },
    "Compressed Hemorphite":{
        "Isogen": 240,
        "Nocxium": 90
    },
    "Compressed Vivid Hemorphite":{
        "Isogen": 252,
        "Nocxium": 95
    },
    "Compressed Radiant Hemorphite":{
        "Isogen": 264,
        "Nocxium": 99
    },
    "Compressed Scintillating Hemorphite":{
        "Isogen": 276,
        "Nocxium": 104
    },
    "Compressed Hedbergite":{
        "Pyerite": 450,
        "Nocxium": 120
    },
    "Compressed Vitric Hedbergite":{
        "Pyerite": 473,
        "Nocxium": 126
    },
    "Compressed Glazed Hedbergite":{
        "Pyerite": 495,
        "Nocxium": 132
    },
    "Compressed Lustrous Hedbergite":{
        "Pyerite": 518,
        "Nocxium": 138
    },
    "Compressed Gneiss":{
        "Pyerite": 2000,
        "Mexallon":1500,
        "Isogen": 800
    },
    "Compressed Iridescent Gneiss":{
        "Pyerite": 2100,
        "Mexallon":1575,
        "Isogen": 840
    },
    "Compressed Prismatic Gneiss":{
        "Pyerite": 2200,
        "Mexallon":1650,
        "Isogen": 880
    },
    "Compressed Brilliant Gneiss":{
        "Pyerite": 2300,
        "Mexallon":1725,
        "Isogen": 920
    },
    "Compressed Dark Ochre":{
        "Mexallon": 1360,
        "Isogen": 1200,
        "Nocxium": 320
    },
    "Compressed Onyx Ochre":{
        "Mexallon": 1428,
        "Isogen": 1260,
        "Nocxium": 336
    },
    "Compressed Obsidian Ochre":{
        "Mexallon": 1496,
        "Isogen": 1320,
        "Nocxium": 352
    },
    "Compressed Jet Ochre":{
        "Mexallon": 1564,
        "Isogen": 1380,
        "Nocxium": 368
    },
    "Compressed Crokite":{
        "Pyerite": 800,
        "Mexallon": 2000,
        "Nocxium": 800
    },
    "Compressed Sharp Crokite":{
        "Pyerite": 840,
        "Mexallon": 2100,
        "Nocxium": 840
    },
    "Compressed Crystalline Crokite":{
        "Pyerite": 880,
        "Mexallon": 2200,
        "Nocxium": 880
    },
    "Compressed Pellucid Crokite":{
        "Pyerite": 920,
        "Mexallon": 2300,
        "Nocxium": 920
    },
    "Compressed Bistot":{
        "Pyerite": 3200,
        "Mexallon": 1200,
        "Zydrine": 160
    },
    "Compressed Triclinic Bistot":{
        "Pyerite": 3360,
        "Mexallon": 1260,
        "Zydrine": 168
    },
    "Compressed Monoclinic Bistot":{
        "Pyerite": 3520,
        "Mexallon": 1320,
        "Zydrine": 176
    },
    "Compressed Cubic Bistot":{
        "Pyerite": 3680,
        "Mexallon": 1380,
        "Zydrine": 184
    },
    "Compressed Bezdnacine":{
        "Tritanium": 40000,
        "Isogen": 4800,
        "Megacyte": 128
    },
    "Compressed Abyssal Bezdnacine":{
        "Tritanium": 42000,
        "Isogen": 5040,
        "Megacyte": 134
    },
    "Compressed Hadal Bezdnacine":{
        "Tritanium": 44000,
        "Isogen": 5280,
        "Megacyte": 141
    },
    "Compressed Arkonor":{
        "Pyerite": 3200,
        "Mexallon": 1200,
        "Megacyte": 120
    },
    "Compressed Crimson Arkonor":{
        "Pyerite": 3360,
        "Mexallon": 1260,
        "Megacyte": 126
    },
    "Compressed Flawless Arkonor":{
        "Pyerite": 3680,
        "Mexallon": 1380,
        "Megacyte": 138
    },
    "Compressed Prime Arkonor":{
        "Pyerite": 3520,
        "Mexallon": 1320,
        "Megacyte": 132
    }
}

minerals = {
    "Tritanium": 34,
    "Pyerite": 35,
    "Mexallon": 36,
    "Isogen": 37,
    "Nocxium": 38,
    "Zydrine": 39,
    "Megacyte": 40,
    "Morphite": 11399
}
ore_ids = {
    "Compressed Veldspar": 62516, 
    "Compressed Concentrated Veldspar": 62517,
    "Compressed Dense Veldspar": 62518,
    "Compressed Stable Veldspar": 62519,
    "Compressed Talassonite": 62582,
    "Compressed Hadal Talassonite": 62584,
    "Compressed Abyssal Talassonite": 62583,
    "Compressed Spodumain": 62572,
    "Compressed Bright Spodumain": 62573,
    "Compressed Gleaming Spodumain": 62574,
    "Compressed Dazzling Spodumain": 62575,
    "Compressed Scordite": 62520,
    "Compressed Condensed Scordite": 62521,
    "Compressed Massive Scordite": 62522,
    "Compressed Glossy Scordite": 62523,
    "Compressed Rakovene": 62579,
    "Compressed Abyssal Rakovene": 62580,
    "Compressed Hadal Rakovene": 62581,
    "Compressed Pyroxeres": 62524,
    "Compressed Solid Pyroxeres": 62525,
    "Compressed Viscous Pyroxeres": 62526,
    "Compressed Opulent Pyroxeres": 62527,
    "Compressed Plagioclase": 62528,
    "Compressed Rich Plagioclase": 62530,
    "Compressed Azure Plagioclase": 62529,
    "Compressed Sparkling Plagioclase": 62531,
    "Compressed Omber": 62532,
    "Compressed Silvery Omber": 62533,
    "Compressed Golden Omber": 62534,
    "Compressed Platinoid Omber": 62535,
    "Compressed Mercoxit": 62586,
    "Compressed Magma Mercoxit": 62587,
    "Compressed Viteous Mercoxit": 62588,
    "Compressed Kernite": 62536,
    "Compressed Luminous Kernite": 62537,
    "Compressed Fiery Kernite": 62538,
    "Compressed Resplendant Kernite": 62539,
    "Compressed Jaspet": 62540,
    "Compressed Pure Jaspet": 62541,
    "Compressed Pristine Jaspet": 62542,
    "Compressed Immaculate Jaspet": 62543,
    "Compressed Hemorphite": 62544,
    "Compressed Vivid Hemorphite": 62545,
    "Compressed Radiant Hemorphite": 62546,
    "Compressed Scintillating Hemorphite": 62547,
    "Compressed Hedbergite": 62548,
    "Compressed Vitric Hedbergite": 62549,
    "Compressed Glazed Hedbergite": 62550,
    "Compressed Lustrous Hedbergite": 62551,
    "Compressed Gneiss": 62552,
    "Compressed Iridescent Gneiss": 62553,
    "Compressed Prismatic Gneiss": 62554,
    "Compressed Brilliant Gneiss": 62555,
    "Compressed Dark Ochre": 62556,
    "Compressed Onyx Ochre": 62557,
    "Compressed Obsidian Ochre": 62558,
    "Compressed Jet Ochre": 62559,
    "Compressed Crokite": 62560,
    "Compressed Sharp Crokite": 62561,
    "Compressed Crystalline Crokite": 62562,
    "Compressed Pellucid Crokite": 62563,
    "Compressed Bistot": 62564,
    "Compressed Triclinic Bistot": 62565,
    "Compressed Monoclinic Bistot": 62566,
    "Compressed Cubic Bistot": 62567,
    "Compressed Bezdnacine": 62576,
    "Compressed Abyssal Bezdnacine": 62577,
    "Compressed Hadal Bezdnacine": 62578,
    "Compressed Arkonor": 62568,
    "Compressed Crimson Arkonor": 62569,
    "Compressed Flawless Arkonor": 62571,
    "Compressed Prime Arkonor": 62570,
}

price_dict = {}
for item in minerals:
    jita_order_list = []
    url = f"https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=sell&page=1&type_id={minerals[item]}"
    req = requests.get(url)
    orders = req.json()
    for order in orders:
        if order["location_id"] == 60003760:
            jita_order_list.append(order)
    price = [x['price'] for x in jita_order_list]
    price_dict[item] = min(price)
#print(price_dict)
ore_dict = {}
for item in ore_ids:
    jita_order_list = []
    url = f"https://esi.evetech.net/latest/markets/10000002/orders/?datasource=tranquility&order_type=sell&page=1&type_id={ore_ids[item]}"
    req = requests.get(url)
    orders = req.json()
    try:
        for order in orders:
            if order["location_id"] == 60003760:
                jita_order_list.append(order)
    
        price = [x['price'] for x in jita_order_list]
        min_price = min(price)
        volume = []
        for order in orders:
            if order['price'] <= min_price*1.05:
                volume.append(order['volume_remain'])
        sum_volume = sum(volume)
        ore_dict[item] = {"Price": min_price, "Volume":sum_volume}
    except:
        continue
#print(ore_dict)

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
print(reprocessing_yield)
#brokers and taxes
broker_fee = .015
sales_tax = .036

for rock in ore:
    #print(rock)
    if rock in ore_dict:
        total_mineral_value = []
        ore_value = ore_dict[rock]["Price"]
        #print(f"Ore cost: {ore_value}")
        for mineral in ore[rock]:
            #print(f"{mineral}:{price_dict[mineral]}")
            mineral_price = price_dict[mineral]
            mineral_value = mineral_price * ore[rock][mineral] * reprocessing_yield
            total_mineral_value.append(mineral_value /100)
        #print(sum(total_mineral_value))
        #profit = (ore_dict[rock]["Volume"]) * ((sum(total_mineral_value) - (sum(total_mineral_value) * broker_fee) - (sum(total_mineral_value) * sales_tax)) - (ore_value * ore_dict[rock]["Volume"]))
        profit = (sum(total_mineral_value) *ore_dict[rock]["Volume"])  - (ore_dict[rock]["Volume"] * ore_dict[rock]["Price"]) 
        #print(f"Profit {profit}")
    
        if profit > 0:
            print('Ore to purchase: ' + rock)
            print('Volume to purchase: ' + '{:,.0f}'.format(ore_dict[rock]["Volume"]))
            print('Max purchase price: $' + '{:,.2f}'.format(ore_dict[rock]["Price"]))
            print('Total cost: $' + '{:,.2f}'.format(ore_dict[rock]["Volume"] * ore_dict[rock]["Price"]))
            print("Total Mineral Value: $" + '{:,.2f}'.format(sum(total_mineral_value) * (ore_dict[rock]["Volume"])))
            print("Profit: $" + '{:,.2f}'.format(profit))
            print('------------------------------')

print(price_dict)
