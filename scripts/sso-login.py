from esipy import EsiSecurity, EsiClient, EsiApp
from esipy.utils import generate_code_verifier
app = EsiApp().get_latest_swagger
# creating the security object using the app
security = EsiSecurity(
    redirect_uri='http://localhost:65432/callback/',
    client_id='YourClientIdHere',
    code_verifier=generate_code_verifier(),
)
#creating the client
client = EsiClient(
    retry_requests=True,
    headers={'User-Agent': 'Something CCP can use to contact you and that define your app'},
    security=security
)

# this will give you the url where your user must be redirected to.
print(security.get_auth_uri(state='SomeRandomGeneratedState', scopes=['esi-wallet.read_character_wallet.v1']))


tokens = security.auth('doWpId-stUirGHq7he5XOQ')
#view the tokens
print(tokens)

api_info = security.verify()
#view the api info
security.verify()
########################
###---Wallet---###
########################

wallet_balance = app.op['get_characters_character_id_wallet'](
    character_id=api_info['sub'].split(':')[-1]
)
wallet = client.request(wallet_balance)

# and to see the data behind, let's print it
print(wallet.data)


get_transactions = app.op['get_characters_character_id_wallet_transactions'](
    character_id=api_info['sub'].split(':')[-1]
)
transactions = client.request(get_transactions)
# this should give a set of dictionaries of individual transactions
print(transactions.data) 


get_journal = app.op['get_characters_character_id_wallet_journal'](
    character_id=api_info['sub'].split(':')[-1]
)
journal = client.request(get_journal)
# this should give a set of dictionaries of individual jounral entries
print(journal.data) 

########################
###---Portrait---###
########################

op = app.op['get_characters_character_id_portrait'](
    character_id=api_info['sub'].split(':')[-1]
)
portrait = client.request(op)

# this should give a dictionary of links to different size portraits
print(portrait.data)

########################
###---Corporation---###
########################

get_corp_id = app.op['get_characters_character_id_corporationhistory'](
    character_id=api_info['sub'].split(':')[-1]
)
corp_history = client.request(get_corp_id)

# this should give a list of dictionaries including corp IDs
print(corp_history.data)


get_corp_name = app.op['get_corporations_corporation_id'](
    corporation_id='The Corp Id from the previous request'
)
corp_deets = client.request(get_corp_name)

# this should give a dictionary with all details of the corporation
print(corp_deets.data)
                       
corp_icon = app.op['get_corporations_corporation_id_icons'](
    corporation_id = 'The Corp Id from the previous request'
)
logo = client.request(corp_icon)
# this will return a dictionary of links to different sized corp logos
print(logo.data)

########################
###---Alliance---###
########################
#Get alliance ID
get_alliance_id = app.op['get_corporations_corporation_id_alliancehistory'](
    corporation_id='The Corp Id from the previous request'
)
alliance_history = client.request(get_alliance_id)
# this should give a list of dictionaries including corp IDs
print(alliance_history.data)

                       
#get Alliance Name
get_alliance_name = app.op[''get_alliances_alliance_id'](
    alliance_id='The alliance Id from the previous request'
)
alliance_deets = client.request(get_alliance_name)
# this should give a dictionary with all details of the corporation
print(alliance_deets.data)
                           
                           
#Get alliance Logo                       
alliance_icon = app.op['get_alliances_alliance_id_icons'](
    corporation_id = 'The alliance Id from the previous request'
)
alliance_logo = client.request(alliance_icon)
# this will return a dictionary of links to different sized corp logos
print(alliance_logo.data)              
########################
###---Skills---###
########################
get_skill_points = app.op['get_characters_character_id_skills'](
    character_id=api_info['sub'].split(':')[-1]
)
skill_list = client.request(get_skill_points)
# this should give a dictionary of a list of dictionaries with individual skills and total sp including unallocated
print(skill_list.data)  
                           
get_skill_queue = app.op['get_characters_character_id_skillqueue'](
    character_id=api_info['sub'].split(':')[-1]
)
skill_queue = client.request(get_skill_queue)
# this should give a bunch of dictionaries including start and finish times for skill training
print(skill_queue.data)
                           
########################
###---Status---###
########################
op = app.op['status']()
status = client.request(op)
#returns a dictionary including player count 
print(status.data)

                           
                           
########################
###---Notifications---###
########################                           
get_notifications = app.op['get_characters_character_id_notifications'](
    character_id=api_info['sub'].split(':')[-1]
)
notifications = client.request(get_notifications)
# this should give a bunch of dictionaries of notifications
print(notifications.data)                           
                           
                           
########################
###---Location---###
########################                           
#get player location
get_player_location = app.op['get_characters_character_id_location'](
    character_id=api_info['sub'].split(':')[-1]
)
location = client.request(get_player_location)
# this should give a dictionary with solar system and station
print(location.data)
                           
#get ship type                           
get_ship = app.op['get_characters_character_id_ship'](
    character_id=api_info['sub'].split(':')[-1]
)
ship_type = client.request(get_ship)
# this should give a dictionary with ship item id, name and type id
print(ship_type.data)                           
                           
########################
###---Mail---###
########################
#get player mail ids
get_mail_ids = app.op['get_characters_character_id_mail'](
    character_id=api_info['sub'].split(':')[-1]
)
mail_ids = client.request(get_mail_ids)
# this should give a dictionary with solar system and station
print(mail_ids.data)                           
                           
#get return a single mail
get_mails = app.op['get_characters_character_id_mail_mail_id'](
    character_id=api_info['sub'].split(':')[-1],
    mail_id='get mail id from previous request'
)
mail_body = client.request(get_mails)
# this should give a dictionary with solar system and station
print(mail_body.data)                           
                           
                           
               
                           
                           
                           
                           
                           
