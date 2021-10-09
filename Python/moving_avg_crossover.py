# Visualizing the Moving Average Crossover algorithm on a stock data.
# Using the stock data of Apple to plot buy and sell signal markers on moving averages.

# You can view the output and the Interactive plots on this link - https://nbviewer.org/github/aditya172926/Bots/blob/7c3291d16e2f923357823bfb53f7f68da72d6dc0/moving_avg_crossover.ipynb

# Resources: 
# 1) Moving Average Crossover - https://www.investopedia.com/articles/active-trading/052014/how-use-moving-average-buy-stocks.asp
# 2) Rolling Window - https://towardsdatascience.com/dont-miss-out-on-rolling-window-functions-in-pandas-850b817131db
# 3) Apple Stock data - https://drive.google.com/file/d/1_HaGnq_R-AvC3CUH1thY_GjkMCcgTnHf/view?usp=sharing


import pandas as pd
import matplotlib.pyplot as plt
# Using plotly for interactive graphs
import plotly.express as px
import plotly.graph_objects as go

# reading the data
aapl = pd.read_csv('data/aapl.csv')
print(aapl.head())

# Initialize the short (40 days) and long (100 days) windows for 2 different line plots
short_window = 40
long_window = 100

#Initialize the 'signals' DataFrame with the 'signal' column
signals = pd.DataFrame(index=aapl.index)
signals['signal'] = 0.0

# Create short simple moving average over the short window with the rolling()
signals['short_mavg'] = aapl['Close'].rolling(window=short_window, min_periods=1, center=False).mean()

# Create long simple moving average over the long window
signals['long_mavg'] = aapl['Close'].rolling(window=long_window, min_periods=1, center=False).mean()

# Create Signals 1 or 0 if short_mavg value goes above long_mavg for time period of short_window
signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)

# Generate trading orders
signals['positions'] = signals['signal'].diff()

print(signals)

######## Static plot using Matplotlib 

fig = plt.figure()

# Add subplot and label for y-axis
ax1 = fig.add_subplot(111, ylabel='Price is $')

# Plot the closing price
aapl['Close'].plot(ax=ax1, color='r', lw=2.)

# Plot the short and long moving averages
signals[['short_mavg', 'long_mavg']].plot(ax=ax1, lw=2.)

# Plot the buy signals
ax1.plot(signals.loc[signals.positions == 1.0].index, signals.short_mavg[signals.positions == 1.0], 
        '^', markersize=10, color='g')

# Plot the sell signals
ax1.plot(signals.loc[signals.positions == -1.0].index, signals.short_mavg[signals.positions == -1.0], 
        'v', markersize=10, color='k')

plt.show()

######## Interactive Plot using Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=aapl.index, y=aapl['Close'], mode='lines', name='lines'))
fig.add_trace(go.Scatter(x=signals.index, y = signals['short_mavg'], mode='lines', name=str(short_window)))
fig.add_trace(go.Scatter(x=signals.index, y = signals['long_mavg'], mode='lines', name=str(long_window)))

# Plotting the BUY signals with an arrow-up symbol
fig.add_trace(go.Scatter(mode = 'markers', x = signals.loc[signals.positions == 1.0].index, y = signals.short_mavg[signals.positions == 1.0], 
                        name='Buy', 
                        marker_symbol = 'triangle-up',
                        marker = dict(color='green', size=10)
                        ))

# Plotting the SELL signals with an arrow-down symbol
fig.add_trace(go.Scatter(mode = 'markers', x = signals.loc[signals.positions == -1.0].index, y = signals.short_mavg[signals.positions == -1.0], 
                        name='Sell',
                        marker_symbol='triangle-down',
                        marker = dict(color='red', size=10)
                        ))
