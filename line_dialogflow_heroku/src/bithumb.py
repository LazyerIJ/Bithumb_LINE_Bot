import urllib.request
import json

URL = 'https://api.bithumb.com/public/ticker/all'

def get_coin_price(coin):
    res = urllib.request.urlopen(URL)
    res_read = res.read().decode('utf-8')
    ticker = json.loads(res_read)
    return ticker['data'][coin]['closing_price']
