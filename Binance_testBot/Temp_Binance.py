from binance.client import Client
from binance.websockets import BinanceSocketManager

from Temt_Utils import API_keys

keys = API_keys("../keys.txt")
client = Client(keys.binance_apiKey, keys.binance_api_secret)

balances = client.get_account()['balances']

def process_message(msg):
    print("message type: {}  message time: {}\n".format(msg[0]['e'], msg[0]['E']))


bm = BinanceSocketManager(client)
bm.start_ticker_socket(process_message)
bm.start()