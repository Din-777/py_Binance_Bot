from collections import namedtuple

class Orders(object):

	def __init__(self):
		self.order = namedtuple('Order', 'symbol price')
		self.ordersBuy = {}
		self.ordersSell = {}
		pass
