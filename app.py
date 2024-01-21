
from slack_sdk import WebClient
from os import getenv
from api_client import VanguardApiClient, Etfs

SLACK_TOKEN = getenv("SLACK_API_TOKEN")
SLACK_CHANNEL_NAME = getenv("SLACK_CHANNEL_NAME")
BASE_URL = getenv("BASE_URL")
api_client = VanguardApiClient(BASE_URL)
slack_client = WebClient(token=SLACK_TOKEN)

data = api_client.get_premium_discount(Etfs.VT)
today_pd_details = data['pdDetails'][-1]

today_pd = today_pd_details['marketPrice'] - today_pd_details['nav']
today_pd_formatted = "${:,.2f}".format(today_pd)

if today_pd > 0:
    message = f"VT is trading at a premium of {today_pd_formatted}"
else:
    message = f"VT is trading at a discount of {today_pd_formatted}"
    slack_client.chat_postMessage(
        channel=SLACK_CHANNEL_NAME,
        text=message
    )
