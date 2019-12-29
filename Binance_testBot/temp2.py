
from collections import namedtuple
from Models import Orders, Tickers

orders = Orders()
orders.ordersBuy['LTCUSDT'] = orders.newOrder('LTCUSDT', 10, 5, 1)
orders.ordersBuy['LTCBTC'] = orders.newOrder('LTCBTC',  100, 50, 10)

orders.saveOrder(orders.ordersBuy['LTCUSDT'])
orders.saveOrder(orders.ordersBuy['LTCBTC'])

orders.ordersBuy.clear()
orders.loadOrders()

print('1')