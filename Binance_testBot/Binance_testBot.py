import time
from threading import Thread

from Temp_Telegram import Telegram
from Temp_Binance import Binance
from Temt_Utils import API_keys
from Models import Orders, Tickers

orders = Orders()
tickers = Tickers()

def telegram_msg_thandler(self, symbol, basecurrence, quotecurrence, target):
	symbol = quotecurrence + basecurrence
	orders.ordersBuy[symbol] = orders.newOrder(symbol=symbol, originalBuyPrice=10, quantity=10)
	orders.saveOrder(orders.ordersBuy[symbol])
	print(orders)

def binance_ticker_thandler(self, msg):
	for ticker in msg:
		symbol = ticker['s']
		ask = ticker['a']
		bid = ticker['b']

		order = orders.ordersBuy.get(symbol)
		if order:			
			print(order.price)
			print(order.price)


keys = API_keys("../keys.txt")

tele = Telegram(keys.tl_id, keys.tl_sec, telegram_msg_thandler)
tele.start()
while not tele.client._authorized:
	pass

print('Telegram Run')

orders.loadOrders()
print('Orders Load')

binance = Binance(keys.binance_apiKey, keys.binance_api_secret, binance_ticker_thandler) 
print('Binance Run')

print('Bot Run')

