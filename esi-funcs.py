import random, string, base64, requests, datetime, os, json, time
from datetime import datetime, timedelta
import logging
from dotenv import load_dotenv

load_dotenv()


#setup for logging
logging.basicConfig(filename='info.log', encoding='utf-8', level=logging.DEBUG)
logging.info(f'Log start at {datetime.utcnow()}')

session = {}
# Create a non-guessable state to prevent CSRF
def create_state():
    logging.info(f'State created at {datetime.utcnow()}')
    state = str("".join(random.choices(string.ascii_uppercase + string.digits, k=30)))
    return state

# B64 encoding function for authenticated calls
def b64_encoding(client_id, secret_key):
    logging.info(f'B64 encoding created at {datetime.utcnow()}')
    auth_b64 = "%s:%s" % (client_id, secret_key)
    auth_b64 = base64.b64encode(auth_b64.encode("utf-8"))
    basic = auth_b64.decode("utf-8")
    return basic

my_id = os.getenv("CLIENT_ID")
my_secret_key = os.getenv("SECRET_KEY")
my_callback = os.getenv("CALLBACK")

def myEnvironment():
    print(f'My id is: {my_id}.')
    print(f'My secret key is: {my_secret_key}.')



def add_character():
    session["state"] = create_state()
    eve_login_base_url = f"https://login.eveonline.com/v2/oauth/authorize?response_type=code&redirect_uri={my_callback}&client_id={my_id}&scope=publicData+esi-mail.send_mail.v1+esi-contracts.read_character_contracts.v1+esi-contracts.read_corporation_contracts.v1+&state={session['state']}"

    print(eve_login_base_url)

def token_func(code):
    eve_online_token_url = "https://login.eveonline.com/v2/oauth/token"
    basic = b64_encoding(my_id, my_secret_key)
    tokens = requests.post(
        f"{eve_online_token_url}",
        headers={
            "Authorization": f"Basic {basic}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={"grant_type": "authorization_code", "code": code},
    )
    tokens = tokens.text
    #return tokens["refresh_token"]
    print(tokens)

refresh_token = os.getenv("REFRESH_TOKEN")

def refresh_eve_token(refresh_token):
    logging.info(f'Refreshing token  at {datetime.utcnow()}.')
    eve_online_token_url = "https://login.eveonline.com/v2/oauth/token"
    b64encode = b64_encoding(my_id, my_secret_key)
    refresh_tokens = requests.post(
        f"{eve_online_token_url}",
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "login.eveonline.com",
            "Authorization": f"Basic {b64encode}",
        },
        data={"grant_type": "refresh_token", "refresh_token": refresh_token},
    )
    if refresh_tokens.status_code == 200:
        refreshed_tokens = refresh_tokens.text
        refreshed_tokens = json.loads(refreshed_tokens)
        return refreshed_tokens["access_token"]
    else:
        logging.info(f'Refreshing failed at {datetime.utcnow()}.')

def get_contracts():
    req = requests.get(
        "https://esi.evetech.net/latest/corporations/98555434/contracts/?datasource=tranquility&page=1", headers={"Authorization": "Bearer " + refresh_eve_token(refresh_token)},
    )
    logging.info(f"Status code {req.status_code}")
    if req.status_code == 200:
        print(req.json())
        for contract in req.json():
            print(contract["contract_id"])
            get_contract_items(contract["contract_id"])

def get_contract_items(contract_id):
    req = requests.get(f"https://esi.evetech.net/latest/corporations/98555434/contracts/{contract_id}/items/?datasource=tranquility&page=1", headers={"Authorization": "Bearer " + refresh_eve_token(refresh_token)},
    )
    logging.info(f"Status code {req.status_code}")
    if req.status_code == 200:
        print(len(req.json()))
        for item in req.json():
            print(item["type_id"])
            #get_item_name(item["type_id"])

def get_item_name(type_id):
    req = requests.get(f"https://esi.evetech.net/latest/universe/types/{type_id}/?datasource=tranquility&language=en"
    )
    logging.info(f"Status code {req.status_code}")
    if req.status_code == 200:
        print(req.json())

if __name__ == "__main__":
    myEnvironment()
    #add_character()
    #code = input()
    #token_func(code)
    get_contracts()