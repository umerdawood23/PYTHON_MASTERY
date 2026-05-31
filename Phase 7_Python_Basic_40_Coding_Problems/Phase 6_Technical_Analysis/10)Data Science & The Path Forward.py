import pandas as pd

class QuantResearcher:
    def __init__(self, ticker):
        self.ticker = ticker
        self.data = None
        self.insights = {}

    def collect_data(self, source_path):
        """Step 2: Methodical Data Collection"""
        self.data = pd.read_csv(source_path)
        print(f"Data for {self.ticker} loaded successfully.")

    def detect_patterns(self):
        """Step 4: Pattern Recognition"""
        # Example: Simple Volatility Pattern
        self.data['volatility'] = self.data['price'].pct_change().rolling(20).std()
        self.insights['avg_vol'] = self.data['volatility'].mean()

    def tell_story(self):
        """Step 5: Storytelling"""
        story = f"The {self.ticker} market is currently showing an average volatility of {self.insights['avg_vol']:.4f}. "
        story += "This suggests a strategic choice to [adjust position sizing/stay out]."
        return story

# Applying the process
researcher = QuantResearcher("XAUUSD")
# researcher.collect_data('gold_ticks.csv')
# print(researcher.tell_story())