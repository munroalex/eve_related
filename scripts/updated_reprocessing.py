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
type_ids = {"Veldspar":1230,"Concentrated Veldspar":17470,"Dense Veldspar":17471,"Stable Veldspar":46689,
            "Compressed Veldspar":28432,"Compressed Concentrated Veldspar":28430,"Compressed Dense Veldspar":28431,"Compressed Stable Veldspar":46705,
            "Scordite":1228,"Condensed Scordite":17463,"Massive Scordite":17464,"Glossy Scordite":46687,
            "Compressed Scordite":28429,"Compressed Condensed Scordite":28427,"Compressed Massive Scordite":28428,"Compressed Glossy Scordite":46703, 
            "Pyroxeres":1224,"Solid Pyroxeres":17459,"Viscous Pyroxeres":17460,"Opulent Pyroxeres":46686,
            "Compressed Pyroxeres":28424,"Compressed Solid Pyroxeres":28425,"Compressed Viscous Pyroxeres":28426,"Compressed Opulent Pyroxeres":46702, 
            "Plagioclase":18,"Azure Plagioclase":17455,"Rich Plagioclase":17456,"Sparkling Plagioclase":46685,
            "Compressed Plagioclase":28422,"Compressed Azure Plagioclase":28421,"Compressed Rich Plagioclase":28423,"Compressed Sparkling Plagioclase":46701, 
            "Omber":1227, "Silvery Omber":17867,"Golden Omber":17868,"Platinoid Omber":46684,
            "Compressed Omber":28416, "Compressed Silvery Omber":28417,"Compressed Golden Omber":28415,"Compressed Platinoid Omber":46700,
            "Kernite":20,"Luminous Kernite":17452,"Fiery Kernite":17453,"Resplendant Kernite":46683,
            "Compressed Kernite":28410,"Compressed Luminous Kernite":28411,"Compressed Fiery Kernite":28409,"Compressed Resplendant Kernite":46699,
            "Jaspet":1226,"Pure Jaspet":17448,"Pristine Jaspet":17449,"Immaculate Jaspet":46682, 
            "Compressed Jaspet":28406,"Compressed Pure Jaspet":28408,"Compressed Pristine Jaspet":28407,"Compressed Immaculate Jaspet":46698,
            "Hemorphite":1231,"Vivid Hemorphite":17444,"Radiant Hemorphite":17445,"Scintillating Hemorphite":46681,
            "Compressed Hemorphite":28403,"Compressed Vivid Hemorphite":28405,"Compressed Radiant Hemorphite":28404,"Compressed Scintillating Hemorphite":46697,
            "Hedbergite":21,"Vitric Hedbergite":17440,"Glazed Hedbergite":17441,"Lustrous Hedbergite":46680, 
            "Compressed Hedbergite":28401,"Compressed Vitric Hedbergite":28402,"Compressed Glazed Hedbergite":28400,"Compressed Lustrous Hedbergite":46696, 
            "Gneiss":1229, "Iridescent Gneiss":17865,"Prismatic Gneiss":17866,"Brilliant Gneiss":46679,
            "Compressed Gneiss":28397, "Compressed Iridescent Gneiss":28398,"Compressed Prismatic Gneiss":28399,"Compressed Brilliant Gneiss":46695,
            "Dark Ochre":1232,"Onyx Ochre":17436,"Obsidian Ochre":17437,"Jet Ochre":46675, 
            "Compressed Dark Ochre":28394,"Compressed Onyx Ochre":28396,"Compressed Obsidian Ochre":28395,"Compressed Jet Ochre":46694,
            "Crokite":1225,"Sharp Crokite":17432,"Crystalline Crokite":17433,"Pellucid Crokite":46677,
            "Compressed Crokite":28391,"Compressed Sharp Crokite":28393,"Compressed Crystalline Crokite":28392,"Compressed Pellucid Crokite":46693,
            "Bistot":1223,"Triclinic Bistot":17428,"Monoclinic Bistot":17429,"Cubic Bistot":46676, 
            "Compressed Bistot":28388,"Compressed Triclinic Bistot":28390,"Compressed Monoclinic Bistot":28389,"Compressed Cubic Bistot":46692, 
            "Arkonor":22,"Crimson Arkonor":17425,"Prime Arkonor":17426,"Flawless Arkonor":46678, 
            "Compressed Arkonor":28367,"Compressed Crimson Arkonor":28385,"Compressed Prime Arkonor":28387,"Compressed Flawless Arkonor":46691, 
            "Mercoxit":11396,"Magma Mercoxit":17869,"Vitreous Mercoxit":17870,
            "Compressed Mercoxit":28413,"Compressed Magma Mercoxit":28412,"Compressed Vitreous Mercoxit":28414,
            "Spodumain":19,"Bright Spodumain":17466,"Gleaming Spodumain":17467,"Dazzling Spodumain":46688, 
            "Compressed Spodumain":28420,"Compressed Bright Spodumain":28418,"Compressed Gleaming Spodumain":28419,"Compressed Dazzling Spodumain":46704, 
            "Bezdnacine":52316, "Rakovene":52315,"Talassonite":52306,
            "Tritanium":34,"Pyerite":35,"Mexallon":36,"Isogen":37,"Nocxium":38,"Zydrine":39,
           "Megacyte":40,"Morphite":11399}
