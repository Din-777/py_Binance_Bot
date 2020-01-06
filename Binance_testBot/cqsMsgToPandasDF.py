from telethon import TelegramClient, sync
import pandas as pd

from Temp_Binance import Binance
from Temt_Utils import API_keys

def cqsGet_Msg(limit=20000):
    keys = API_keys("../keys.txt")
    client = TelegramClient('session_name', keys.tl_id, keys.tl_sec)
    client.start()

    msg = client.get_messages('CQSScalpingFree', limit=limit)
    return msg

def cqsMsgToDataFrame(messages):
    df = pd.DataFrame()
    for msg in messages:
        msgSplitLine = msg.message.split('\n')
        if msgSplitLine[0].find('BINANCE')!=-1:

            if msgSplitLine[1][:3] == 'BUY':
                symbol = msgSplitLine[0].split(' ')[0][1:]
                s = symbol.split('_')
                basecurrence = s[0]
                quotecurrence = s[1]
                buy = float(msgSplitLine[1][6:])
                target = float(msgSplitLine[2].split(' ')[1])
                id = int(msgSplitLine[3][3:])
                df = df.append([pd.Series([msg.date, 'buy', symbol, buy, target, id])] )
        
            if msgSplitLine[1][:10] == 'CLOSE LONG':
                symbol = msgSplitLine[0].split(' ')[0][1:]
                s = symbol.split('_')
                basecurrence = s[0]
                quotecurrence = s[1]
                close = float(msgSplitLine[1][12:])
                profit = float(msgSplitLine[2][12:16])
                id = int(msgSplitLine[3][3:])
                df = df.append([pd.Series([msg.date, 'close', symbol, close, profit, id])] )

    df.columns = ['date', 'side', 'symbol', 'price', 'target', 'id']    
    df['quot'] = df.symbol.str.split('_', 1).str[0]
    df['base'] = df.symbol.str.split('_', 1).str[1]
    df['closed'] = df.duplicated(subset = 'id', keep = 0 )
    df = df[['date','symbol', 'quot', 'base', 'side', 'price', 'target', 'closed', 'id']]
    df = df.drop(df[(df.side == 'close') & (df.closed == 0)].index)    
    df.index = pd.RangeIndex(len(df.index))

    return df

def getBinanceTickersDataFrame():
    keys = API_keys("../keys.txt")
    binance = Binance(keys.binance_apiKey, keys.binance_api_secret)
    prices = binance.client.get_ticker()

    df = pd.DataFrame(prices)

    df['base'] = df.symbol.str.extract(r'(.+(?=BTC$|USDT$|BNB$|ETH$))', expand=True)
    df['quot'] = df.symbol.str.extract(r'(BTC$|USDT$|BNB$|ETH$)', expand=True)

    return df


#dfTickers = getBinanceTickersDataFrame()
#dfTickers.to_csv('allTickers.csv', sep=';')

dfTickers = pd.read_csv('allTickers.csv', sep=';')
dfTickers = dfTickers[['symbol','base','quot','bidPrice','askPrice']]
print(dfTickers)

#df_Cqs = cqsMsgToDataFrame(cqsGet_Msg(limit=5000))
#df_Cqs.to_csv('cqsData20000.csv', index=0, sep=';')

df_Cqs = pd.read_csv('cqsData20000.csv', sep=';')

df_Cqs = df_Cqs.drop(df_Cqs[(df_Cqs.side == 'close') & (df_Cqs.closed == 0)].index)
print(df_Cqs, '\n')

df_Cqs.date = pd.to_datetime(df_Cqs['date'], format='%Y-%m-%d %H:%M:%S')

dfClosed = df_Cqs[(df_Cqs.side =='close') & (df_Cqs.closed == 1)]
#dfClosed['deltatime'] = 
#dfClosed = dfClosed.groupby(['quot']).size().reset_index(name='count').sort_values(['count'], ascending = 0)

dfClosed['profit_in_$'] = dfClosed.target / 10.0

print(dfClosed, '\n')
print(dfClosed['profit_in_$'].sum(), '\n')

dfOpen = df_Cqs[(df_Cqs.side =='buy') & (df_Cqs.closed == 0)]
print(dfOpen, '\n')

dfResult = pd.merge(dfOpen, dfTickers, how='inner', on=['quot', 'base'])
dfResult['profit_in_%'] = (100.0 / (dfResult.price / dfResult.bidPrice) ) - 100.0

dfResult['profit_in_$'] = dfResult['profit_in_%'] / 10.0
dfResult.to_csv('dfResult.csv', index=0, sep=';')

print(dfResult, '\n')
print(dfResult['profit_in_$'].sum(), '\n')

import matplotlib.pyplot as plt

new_sample_df = dfResult[ ['date', 'profit_in_$'] ]
new_sample_df.index = new_sample_df.date.dt.day
new_sample_df.plot(figsize=(12, 9))
plt.show()

print('\n', 'End')