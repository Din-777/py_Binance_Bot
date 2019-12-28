from collections import namedtuple
import csv


class Orders(object):

	def __init__(self):
		self.order = namedtuple('Order', 'symbol price')
		self.ordersBuy = {}
		self.ordersSell = {}
		pass

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
