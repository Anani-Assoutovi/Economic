
import pandas as pd
import plotly.graph_objects as go
import warnings
import kagglehub

class AppleStockAnalyzer:
    def __init__(self):
        warnings.filterwarnings('ignore')
        self.df = None
        self.data_path = None

    def download_dataset(self):
        path = kagglehub.dataset_download("muhammadatiflatif/apple-complete-stocks-datasetall-the-time")
        self.data_path = f"{path}/AAPL_1980-12-03_2025-04-17.csv"

    def load_data(self):
        self.df = pd.read_csv(self.data_path)
        self.df['date'] = pd.to_datetime(self.df['date'])
        self.df.sort_values(by='date', inplace=True)

    def compute_indicators(self):
        self.df['SMA_20'] = self.df['close'].rolling(window=20).mean()
        self.df['SMA_50'] = self.df['close'].rolling(window=50).mean()

    def plot_price_trend(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=self.df['date'], y=self.df['close'], mode='lines', name='Close Price', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=self.df['date'], y=self.df['adj_close'], mode='lines', name='Adjusted Close Price', line=dict(color='green')))
        fig.update_layout(title='Stock Price Trend Over Time', xaxis_title='Date', yaxis_title='Price', template='plotly_white', hovermode='x unified')
        fig.show()

    def plot_moving_averages(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=self.df['date'], y=self.df['close'], mode='lines', name='Close Price', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=self.df['date'], y=self.df['adj_close'], mode='lines', name='Adjusted Close Price', line=dict(color='green', dash='dot')))
        fig.add_trace(go.Scatter(x=self.df['date'], y=self.df['SMA_20'], mode='lines', name='20-Day SMA', line=dict(color='orange')))
        fig.add_trace(go.Scatter(x=self.df['date'], y=self.df['SMA_50'], mode='lines', name='50-Day SMA', line=dict(color='red')))
        fig.update_layout(title='Price Trend with Moving Averages', xaxis_title='Date', yaxis_title='Price', template='plotly_white', hovermode='x unified')
        fig.show()

    def plot_golden_death_crosses(self):
        golden_cross = (self.df['SMA_20'].shift(1) < self.df['SMA_50'].shift(1)) & (self.df['SMA_20'] > self.df['SMA_50'])
        death_cross = (self.df['SMA_20'].shift(1) > self.df['SMA_50'].shift(1)) & (self.df['SMA_20'] < self.df['SMA_50'])
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=self.df['date'], y=self.df['close'], mode='lines', name='Close Price', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=self.df['date'], y=self.df['adj_close'], mode='lines', name='Adjusted Close Price', line=dict(color='green', dash='dot')))
        fig.add_trace(go.Scatter(x=self.df['date'], y=self.df['SMA_20'], mode='lines', name='20-Day SMA', line=dict(color='orange')))
        fig.add_trace(go.Scatter(x=self.df['date'], y=self.df['SMA_50'], mode='lines', name='50-Day SMA', line=dict(color='red')))
        fig.add_trace(go.Scatter(x=self.df.loc[golden_cross, 'date'], y=self.df.loc[golden_cross, 'close'], mode='markers', name='Golden Cross', marker=dict(color='gold', size=10, symbol='star')))
        fig.add_trace(go.Scatter(x=self.df.loc[death_cross, 'date'], y=self.df.loc[death_cross, 'close'], mode='markers', name='Death Cross', marker=dict(color='black', size=10, symbol='x')))
        fig.update_layout(title='Golden and Death Crosses', xaxis_title='Date', yaxis_title='Price', template='plotly_white', hovermode='x unified')
        fig.show()


if __name__ == "__main__":
    analyzer = AppleStockAnalyzer()
    analyzer.download_dataset()
    analyzer.load_data()
    analyzer.compute_indicators()
    analyzer.plot_price_trend()
    analyzer.plot_moving_averages()
    analyzer.plot_golden_death_crosses()
