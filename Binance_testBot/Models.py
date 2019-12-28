from collections import namedtuple

class Orders(object):

	def __init__(self):
		self.order = namedtuple('Order', 'symbol price')
		self.ordersBuy = {}
		self.ordersSell = {}
		pass

class Tickers(object):

	def __init__(self):
		self.ticker = namedtuple('Ticker', 'symbol bid ask')
		self.tickers = {}
		pass
