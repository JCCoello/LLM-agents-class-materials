# filename: asset_analysis.py
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Define the date range
end_date = datetime(2026, 1, 15)
start_date = end_date - timedelta(weeks=5*52)  # 5 years ago

# Fetch data for NVDA and BTC-USD using yfinance
nvda_data = yf.download('NVDA', start=start_date, end=end_date)
btc_data = yf.download('BTC-USD', start=start_date, end=end_date)

# Check column names and normalize the prices accordingly
nvda_close_col = 'Adj Close' if 'Adj Close' in nvda_data.columns else 'Close'
btc_close_col = 'Adj Close' if 'Adj Close' in btc_data.columns else 'Close'

nvda_norm = nvda_data[nvda_close_col] / nvda_data[nvda_close_col].iloc[0]
btc_norm = btc_data[btc_close_col] / btc_data[btc_close_col].iloc[0]

# Calculate 60 weeks (approximately 300 trading days) moving average
nvda_ma60 = nvda_norm.rolling(window=300).mean()
btc_ma60 = btc_norm.rolling(window=300).mean()

# Print normalized prices
print("Normalized NVDA prices:\n", nvda_norm.head())
print("Normalized BTC-USD prices:\n", btc_norm.head())

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