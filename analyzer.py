
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json

def preprocess_data(df):
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    return df

def compute_features(df):
    if {'Open', 'Close'}.issubset(df.columns):
        df['Daily Return'] = (df['Close'] - df['Open']) / df['Open'] * 100
    if 'Close' in df.columns:
        df['Moving Avg (7-day)'] = df['Close'].rolling(window=7).mean()
    return df

def plot_closing_price(df):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x=df['Date'], y=df['Close'], ax=ax)
    plt.title('Closing Price Trend')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.xticks(rotation=45)
    return fig

def plot_correlation_heatmap(df):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
    plt.title('Feature Correlation Heatmap')
    return fig

def plot_daily_return_distribution(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(df['Daily Return'], bins=30, kde=True, ax=ax)
    plt.title('Distribution of Daily Returns')
    plt.xlabel('Daily Return (%)')
    plt.ylabel('Frequency')
    return fig

st.title("Stock Market Data Analysis")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df = preprocess_data(df)
    df = compute_features(df)
    
    st.subheader("Data Preview")
    st.write(df.head())
    
    st.subheader("Visualizations")
    
    st.pyplot(plot_closing_price(df))
    st.pyplot(plot_correlation_heatmap(df))
    st.pyplot(plot_daily_return_distribution(df))
    
    analysis_results = {
        "Feature Correlation Heatmap": df.corr().to_dict(),
        "Daily Return Distribution": df['Daily Return'].tolist(),
    }
    
    st.subheader("Analysis Results (JSON Format)")
    st.json(json.dumps(analysis_results, indent=4, default=str))
