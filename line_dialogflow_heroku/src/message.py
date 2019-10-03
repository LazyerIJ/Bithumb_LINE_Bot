from src.bithumb import get_coin_price
from src.news import get_news, titles_to_str, add_ref_site
import datetime
import os

AVAL_REPLY_DT_FORMAT = '[*]%Y.%m.%d %H:%M'
AVAL_REPLY_FORMAT = '\n{}: {}'
SEOUL_TIMEDELTA = 9


def get_dt():
    now = datetime.datetime.now()
    now += datetime.timedelta(hours=SEOUL_TIMEDELTA)
    return now


def make_reply(cur_dt, coin, price):
    str1 = cur_dt.strftime(AVAL_REPLY_DT_FORMAT)
    str2 = AVAL_REPLY_FORMAT.format(coin, price)
    rs = str1 + str2
    return rs

def get_reply(coin, asktype):
    cur_dt = get_dt()
    if asktype == 'PRICE':
        if coin:
            price = get_coin_price(coin)
            return make_reply(cur_dt, coin, price)
        else:
            return '어떤 코인을 알려드릴까요?'
    else:
        titles = get_news(cur_dt)
        rs = titles_to_str(titles)
        rs = add_ref_site(rs)
        print('[*]{}'.format(rs))
        return rs 
