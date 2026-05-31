import ccxt

# 1. Initialize the tool
exchange = ccxt.binance()

# 2. Fetch the data
ticker = exchange.fetch_ticker('BTC/USDT')

# 3. Extract the specific piece of data
last_price = ticker['last']

print("The current price of BTC is: $", last_price)