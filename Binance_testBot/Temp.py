
from collections import namedtuple

Order = namedtuple('Order', 'symbol price')

order1 = Order('usdtbtc', 100.0)
order2 = Order('usdteth', 200.0)
order3 = Order('usdtbnb', 300.0)

orders = [order1, order2, order3]

from telethon import TelegramClient, sync
from Temt_Utils import API_keys

keys = API_keys("../keys.txt")
client = TelegramClient('session_name', keys.tl_id, keys.tl_sec)
client.start()

username = 'CQSScalpingFree'
dp = client.get_entity(username)

messages = client.get_messages(username, limit=10000)

msg = {}
for m in messages:
    msg[m.date] = m.message

import pickle
with open('..\CQS_10000msg_301219.pickle', 'wb') as f:
    pickle.dump(msg, f)

with open('..\CQS_10000msg_301219.pickle', 'rb') as f:
    data_new = pickle.load(f)


print('saf')
