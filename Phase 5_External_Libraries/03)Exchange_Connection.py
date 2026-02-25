import ccxt
exchange = ccxt.binance()
markets = exchange.load_markets()

print("The total number of trading pairs: ", len(markets))


