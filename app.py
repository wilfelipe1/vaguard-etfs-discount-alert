from os import getenv
from api_client import VanguardApiClient, Etfs

BASE_URL = getenv("BASE_URL")
api_client = VanguardApiClient(BASE_URL)

data = api_client.get_premium_discount(Etfs.VT)
today_pd_details = data['pdDetails'][-1]

today_pd = today_pd_details['marketPrice'] - today_pd_details['nav']

if today_pd > 0:
    print(f"VT is trading at a premium of {today_pd}")
else:
    print(f"VT is trading at a discount of {today_pd}")