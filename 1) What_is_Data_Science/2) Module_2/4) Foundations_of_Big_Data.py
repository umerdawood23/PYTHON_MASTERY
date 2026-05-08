import pandas as pd

# 1. Variety: Mixing structured prices with unstructured 'Social Sentiment'
data = {
    'timestamp': ['2026-03-18 09:00', '2026-03-18 09:01'],
    'price': [2150.50, 2151.20],                    # Structured
    'tweet_text': ["Gold is mooning!", "Sell XAU now!"] # Unstructured
}
df = pd.DataFrame(data)

# 2. Veracity: Checking for 'Completeness' or 'Outliers'
# Simple filter to ensure we don't have null values (Completeness)
df_clean = df.dropna()

# 3. Value: Turning text into a 'Sentiment Score' (1 = Bullish, -1 = Bearish)
def get_sentiment(text):
    if "mooning" in text.lower(): return 1
    if "sell" in text.lower(): return -1
    return 0

df_clean['sentiment'] = df_clean['tweet_text'].apply(get_sentiment)
print(df_clean[['price', 'sentiment']])