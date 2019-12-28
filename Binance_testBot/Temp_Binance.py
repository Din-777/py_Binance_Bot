from binance.client import Client
from binance.websockets import BinanceSocketManager

from Temt_Utils import API_keys

class Binance(object):
	
	def process_message(self, msg):
		self.even_thandler(self, msg)

	def __init__(self, apiKey, api_secret, even_thandler):
		self.client = Client(apiKey, api_secret)
		self.balances = self.client.get_account()['balances']

		self.even_thandler = even_thandler

		bm = BinanceSocketManager(self.client)
		bm.start_ticker_socket(self.process_message)
		bm.start()

