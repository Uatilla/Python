import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf

#1. Get the data
df = pd.read_csv('./data/apple.csv')
print(df.head())

#2. Convert the date column from text to date to number
df['Date'] = pd.to_datetime(df['Date'])
#df['Date'] = df['Date'].apply(mdates.date2num)

# 3. Set Date as index
df.set_index('Date', inplace=True)

#3. Get only the data that matters to the new table
candle_data = df[['Open', 'High', 'Low', 'Close']]
print(candle_data.head())

## 4. Plot using mplfinance
mpf.plot(candle_data, type='candle', style='charles', title='Candlestick Chart for AAPL', ylabel='Value($)', xlabel = 'Date')
plt.show()