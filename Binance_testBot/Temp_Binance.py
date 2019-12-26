from binance.client import Client
from Temt_Utils import API_keys

keys = API_keys("../keys.txt")
client = Client(keys.binance_apiKey, keys.binance_api_secret)

from binance.websockets import BinanceSocketManager
bm = BinanceSocketManager(client)
bm.start_ticker_socket(process_message)
bm.start()


# start aggregated trade websocket for BNBBTC
def process_message(msg):
    print("message type: {}  message time: {}\n".format(msg[0]['e'], msg[0]['E']))