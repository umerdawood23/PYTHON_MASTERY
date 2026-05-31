import pandas as pd

# 1. Traditional approach: Manual check (Slow/Small scale)
# 2. Computational approach: Vectorized operations (Fast/Big Data scale)

def calculate_technical_indicators(df):
    """Applying the 'Bank' logic of grinding data sideways"""
    # Calculate a 20-period moving average
    df['SMA_20'] = df['Close'].rolling(window=20).mean()
    
    # Identify 'Outlier' events (Volatility spikes)
    df['Volatility'] = df['Close'].pct_change().std()
    
    return df

# Example usage for XAUUSD data
# df = pd.read_csv('gold_tick_data.csv')
# df_processed = calculate_technical_indicators(df)