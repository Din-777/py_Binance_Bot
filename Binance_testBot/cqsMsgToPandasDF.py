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


#df_Cqs = cqsMsgToDataFrame(cqsGet_Msg(limit=20))
#df_Cqs.to_csv('cqsData20000.csv', sep=';')
df_Cqs = pd.read_csv('cqsData20000.csv', sep=';')
print(df_Cqs, '\n')

#str.extract(r'([^,\.]*)[,\.]+(.*)', expand=True)
df_Cqs[['quit','base']] = df_Cqs.symbol.str.split('_').str
print(df_Cqs, '\n')

df_Cqs['closed'] = df_Cqs.duplicated(subset = 'id', keep = 0 )
print(df_Cqs, '\n')

dfClosed = df_Cqs[(df_Cqs.side =='close') & df_Cqs.closed == 1 ]
print(dfClosed, '\n')

dfOpen = df_Cqs[(df_Cqs.side =='buy') & (df_Cqs.closed == 0)]
print(dfOpen, '\n')

sumProfitClosed = dfClosed[dfClosed.side == 'close'].sum().drop(['side', 'id'])
print(sumProfitClosed)

print('\n', 'End')