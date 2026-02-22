balance = 5000
risk_dollars = 2.0

def calculate_risk_amount(balance, risk_percent):
    risk_dollars = balance * (risk_percent/100)
    return risk_dollars

calculate_risk_amount = calculate_risk_amount(balance, risk_dollars)
print("Risk Amount:$",calculate_risk_amount)


