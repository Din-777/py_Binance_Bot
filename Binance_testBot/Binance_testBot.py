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
	orders.ordersBuy[symbol] = orders.order(symbol, target)
	orders.saveOrder(orders.ordersBuy[symbol])
	print(orders)

def binance_ticker_thandler(self, msg):
	tickers.tickers.clear()
	for line in msg:
		#tickers.tickers[line['s']] = tickers.ticker(line['s'], float(line['a']), float(line['b']))
		symbol = line['s']
		ask = line['a']
		bid = line['b']

		if orders.ordersBuy.get(symbol):
			print('Order BUY ' + symbol)



	#print('Symbol {} Bid {} Ask {}'.format(msg[0]['s'], msg[0]['b'], msg[0]['a']))


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

