from src.message.parse import find_coin_in_message
from src.scrapy.get_price import get_coin


AVAL_REPLY_FORMAT = '{}의 가격은 {}입니다'
DISAVL_REPLY_FORMAT = '아쉽지만 대답하기 어려운 질문이네요.. [웨이브, 비트코인, 이오스]의 가격만 알 수 있어요'


def reply(message):
    coin = find_coin_in_message(message)
    if coin:
        price = get_coin(coin)
        return AVAL_REPLY_FORMAT.format(coin, price)
    return DISAVL_REPLY_FORMAT
