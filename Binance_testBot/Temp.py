
from collections import namedtuple, OrderedDict

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


import pandas as pd
messages = client.get_messages(username, limit=100)

df = pd.DataFrame({})
for m in messages:
    mSplit = m.message.split('\n')
    if mSplit[0].find('BINANCE')!=-1:
        if mSplit[1][:3] == 'BUY':
            symbol = mSplit[0].split(' ')[0][1:]
            s = symbol.split('_')
            basecurrence = s[0]
            quotecurrence = s[1]
            buy = float(mSplit[1][6:])
            target = float(mSplit[2].split(' ')[1])
            df.append(pd.Series({'side':'BUY', 'symbol':symbol, 'buyPrice':buy, 'target':target}))

        #if mSplit[1][:5] == 'CLOSE':
        #    symbol = mSplit[0].split(' ')[0][1:]
        #    s = symbol.split('_')
        #    basecurrence = s[0]
        #    quotecurrence = s[1]
        #    close = float(mSplit[1][12:])
        #    profit = float(mSplit[2][12:16])
        #    df[m.date] = pd.Series({'side':'CLOSE', 'symbol':symbol, 'closePrice':close, 'profit':profit})


print(df)

import pickle
with open('..\CQS_10000msg_301219.pickle', 'wb') as f:
    pickle.dump(msg, f)

with open('..\CQS_10000msg_301219.pickle', 'rb') as f:
    data_new = pickle.load(f)


print('saf')