#mineral content in reprocessed ores nested dictionary
reprocessed_ores = {"Veldspar": {"Tritanium":400},"Concentrated Veldspar": {"Tritanium":420},"Dense Veldspar": {"Tritanium":441},"Stable Veldspar": {"Tritanium":463},
                    "Compressed Veldspar": {"Tritanium":40000},"Compressed Concentrated Veldspar": {"Tritanium":42000},"Compressed Dense Veldspar": {"Tritanium":44100},"Compressed Stable Veldspar": {"Tritanium":46300},
                    "Scordite": {"Tritanium":150,"Pyerite":90},"Condensed Scordite": {"Tritanium":157,"Pyerite":94},"Massive Scordite": {"Tritanium":164,"Pyerite":98},"Glossy Scordite": {"Tritanium":172,"Pyerite":102},
                    "Compressed Scordite": {"Tritanium":15000,"Pyerite":9000},"Compressed Condensed Scordite": {"Tritanium":15700,"Pyerite":9400},"Compressed Massive Scordite": {"Tritanium":16400,"Pyerite":9800},"Compressed Glossy Scordite": {"Tritanium":17200,"Pyerite":10200},
                    "Pyroxeres": {"Pyerite":90,"Mexallon":30},"Solid Pyroxeres": {"Pyerite":94,"Mexallon":31},"Viscous Pyroxeres": {"Pyerite":98,"Mexallon":32},"Opulent Pyroxeres": {"Pyerite":102,"Mexallon":33},
                    "Compressed Pyroxeres": {"Pyerite":9000,"Mexallon":3000},"Compressed Solid Pyroxeres": {"Pyerite":9400,"Mexallon":3100},"Compressed Viscous Pyroxeres": {"Pyerite":9800,"Mexallon":3200},"Compressed Opulent Pyroxeres": {"Pyerite":10200,"Mexallon":3300},
                    "Plagioclase": {"Tritanium":175,"Mexallon":70},"Azure Plagioclase": {"Tritanium":183,"Mexallon":73},"Rich Plagioclase": {"Tritanium":192,"Mexallon":76},"Sparkling Plagioclase": {"Tritanium":201,"Mexallon":79},
                    "Compressed Plagioclase": {"Tritanium":17500,"Mexallon":7000},"Compressed Azure Plagioclase": {"Tritanium":18300,"Mexallon":7300},"Compressed Rich Plagioclase": {"Tritanium":19200,"Mexallon":7600},"Compressed Sparkling Plagioclase": {"Tritanium":20100,"Mexallon":7900},
                    "Omber": {"Pyerite":90,"Isogen":75},"Silvery Omber": {"Pyerite":94,"Isogen":78},"Golden Omber": {"Pyerite":98,"Isogen":81},"Platinoid Omber": {"Pyerite":102,"Isogen":85},
                    "Compressed Omber": {"Pyerite":9000,"Isogen":7500},"Compressed Silvery Omber": {"Pyerite":9400,"Isogen":7800},"Compressed Golden Omber": {"Pyerite":9800,"Isogen":8100},"Compressed Platinoid Omber": {"Pyerite":10200,"Isogen":8500},
                    "Kernite": {"Mexallon":60,"Isogen":120},"Luminous Kernite": {"Mexallon":63,"Isogen":126},"Fiery Kernite": {"Mexallon":66,"Isogen":132},"Resplendant Kernite": {"Mexallon":69,"Isogen":138},
                    "Compressed Kernite": {"Mexallon":6000,"Isogen":12000},"Compressed Luminous Kernite": {"Mexallon":6300,"Isogen":12600},"Compressed Fiery Kernite": {"Mexallon":6600,"Isogen":13200},"Compressed Resplendant Kernite": {"Mexallon":6900,"Isogen":13800},
                    "Jaspet": {"Mexallon":150,"Nocxium":50},"Pure Jaspet": {"Mexallon":157,"Nocxium":52},"Pristine Jaspet": {"Mexallon":164,"Nocxium":54},"Immaculate Jaspet": {"Mexallon":172,"Nocxium":56},
                    "Compressed Jaspet": {"Mexallon":15000,"Nocxium":5000},"Compressed Pure Jaspet": {"Mexallon":15700,"Nocxium":5200},"Compressed Pristine Jaspet": {"Mexallon":16400,"Nocxium":5400},"Compressed Immaculate Jaspet": {"Mexallon":17200,"Nocxium":5600},
                    "Hemorphite": {"Isogen":240,"Nocxium":90},"Vivid Hemorphite": {"Isogen":252,"Nocxium":94},"Radiant Hemorphite": {"Isogen":264,"Nocxium":98},"Scintillating Hemorphite": {"Isogen":277,"Nocxium":102},
                    "Compressed Hemorphite": {"Isogen":24000,"Nocxium":9000},"Compressed Vivid Hemorphite": {"Isogen":25200,"Nocxium":9400},"Compressed Radiant Hemorphite": {"Isogen":26400,"Nocxium":9800},"Compressed Scintillating Hemorphite": {"Isogen":27700,"Nocxium":10200},
                    "Hedbergite": {"Pyerite":450,"Nocxium":120},"Vitric Hedbergite": {"Pyerite":472,"Nocxium":126},"Glazed Hedbergite": {"Pyerite":495,"Nocxium":132},"Lustrous Hedbergite": {"Pyerite":519,"Nocxium":138},
                    "Compressed Hedbergite": {"Pyerite":45000,"Nocxium":12000},"Compressed Vitric Hedbergite": {"Pyerite":47200,"Nocxium":12600},"Compressed Glazed Hedbergite": {"Pyerite":49500,"Nocxium":13200},"Compressed Lustrous Hedbergite": {"Pyerite":51900,"Nocxium":13800},
                    "Gneiss": {"Pyerite":2000,"Mexallon":1500,"Isogen":800},"Iridescent Gneiss": {"Pyerite":2100,"Mexallon":1575,"Isogen":840},"Prismatic Gneiss": {"Pyerite":2205,"Mexallon":1653,"Isogen":882},"Brilliant Gneiss": {"Pyerite":2315,"Mexallon":1735,"Isogen":926},
                    "Compressed Gneiss": {"Pyerite":200000,"Mexallon":150000,"Isogen":80000},"Compressed Iridescent Gneiss": {"Pyerite":210000,"Mexallon":157500,"Isogen":84000},"Compressed Prismatic Gneiss": {"Pyerite":220500,"Mexallon":165300,"Isogen":88200},"Compressed Brilliant Gneiss": {"Pyerite":231500,"Mexallon":173500,"Isogen":92600},
                    "Dark Ochre": {"Mexallon":1360,"Isogen":1200,"Nocxium":320},"Onyx Ochre": {"Mexallon":1428,"Isogen":1260,"Nocxium":336},"Obsidian Ochre": {"Mexallon":1499,"Isogen":1323,"Nocxium":352},"Jet Ochre": {"Mexallon":1573,"Isogen":1389,"Nocxium":369},
                    "Compressed Dark Ochre": {"Mexallon":136000,"Isogen":120000,"Nocxium":32000},"Compressed Onyx Ochre": {"Mexallon":142800,"Isogen":126000,"Nocxium":33600},"Compressed Obsidian Ochre": {"Mexallon":149900,"Isogen":132300,"Nocxium":35200},"Compressed Jet Ochre": {"Mexallon":157300,"Isogen":138900,"Nocxium":36900},
                    "Crokite": {"Pyerite":800,"Mexallon":2000,"Nocxium":800},"Sharp Crokite": {"Pyerite":840,"Mexallon":2100,"Nocxium":840},"Crystalline Crokite": {"Pyerite":882,"Mexallon":2205,"Nocxium":882},"Pellucid Crokite": {"Pyerite":926,"Mexallon":2315,"Nocxium":926},
                    "Compressed Crokite": {"Pyerite":80000,"Mexallon":200000,"Nocxium":80000},"Compressed Sharp Crokite": {"Pyerite":84000,"Mexallon":210000,"Nocxium":84000},"Compressed Crystalline Crokite": {"Pyerite":88200,"Mexallon":220500,"Nocxium":88200},"Compressed Pellucid Crokite": {"Pyerite":92600,"Mexallon":231500,"Nocxium":92600},
                    "Bistot": {"Pyerite":3200,"Mexallon":1200,"Zydrine":160},"Triclinic Bistot": {"Pyerite":3360,"Mexallon":1260,"Zydrine":168},"Monoclinic Bistot": {"Pyerite":3528,"Mexallon":1323,"Zydrine":176},"Cubic Bistot": {"Pyerite":3704,"Mexallon":1389,"Zydrine":184},
                    "Compressed Bistot": {"Pyerite":320000,"Mexallon":120000,"Zydrine":16000},"Compressed Triclinic Bistot": {"Pyerite":336000,"Mexallon":126000,"Zydrine":16800},"Compressed Monoclinic Bistot": {"Pyerite":352800,"Mexallon":132300,"Zydrine":17600},"Compressed Cubic Bistot": {"Pyerite":370400,"Mexallon":138900,"Zydrine":18400},
                    "Arkonor": {"Pyerite":3200,"Mexallon":1200,"Megacyte":120},"Crimson Arkonor": {"Pyerite":3360,"Mexallon":1260,"Megacyte":126},"Prime Arkonor": {"Pyerite":3528,"Mexallon":1323,"Megacyte":132},"Flawless Arkonor": {"Pyerite":3704,"Mexallon":1389,"Megacyte":138},
                    "Compressed Arkonor": {"Pyerite":320000,"Mexallon":120000,"Megacyte":12000},"Compressed Crimson Arkonor": {"Pyerite":336000,"Mexallon":126000,"Megacyte":12600},"Compressed Prime Arkonor": {"Pyerite":352800,"Mexallon":132300,"Megacyte":13200},"Compressed Flawless Arkonor": {"Pyerite":370400,"Mexallon":138900,"Megacyte":13800},
                    "Mercoxit": {"Morphite":140},"Magma Mercoxit": {"Morphite":147},"Vitreous Mercoxit": {"Morphite":154},
                    "Compressed Mercoxit": {"Morphite":14000},"Compressed Magma Mercoxit": {"Morphite":14700},"Compressed Vitreous Mercoxit": {"Morphite":15400},
                    "Spodumain": {"Tritanium":48000,"Isogen":1000,"Nocxium":160,"Zydrine":80,"Megacyte":40},
                    "Bright Spodumain": {"Tritanium":50400,"Isogen":1050,"Nocxium":168,"Zydrine":84,"Megacyte":42},
                    "Gleaming Spodumain": {"Tritanium":52920,"Isogen":1102,"Nocxium":176,"Zydrine":88,"Megacyte":44},
                    "Dazzling Spodumain": {"Tritanium":55566,"Isogen":1157,"Nocxium":184,"Zydrine":92,"Megacyte":46},
                    "Compressed Spodumain": {"Tritanium":4800000,"Isogen":100000,"Nocxium":16000,"Zydrine":8000,"Megacyte":4000},
                    "Compressed Bright Spodumain": {"Tritanium":5040000,"Isogen":105000,"Nocxium":16800,"Zydrine":8400,"Megacyte":4200},
                    "Compressed Gleaming Spodumain": {"Tritanium":5292000,"Isogen":110200,"Nocxium":17600,"Zydrine":8800,"Megacyte":4400},
                    "Compressed Dazzling Spodumain": {"Tritanium":5556600,"Isogen":115700,"Nocxium":18400,"Zydrine":9200,"Megacyte":4600},
                    
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

#list of all ores to search
ore_list = ["Veldspar","Concentrated Veldspar","Dense Veldspar","Stable Veldspar",
            "Compressed Veldspar","Compressed Concentrated Veldspar","Compressed Dense Veldspar","Compressed Stable Veldspar",
            "Scordite","Condensed Scordite","Massive Scordite","Glossy Scordite",
            "Compressed Scordite","Compressed Condensed Scordite","Compressed Massive Scordite","Compressed Glossy Scordite", 
            "Pyroxeres","Solid Pyroxeres","Viscous Pyroxeres","Opulent Pyroxeres",
            "Compressed Pyroxeres","Compressed Solid Pyroxeres","Compressed Viscous Pyroxeres","Compressed Opulent Pyroxeres", 
            "Plagioclase","Azure Plagioclase","Rich Plagioclase","Sparkling Plagioclase",
            "Compressed Plagioclase","Compressed Azure Plagioclase","Compressed Rich Plagioclase","Compressed Sparkling Plagioclase", 
            "Omber", "Silvery Omber","Golden Omber","Platinoid Omber",
            "Compressed Omber", "Compressed Silvery Omber","Compressed Golden Omber","Compressed Platinoid Omber",
            "Kernite","Luminous Kernite","Fiery Kernite","Resplendant Kernite",
            "Compressed Kernite","Compressed Luminous Kernite","Compressed Fiery Kernite","Compressed Resplendant Kernite",
            "Jaspet","Pure Jaspet","Pristine Jaspet","Immaculate Jaspet", 
            "Compressed Jaspet","Compressed Pure Jaspet","Compressed Pristine Jaspet","Compressed Immaculate Jaspet",
            "Hemorphite","Vivid Hemorphite","Radiant Hemorphite","Scintillating Hemorphite",
            "Compressed Hemorphite","Compressed Vivid Hemorphite","Compressed Radiant Hemorphite","Compressed Scintillating Hemorphite",
            "Hedbergite","Vitric Hedbergite","Glazed Hedbergite","Lustrous Hedbergite", 
            "Compressed Hedbergite","Compressed Vitric Hedbergite","Compressed Glazed Hedbergite","Compressed Lustrous Hedbergite", 
            "Gneiss", "Iridescent Gneiss","Prismatic Gneiss","Brilliant Gneiss",
            "Compressed Gneiss", "Compressed Iridescent Gneiss","Compressed Prismatic Gneiss","Compressed Brilliant Gneiss",
            "Dark Ochre","Onyx Ochre","Obsidian Ochre","Jet Ochre", 
            "Compressed Dark Ochre","Compressed Onyx Ochre","Compressed Obsidian Ochre","Compressed Jet Ochre",
            "Crokite","Sharp Crokite","Crystalline Crokite","Pellucid Crokite",
            "Compressed Crokite","Compressed Sharp Crokite","Compressed Crystalline Crokite","Compressed Pellucid Crokite",
            "Bistot","Triclinic Bistot","Monoclinic Bistot","Cubic Bistot", 
            "Compressed Bistot","Compressed Triclinic Bistot","Compressed Monoclinic Bistot","Compressed Cubic Bistot", 
            "Arkonor","Crimson Arkonor","Prime Arkonor","Flawless Arkonor", 
            "Compressed Arkonor","Compressed Crimson Arkonor","Compressed Prime Arkonor","Compressed Flawless Arkonor", 
            "Mercoxit","Magma Mercoxit","Vitreous Mercoxit",
            "Compressed Mercoxit","Compressed Magma Mercoxit","Compressed Vitreous Mercoxit",
            "Spodumain","Bright Spodumain","Gleaming Spodumain","Dazzling Spodumain", 
            "Compressed Spodumain","Compressed Bright Spodumain","Compressed Gleaming Spodumain","Compressed Dazzling Spodumain", 
            "Bezdnacine", "Rakovene","Talassonite"]
#freighter capacity
charon_capacity = 465000

for ore in ore_list:
    try:
        total_mineral_value = []
        ore_value = price_list[ore]["Price"] * 100
        #total_mineral_mass = []
        for key in reprocessed_ores[ore]:
            mineral_price = price_list[key]["Price"]
            mineral_value = mineral_price * reprocessed_ores[ore][key] * reprocessing_yield
            #mineral_mass = reprocessed_ores[ore][key] * reprocessing_yield * volumes[key] * price_list[ore]["Volume"]
        
            #total_mineral_mass.append(mineral_mass)
            total_mineral_value.append(mineral_value)
        profit = (price_list[ore]["Volume"] / 100) * (sum(total_mineral_value) - ore_value)
        #trips = charon_capacity / sum(total_mineral_mass)
        if profit > 25000000:
            print(ore + " profit: $" + '{:,.2f}'.format(profit))
            #print(sum(total_mineral_mass))
            #print(math.ceil(trips))
    except:
        pass

