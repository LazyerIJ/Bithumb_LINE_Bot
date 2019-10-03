from src.bithumb import get_coin_price
import datetime

AVAL_REPLY_DT_FORMAT = '[*]%Y.%m.%d %H:%M'
AVAL_REPLY_FORMAT = '\n{}: {}'

SEOUL_TIMEDELTA = 0

def get_dt():
    now = datetime.datetime.now()
    now += datetime.timedelta(hours=SEOUL_TIMEDELTA)
    return now.strftime(AVAL_REPLY_DT_FORMAT)


def make_reply(coin, price):
    str1 = '{}'.format(get_dt())
    str2 = AVAL_REPLY_FORMAT.format(coin, price)
    rs = str1 + str2
    return rs

def get_reply(coin, asktype):
    if asktype == 'PRICE':
        price = get_coin_price(coin)
        return make_reply(coin, price)
    else:
        return 'I can reply only about price yet. sorry.'
