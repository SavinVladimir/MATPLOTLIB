import pandas as pd
import mplfinance as mpf

data = pd.read_csv('../AAPL.csv')


def Date():
    global data
    data.Date = pd.to_datetime(data.Date)
    data = data.set_index('Date')


Date()

mpf.plot(data)