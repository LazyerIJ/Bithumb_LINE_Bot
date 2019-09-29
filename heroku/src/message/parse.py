coin_dict = {'WAVES': ['WAVES', 'waves', '웨이브'],
             'BTC': ['BTC', 'btc', '비트코인'],
             'EOS': ['EOS', 'eos', '이오스']}


def find_coin_in_message(message):
    for key, items in coin_dict.items():
        for item in items:
            if item in message:
                return key
    return None



