
from collections import namedtuple

Order = namedtuple('Order', 'symbol price')

order1 = Order('usdtbtc', 100.0)
order2 = Order('usdteth', 200.0)
order3 = Order('usdtbnb', 300.0)

orders = [order1, order2, order3]

print(order1.symbol)
order1._replace(symbol='asdfg')
print(order1.symbol)

import win32api 
win32api.SetConsoleCtrlHandler(on_exit, True) 

print('saf')
