import urllib.request
import json

URL = 'https://api.bithumb.com/public/ticker/all'
COIN_DICT = {'WAVES': ['WAVES', 'waves', '웨이브'],
             'BTC': ['BTC', 'btc', '비트코인'],
             'EOS': ['EOS', 'eos', '이오스']}


def find_coin_in_message(message):
    for key, items in COIN_DICT.items():
        for item in items:
            if item in message:
                return key
    return None


def get_coin(coin):
    res = urllib.request.urlopen(URL)
    res_read = res.read().decode('utf-8')
    ticker = json.loads(res_read)
    return ticker['data'][coin]['closing_price']
