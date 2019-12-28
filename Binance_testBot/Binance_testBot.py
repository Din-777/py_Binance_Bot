import time
from threading import Thread

from Temp_Telegram import Telegram
from Temt_Utils import API_keys
from Models import Orders
from Temp_Binance import Binance

orders = Orders()

def telegram_msg_thandler(self, symbol, basecurrence, quotecurrence, target):
	orders.ordersBuy[symbol] = orders.order(symbol, target)

	print(orders)

def binance_ticker_thandler(self, tickers):
	print('Symbol {} Bid {} Ask {}'.format(tickers[0]['s'], tickers[0]['b'], tickers[0]['a']))


keys = API_keys("../keys.txt")

tele = Telegram(keys.tl_id, keys.tl_sec, telegram_msg_thandler)
tele.start()
while not tele.client._authorized:
	pass

print('Telegram Run')

binance = Binance(keys.binance_apiKey, keys.binance_api_secret, binance_ticker_thandler) 
print('Binance Run')

print('Bot Run')

