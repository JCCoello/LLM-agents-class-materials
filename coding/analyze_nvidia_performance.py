# filename: analyze_nvidia_performance.py

import yfinance as yf
import pandas as pd

# Define the ticker symbol for Nvidia
ticker = 'NVDA'

# Define the start and end dates
start_date = '2024-06-26'
end_date = '2024-07-26'

# Download data using yfinance
nvidia_data = yf.download(ticker, start=start_date, end=end_date)

# Print column names for debugging
print("Column names:", nvidia_data.columns)

# Use the correct column name after checking
close_column = 'Close'  # you might need to adjust based on the column names

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
print(f"Percentage Change in Stock Price: {percentage_change:.2f}%")
print(f"Highest Closing Price: ${highest_close:.2f}")
print(f"Lowest Closing Price: ${lowest_close:.2f}")
print(f"Average Trading Volume: {average_volume:.2f}")