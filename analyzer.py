import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from functools import wraps
import time
import os

# Decorator for timing functions
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time for {func.__name__}: {end_time - start_time:.2f} seconds")
        return result
    return wrapper

# Context manager for handling large data processing
class DataHandler:
    def __init__(self, filepath):
        self.filepath = filepath
    
    def __enter__(self):
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"File {self.filepath} not found.")
        self.df = pd.read_csv(self.filepath)
        return self.df
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing dataset")
        del self.df

# Load and clean dataset
@timer
def load_and_clean_data(filepath):
    with DataHandler(filepath) as df:
        df.dropna(inplace=True)  # Handle missing values
        df['Date'] = pd.to_datetime(df['Date'])  # Ensure Date column is in datetime format
        df.sort_values('Date', inplace=True)  # Sort data by date
        df['Daily Change %'] = ((df['Close'] - df['Open']) / df['Open']) * 100
        print("Data loaded and cleaned successfully.")
        return df

# Exploratory Data Analysis
@timer
def exploratory_analysis(df):
    print("Summary Statistics:\n", df.describe())
    top_performers = df.groupby('Symbol')['Daily Change %'].mean().nlargest(10)
    underperformers = df.groupby('Symbol')['Daily Change %'].mean().nsmallest(10)
    most_volatile = df.groupby('Symbol')['Daily Change %'].std().nlargest(10)
    
    print("Top 10 Performing Stocks:\n", top_performers)
    print("Top 10 Underperforming Stocks:\n", underperformers)
    print("Top 10 Most Volatile Stocks:\n", most_volatile)

# Data Aggregation
@timer
def aggregate_data(df):
    grouped = df.groupby(df['Date'].dt.to_period("M")).agg({'Shares Traded': 'sum', 'Close': 'mean'})
    print("Aggregated Data:\n", grouped.head())
    return grouped

# Visualization
@timer
def visualize_data(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['Close'], label='Closing Prices', color='b')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title('NIFTY50 Closing Prices Over Time')
    plt.legend()
    plt.show()
    
    plt.figure(figsize=(8, 4))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title('Feature Correlation Heatmap')
    plt.show()

if __name__ == "__main__":
    filepath = "/Users/tkkhand/Desktop/OracleIntern/python/stock_analyzer/nifty_fifty.csv" 
    if not filepath:
        raise ValueError("File path is not provided. Please specify a valid file path.")
    df = load_and_clean_data(filepath)
    exploratory_analysis(df)
    grouped_data = aggregate_data(df)
    visualize_data(df)
