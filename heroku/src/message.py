from src.bithumb import find_coin_in_message, get_coin
from datetime import datetime

AVAL_REPLY_DT_FORMAT = '[*]%Y.%m.%d %H:%M'
AVAL_REPLY_FORMAT = '\n{}: {}'
DISAVL_REPLY_FORMAT = '아쉽지만 대답하기 어려운 질문이네요..\n[웨이브, 비트코인, 이오스]의 가격만 알 수 있어요'


def get_dt():
    now = datetime.now()
    return now.strftime(AVAL_REPLY_DT_FORMAT)


def make_reply(coin, price):
    str1 = '{}'.format(get_dt())
    str2 = AVAL_REPLY_FORMAT.format(coin, price)
    rs = str1 + str2
    return rs


def get_reply(message):
    coin = find_coin_in_message(message)
    if coin:
        price = get_coin(coin)
        return make_reply(coin, price)
    return DISAVL_REPLY_FORMAT
