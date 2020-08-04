import json
from binance.client import Client, date_to_milliseconds, interval_to_milliseconds
import pandas as pd

client = Client("", "")

symbol = "ADAUSDT"
start  = "1 August, 2020"
end    = "4 August, 2020"
interval = Client.KLINE_INTERVAL_5MINUTE

klines = client.get_historical_klines(symbol, interval, start, end)

df = pd.DataFrame(klines, columns=['OpenTime', 'Open', 'High', 'Low', 'Close', 'Volume', 'CloseTime', 'QuoteAssetVolume', 'NumberTrades', 'BaseVolume', 'QuoteVolume', 'Ignored'])
df['OpenTime'] = pd.to_datetime(df['OpenTime'], unit='ms')

df.to_csv("../binance_{}_{}_{}-{}.csv".format(symbol, interval, start, end))

df = pd.read_csv("../binance_{}_{}_{}-{}.csv".format(symbol, interval, start, end))
df = df[['OpenTime', 'Open', 'High', 'Low', 'Close', 'Volume', 'CloseTime', 'QuoteAssetVolume', 'NumberTrades', 'BaseVolume', 'QuoteVolume']]

print(df)

print('OK')