import pandas as pd
from datetime import datetime

prices_list = [65000, 65100, 65200, 64900, 64800]
timestamps_list = pd.date_range(start="2026-01-01", periods=5, freq="H")

df = pd.DataFrame(data={'Price': prices_list}, index = timestamps_list)
df['Previous_Price'] = df['Price'].shift(1)
df['Price_Change'] = df['Price'] - df['Previous_Price']
df['Percent_Change'] = ((df['Price_Change'] / df['Previous_Price']) * 100)
df["SMA_3"] = df['Price'].rolling(window=3).mean()
df["Is_Bullish"] = df['Price'] > df["SMA_3"]

print(df)

# Create a NEW variable for the cleaned data
df_clean = df.dropna()

print("Cleaned Data Frame:")
print(df_clean)

buy_signals = df_clean[df_clean['Is_Bullish'] == True]
print(buy_signals)
