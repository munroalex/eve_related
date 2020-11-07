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

# now get the wallet data
op = app.op['get_characters_character_id_wallet'](
    character_id=api_info['sub'].split(':')[-1]
)
wallet = client.request(op)

# and to see the data behind, let's print it
print(wallet.data)
