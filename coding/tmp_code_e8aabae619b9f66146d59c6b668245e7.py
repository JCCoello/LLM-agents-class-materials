import pandas_datareader.data as web
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Define the date range
end_date = datetime(2026, 1, 15)
start_date = end_date - timedelta(weeks=5*52)  # 5 years ago

# Fetch data for NVDA and BTC-USD
nvda_data = web.DataReader('NVDA', 'yahoo', start_date, end_date)
btc_data = web.DataReader('BTC-USD', 'yahoo', start_date, end_date)

# Normalize the prices
nvda_norm = nvda_data['Adj Close'] / nvda_data['Adj Close'].iloc[0]
btc_norm = btc_data['Adj Close'] / btc_data['Adj Close'].iloc[0]

# Calculate 60 weeks moving average
nvda_ma60 = nvda_norm.rolling(window=60 * 5).mean()  # Approximating 60 weeks
btc_ma60 = btc_norm.rolling(window=60 * 5).mean()

# Print normalized prices
print("Normalized NVDA prices:\n", nvda_norm)
print("Normalized BTC-USD prices:\n", btc_norm)

# Plotting
plt.figure(figsize=(14, 7))
plt.plot(nvda_norm.index, nvda_norm, label='NVDA Normalized Price')
plt.plot(btc_norm.index, btc_norm, label='BTC-USD Normalized Price')
plt.plot(nvda_ma60.index, nvda_ma60, label='NVDA 60-week MA', linestyle='--')
plt.plot(btc_ma60.index, btc_ma60, label='BTC-USD 60-week MA', linestyle='--')

plt.title('Normalized Price of NVDA and BTC-USD with 60 Weeks Moving Average')
plt.xlabel('Date')
plt.ylabel('Normalized Price')
plt.legend()
plt.grid(True)

# Save the plot
plt.savefig('asset_analysis.png')

# Show the plot
plt.show()