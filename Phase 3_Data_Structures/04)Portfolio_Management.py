portfolio = [{"symbol":"ETH", "profit": 150}, {"symbol":"SOL", "profit":-50}]

portfolio[1]["profit"] = -100
Total_profit = portfolio[0]["profit"] + portfolio[1]["profit"]

print("The Total Profit of the portfolio is: ", Total_profit)

