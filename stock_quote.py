import requests
import time

ticker = "MSFT"
api_key = "146a407827e04b31afc509d21a7fe387"

def get_stpcl_price(ticker_symbol, api):
    url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
