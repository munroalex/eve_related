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

op = app.op['get_characters_character_id_wallet'](
    character_id=api_info['sub'].split(':')[-1]
)
wallet = client.request(op)

# and to see the data behind, let's print it
print(wallet.data)

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


get_corp_name = app.op[''get_corporations_corporation_id'](
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
get_alliance_id = app.op['get_corporations_corporation_id_alliancehistory'](
    corporation_id='The Corp Id from the previous request'
)
alliance_history = client.request(get_alliance_id)

# this should give a list of dictionaries including corp IDs
print(alliance_history.data)


get_alliance_name = app.op[''get_alliances_alliance_id'](
    alliance_id='The alliance Id from the previous request'
)
alliance_deets = client.request(get_alliance_name)

# this should give a dictionary with all details of the corporation
print(alliance_deets.data)
                       
alliance_icon = app.op['get_alliances_alliance_id_icons'](
    corporation_id = 'The alliance Id from the previous request'
)
alliance_logo = client.request(alliance_icon)
# this will return a dictionary of links to different sized corp logos
print(alliance_logo.data)
                       
                       
