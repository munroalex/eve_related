import pandas as pd
from esipy import EsiApp
from esipy import EsiClient
from esipy import EsiSecurity


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

df = pd.read_csv("prices.csv", index_col=0)


for index, row in df.iterrows():
    df["Margin"][index] = df["Amarr_Price"][index] - df["Jita_Price"][index]
    df["Percent"][index] = (df["Margin"][index] / df["Amarr_Price"][index]) * 100


for index, row in (
    df.sort_values(["ISK_Volume"], ascending=False).head(10000).iterrows()
):
    if df["Margin"][index] > 500000:
        if df["Percent"][index] > 20:
            if df["ISK_Volume"][index] > 10000000:
                item_name = app.op["get_universe_types_type_id"](type_id=index)
                item = client.request(item_name)
                df["Name"][index] = item.data["name"]
                print(df["Name"][index])

df.dropna()

print(df)
df.to_csv("finished.csv", index=True)
