type_ids = []
market_groups = app.op['get_markets_groups'](
)
group_ids = client.request(market_groups)

for group in group_ids.data:
    market_ids = app.op['get_markets_groups_market_group_id'](
        market_group_id=group
    )
    group = client.request(market_ids)
    group_ids = group.data['types']
    for id in group_ids:
        if id == None:
            pass
        else:
            type_ids.append(id)


types = np.array(type_ids)





df = pd.DataFrame(columns = ['AV_Price','AV_Volume', 'ISK_Volume'], index=types)

def average(lists):
    average = sum(lists)/len(lists)
    return average
    
    
#function for getting the minimum price of items in Jita
def get_history_jita_price(item):
    #get type_id of mineral input
    type_id = item
    print(type_id)


    #create request to swagger interface
    price_list = []
   
    volume_list = []

###Forge Region Request###
    market_history_operation = app.op['get_markets_region_id_history'](
        region_id=10000002,
        type_id=type_id,
    )
    res = client.head(market_history_operation)
    #if status 200 all good to go
    if res.status == 200:
        #make request
        response = client.request(market_history_operation, raw_body_only=True)
        response = json.loads(response.raw)
        month = response[-30:]
        for date in range(len(month)):
            price = month[date]["average"]
            
            volume = month[date]["volume"]
            price_list.append(price)
           
            volume_list.append(volume)
        try:
            df['AV_Price'][index] = average(price_list)    
            df['AV_Volume'][index] = average(volume_list)
        except:
            df['AV_Price'][index] = 0
            df['AV_Volume'][index] = 0
        df['ISK_Volume'][index] = df['AV_Price'][index] * df['AV_Volume'][index]

        print(df['ISK_Volume'][index])



for index, row in df.iterrows():
    get_history_jita_price(index)

df.to_csv('isk_volume.csv')

for index, row in df.sort_values(['ISK_Volume'], ascending=False).head(100).iterrows():
    if df['AV_Volume'][index] > 1000:
        top_items = app.op['get_universe_types_type_id'](
            type_id=index
            )
        top_item_types = client.request(top_items)
        print(top_item_types.data['name'])
