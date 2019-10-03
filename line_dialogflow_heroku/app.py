from flask import Flask, request, abort, jsonify
import os ,json, threading
from src.message import get_reply

app = Flask(__name__)
token = json.load((open('token.json')))

@app.route("/callback", methods=['POST'])
def callback():
    # get request body as text
    req = request.get_json(silent=True, force=True)
    # handle webhook body
    try:
        parameter = req['queryResult']['parameters']
        coin = parameter['CoinType']
        asktype = parameter['AskType'] if parameter['AskType'] else 'PRICE'
        fulfillmentText = get_reply(coin, asktype)
    except:
        fulfillmentText = 'Server is sleeping now. Sorry'
        abort(400)
    reply = {
        "fulfillmentText": fulfillmentText
    }
    return jsonify(reply)


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
