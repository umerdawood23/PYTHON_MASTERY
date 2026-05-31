is_trade_open = True
current_profit = 2.5

if is_trade_open:
    if current_profit > 2.0:
        print("Target Reached: Closing Trade")
    else:
        print("Trade Open: Waiting for Target")
else:
    print ("Scanning for entry...")