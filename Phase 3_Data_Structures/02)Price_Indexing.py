closing_prices = [1.1200, 1.1210, 1.1205, 1.1230]
current_price = closing_prices[-1]
previous_price = closing_prices[-2]

if current_price > previous_price:
    print("Price Increasing")
else:
    print("Price Decreasing or Flat")

    