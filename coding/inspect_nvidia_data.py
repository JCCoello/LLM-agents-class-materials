# filename: inspect_nvidia_data.py

import yfinance as yf
import pandas as pd

# Define the ticker symbol for Nvidia
ticker = 'NVDA'

# Define the start and end dates
start_date = '2024-06-26'
end_date = '2024-07-26'

# Download data using yfinance
nvidia_data = yf.download(ticker, start=start_date, end=end_date)

# Display the DataFrame to verify its structure
print(nvidia_data.head())
print(nvidia_data.columns)
print(nvidia_data.dtypes)

# Resetting index could be useful in maintaining structure sanity
nvidia_data.reset_index()

# Assuming 'Close' column correct determination post-inspection
close_column = nvidia_data.columns.get_level_values(0)[-1] if len(nvidia_data.columns) > 1 else 'Close'

# Calculate percentage change in stock price over the month
start_price = nvidia_data[close_column].iloc[0]
end_price = nvidia_data[close_column].iloc[-1]
percentage_change = ((end_price - start_price) / start_price) * 100

# Identify the highest and lowest closing prices
highest_close = nvidia_data[close_column].max()
lowest_close = nvidia_data[close_column].min()

# Compute the average trading volume
average_volume = nvidia_data['Volume'].mean()

# Print the calculated metrics
print(f"Percentage Change in Stock Price: {percentage_change}%")
print(f"Highest Closing Price: ${highest_close}")
print(f"Lowest Closing Price: ${lowest_close}")
print(f"Average Trading Volume: {average_volume}")