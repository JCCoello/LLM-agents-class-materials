import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the ticker symbols and the period
tickers = ['NVDA', 'BTC-USD']
start_date = '2021-01-15'
end_date = '2026-01-15'

# Download historical data for the last 5 years
data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']

# Normalize the data
normalized_data = data / data.iloc[0]

# Calculate the 60 weeks moving average
moving_average_60w = normalized_data.rolling(window=60).mean()

# Print the normalized prices
print("Normalized Prices:")
print(normalized_data)

# Plotting
plt.figure(figsize=(14, 7))
plt.plot(normalized_data, label=['NVDA', 'BTC-USD'])
plt.plot(moving_average_60w, linestyle='--', label=['NVDA 60w MA', 'BTC-USD 60w MA'])

plt.title('Normalized Price of NVDA and BTC-USD with 60 Weeks Moving Average')
plt.xlabel('Date')
plt.ylabel('Normalized Price')
plt.legend()
plt.grid(True)

# Save and show the figure
plt.savefig('asset_analysis.png')
plt.show()