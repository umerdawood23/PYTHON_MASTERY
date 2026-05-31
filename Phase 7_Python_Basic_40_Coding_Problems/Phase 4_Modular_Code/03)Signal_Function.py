current_market_price = 95
price = 0.0

def check_signal(price):
    if price < 100:
        return "BUY"
    else:
        return "WAIT"
    
signal = check_signal(current_market_price)

print("The current signal is: " + str(signal))


