from collections import namedtuple
import csv


class Orders(object):

	def __init__(self):
		self.Order = namedtuple('Order', 'symbol originalBuyPrice originalTarget DCA1Buy DCA2Buy DCAAverage DCATarget quantity DCALivel')
		self.ordersBuy = {}
		self.ordersSell = {}
		pass

	def newOrder(self, symbol, originalBuyPrice, quantity):

		self.originalTarget = originalBuyPrice + ((originalBuyPrice / 100.0) * 1.5)
		self.DCA1Buy = originalBuyPrice - ((originalBuyPrice / 100.0) * 2.5)
		self.DCA2Buy = originalBuyPrice - ((originalBuyPrice / 100.0) * 5.0)
		self.DCALivel = 0
		self.DCAAverage = originalBuyPrice
		self.DCATarget = self.originalTarget

		self.order = Order(symbol, originalBuyPrice, originalTarget, DCA1Buy, DCA2Buy, DCAAverage, DCATarget, quantity, DCALivel)
		return self.order

	def saveOrders(self, filename = "../ordersBuy.csv"):
		with open(filename, 'w') as f:
			w = csv.writer(f, dialect = 'excel')
			#w.writerow(('symbol', 'symbol', 'price'))    # field header
			w.writerows([(name, data.symbol, data.price) for name, data in self.ordersBuy.items()])

	def saveOrder(self, order, filename = "../ordersBuy.csv"):
		with open(filename, 'a') as f:
			w = csv.writer(f, dialect = 'excel')
			w.writerow([order.symbol, order.symbol, order.price])

	def loadOrders(self, filename = "../ordersBuy.csv"):
		with open(filename, "r", newline="") as file:
			reader = csv.reader(file)
			for row in reader:
				if len(row) != 0:
					self.ordersBuy[row[0]] = self.order(row[1], float(row[2]))


class Tickers(object):

	def __init__(self):
		self.ticker = namedtuple('Ticker', 'symbol ask bid')
		self.tickers = {}
		pass
