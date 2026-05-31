current_price = 150
moving_average = 140

threshold = moving_average * 1.05

if current_price > threshold:
    print("Overextended Bullish")

elif current_price > moving_average and current_price < threshold:
    print("Bullish Trend")

else:
    print("Bearish Trend")

