
from collections import namedtuple
Order = namedtuple('Order', 'symbol originalBuyPrice originalTarget DCA1Buy DCA2Buy DCAAverage DCATarget quantity DCALivel')

def newOrder(symbol, originalBuyPrice, quantity):

	originalTarget = originalBuyPrice + ((originalBuyPrice / 100.0) * 1.5)
	DCA1Buy = originalBuyPrice - ((originalBuyPrice / 100.0) * 2.5)
	DCA2Buy = originalBuyPrice - ((originalBuyPrice / 100.0) * 5.0)
	DCALivel = 0
	DCAAverage = originalBuyPrice
	DCATarget = originalTarget

	order = Order(symbol, originalBuyPrice, originalTarget, DCA1Buy, DCA2Buy, DCAAverage, DCATarget, quantity, DCALivel)
	return order


order = newOrder('USDTBTC', 100.0, 10)

print('1')