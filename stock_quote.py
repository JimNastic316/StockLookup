import requests
# import time

ticker = "MSFT"
api_key = "146a407827e04b31afc509d21a7fe387"


def get_stock_price(ticker_symbol, api):
    url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    price = response['price'][:-3]
    return price


def get_stock_quote(ticker_symbol, api):
    url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    return response


stockdata = get_stock_quote(ticker, api_key)
stock_price = "$" + get_stock_price(ticker, api_key)

name = stockdata['name']
exchange = stockdata['exchange']
currency = stockdata['currency']
open_price = stockdata['open']
high_price = stockdata['high']
low_price = stockdata['low']
close_price = stockdata['close']
volume = stockdata['volume']



print(name, stock_price)
