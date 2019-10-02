from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import os ,json
from src.message import get_reply

app = Flask(__name__)

token = json.load(open('token.json'))
line_bot_api = LineBotApi(token['access'])  # Channel access token
handler = WebhookHandler(token['secret'])  # Channel secret


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)

    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print('[L]userId: {}'.format(event.source))
    print('[L]event.message: {}'.format(event.message))
    text = get_reply(event.message.text)

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text))


if __name__ == "__main__":
    port = None
    try:
        #hekoru
        port = int(os.getenv("PORT"))
    except:
        #local
        port = 5050
    app.run(host="0.0.0.0", port=port)
    #app.run()
