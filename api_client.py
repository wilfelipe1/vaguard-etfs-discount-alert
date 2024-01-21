import requests
from enum import Enum


class Etfs(Enum):
    VT = '3141'
    VTI = '0970'
    VOO = '0968'


class VanguardApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_premium_discount(self, etf: Etfs):
        url = f"{self.base_url}/{etf.value}/premium-discount/CURR"
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        return response.json()
