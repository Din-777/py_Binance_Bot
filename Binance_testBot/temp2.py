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

def binance_ticker_thandler(self, ticker):
	print(ticker)


keys = API_keys("../keys.txt")

tele = Telegram(keys.tl_id, keys.tl_sec, telegram_msg_thandler)
tele.start()
print('Telegram Run')

binance = Binance(keys.binance_apiKey, keys.binance_api_secret, binance_ticker_thandler) 
print('Binance Run')

while 1:
	pass

print('ads')
