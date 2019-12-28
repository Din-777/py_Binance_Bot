from Models import Orders

orders = Orders()

orders.ordersBuy['USDBTC'] = orders.order('USDBTC', 300.0)
orders.ordersBuy['btcusd'] = orders.order('btcusd', 100.0)
orders.ordersBuy['btceth'] = orders.order('btceth', 200.0)

print(orders.ordersBuy.items())

msg = {0: {'s': 'USDBTC'} }

symbol = 'ETHCVC'

print('load')
orders.loadOrders()

d = orders.ordersBuy.get(symbol)

if orders.ordersBuy.get('ETHCVC'):
	print('Order BUY ' + symbol)

print('clear')
orders.ordersBuy.clear()


print(orders.ordersBuy.items())
