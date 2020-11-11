import pandas as pd
import mplfinance as mpf

data = pd.read_csv('../AAPL.csv')


def Date():
    global data
    data.Date = pd.to_datetime(data.Date)
    data = data.set_index('Date')


Date()

mpf.plot(data['2020-09':'2020-10'], figratio=(22, 12), type='candle',
         mav=2, volume=True,title='AAPL', style='checkers')