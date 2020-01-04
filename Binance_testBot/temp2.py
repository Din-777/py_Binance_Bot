
from collections import namedtuple
from Models import Orders, Tickers
import pandas as pd

df = pd.DataFrame([['close', 100, 0],
				   ['buy', 101, 1],
				   ['buy', 102, 2],
				   ['close', 1.5, 1],
				   ['buy', 103, 3],
				   ['buy', 104, 4],
				   ['close', 1.5, 4],
				   ['buy', 105, 5],
				   ['close', 1.5, 5]], columns=['side','target','id'])

df['closed'] = df.duplicated(subset = 'id', keep = 0 )
print(df, '\n')

dfClosed = df[df.closed == 1 ]
print(dfClosed, '\n')

dfOpen = df[(df.side =='buy') & (df.closed == 0)]
print(dfOpen, '\n')

sumProfitClosed = dfClosed[dfClosed.side == 'close'].sum().drop(['side', 'id'])
print(sumProfitClosed)

dfConsolidat

print('end')