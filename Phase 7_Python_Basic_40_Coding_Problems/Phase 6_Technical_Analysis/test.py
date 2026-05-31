import pandas as pd

# Load your XAUUSD Tick or OHLCV data
df = pd.read_csv('2026.4.24AMDUSUSD_dukascopy_TICK_UTC-TICK-No Session.csv', parse_dates=True, index_col='Timestamp')

# 1. 'Study' the data properties (Data Science as a study of data)
print(df.info()) 

# 2. Basic Hypothesis: Is the daily return mean-reverting?
df['returns'] = df['Close'].pct_change()

# 3. Validation: Quick look at the 'Story' (Distribution)
print(df['returns'].describe())

# 4. Visualization: Uncovering the 'Trend'
df['Close'].plot(title='Gold Price Strategic View')