import time
from threading import Thread

from Temp_Telegram import Telegram
from Temp_Binance import Binance
from Temt_Utils import API_keys
from Models import Orders, Tickers

orders = Orders()
tickers = Tickers()

def telegram_msg_thandler(self, basecurrence, quotecurrence, buy, target):
	symbol = quotecurrence + basecurrence
	order = orders.ordersBuy.get(symbol)
	if not order:
		self.quantity = 10.0 / buy
		orders.ordersBuy[symbol] = orders.newOrder(symbol, buy, self.quantity, target)
		orders.saveOrder(orders.ordersBuy[symbol])

def binance_ticker_thandler(self, msg):
	for ticker in msg:
		symbol = ticker['s']
		ask = ticker['a']
		bid = ticker['b']

		order = orders.ordersBuy.get(symbol)
		if order:
			if ask > order.


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

