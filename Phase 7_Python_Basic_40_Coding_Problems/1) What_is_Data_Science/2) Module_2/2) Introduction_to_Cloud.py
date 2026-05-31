import pandas as pd

# 1. Defining the 'Measured Service' Costs
COST_PER_CPU_HOUR = 0.05  # Standard IaaS rate

# 2. Daily Resource Usage (Fluctuating Demand)
usage_log = pd.DataFrame({
    'hour': range(1, 7),
    'cpu_count': [2, 2, 32, 64, 8, 2] # Scaling up for backtesting, then scaling back
})

# 3. Calculating the Total Cost (Pay-for-use)
usage_log['hourly_cost'] = usage_log['cpu_count'] * COST_PER_CPU_HOUR
total_cost = usage_log['hourly_cost'].sum()

print(f"Total Cloud Cost for Session: ${total_cost:.2f}")
# This highlights 'Rapid Elasticity'—only paying $3.20 for a massive 64-core burst!