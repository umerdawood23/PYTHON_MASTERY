import ccxt
import time 

exchange = ccxt.binance()

target_price = 65500
while True:
    ticker = exchange.fetch_ticker("BTC/USDT")
    last_price = ticker['last']
    
    print("Current Price: ", last_price)
    if last_price >= target_price:
        print("TARGET HIT! SELLING BTC...")
        break
    time.sleep(5)




