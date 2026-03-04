import pandas as pd
from datetime import datetime

prices_list = [65000, 65100, 65200, 64900, 64800]
timestamps_list = pd.date_range(start="2026-01-01", periods=5, freq="h") # Changed to 'h' to avoid warning

df = pd.DataFrame(data={'Price': prices_list}, index = timestamps_list)
df['Previous_Price'] = df['Price'].shift(1)
df['Price_Change'] = df['Price'] - df['Previous_Price']
df['Percent_Change'] = ((df['Price_Change'] / df['Previous_Price']) * 100)
df["SMA_3"] = df['Price'].rolling(window=3).mean()
df["Is_Bullish"] = df['Price'] > df["SMA_3"]

# THE FIX: Add .copy() here to make df_clean an independent object
df_clean = df.dropna().copy()

# Now adding columns won't trigger warnings
df_clean['Gain'] = df_clean['Price_Change'].clip(lower=0)
df_clean['Loss'] = df_clean['Price_Change'].clip(upper=0).abs()

print("--- Cleaned Data with Gains and Losses ---")
print(df_clean[['Price', 'Price_Change', 'Gain', 'Loss']])