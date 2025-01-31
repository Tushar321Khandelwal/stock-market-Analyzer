# Stock Market Data Analysis

## Overview
This Streamlit application allows users to upload a CSV file containing stock market data and performs various analyses, including:
- Data preprocessing (handling missing values, duplicates, and date formatting)
- Feature computation (daily return and moving average)
- Data visualization (closing price trend, correlation heatmap, and daily return distribution)
- JSON-based analysis output

## Features
- **CSV File Upload**: Users can upload a CSV file containing stock market data.
- **Data Preprocessing**:
  - Converts 'Date' column to datetime format.
  - Drops missing values and duplicate entries.
- **Feature Engineering**:
  - Computes daily return percentage.
  - Calculates a 7-day moving average.
- **Visualizations**:
  - Line plot of closing prices.
  - Correlation heatmap of numerical features.
  - Histogram of daily return distribution.
- **JSON Output**:
  - Provides a JSON summary of correlation heatmap values and daily return distribution.

## Installation & Setup
### Prerequisites
Ensure you have Python installed along with the following dependencies:
```sh
pip install streamlit pandas numpy matplotlib seaborn
```

### Running the Application
1. Clone or download this repository.
2. Navigate to the project directory and run:
```sh
streamlit run app.py
```
3. Upload a CSV file with stock market data (including 'Date', 'Open', and 'Close' columns).

## Usage
- Upload a CSV file containing stock market data.
- View data preprocessing and computed features.
- Analyze stock trends with visualizations.
- View a JSON summary of analysis results.

## Expected CSV Format
The uploaded CSV file should include the following columns:
- `Date`: Date of stock data (YYYY-MM-DD format recommended)
- `Open`: Opening stock price
- `Close`: Closing stock price
- Additional numerical columns (optional) for correlation analysis

## Example Output
### Data Preview
| Date       | Open  | Close | Daily Return | Moving Avg (7-day) |
|------------|------:|------:|-------------:|--------------------:|
| 2024-01-01 | 100.0 | 105.0 |         5.00 |               102.5 |
| 2024-01-02 | 105.0 | 107.0 |         1.90 |               103.0 |

### Visualizations
- **Closing Price Trend**: A line chart of closing prices over time.
- **Feature Correlation Heatmap**: A heatmap showing correlation between numerical features.
- **Daily Return Distribution**: A histogram showing the distribution of daily returns.

<img width="945" alt="image" src="https://github.com/user-attachments/assets/15ad0102-2701-4040-a2fd-67026b096f99" />
<img width="842" alt="image" src="https://github.com/user-attachments/assets/721dfdf4-1977-4c1e-8b46-eabeacfd301e" />
<img width="896" alt="image" src="https://github.com/user-attachments/assets/95c862f4-bee3-4653-877f-d6b5a77724d1" />
<img width="830" alt="image" src="https://github.com/user-attachments/assets/08932a04-2894-434c-b262-6fef53ef2064" />
<img width="849" alt="image" src="https://github.com/user-attachments/assets/2f75cd61-ded4-4a08-97b0-4621180844d6" />

### JSON Output Example
```json
{
    "Feature Correlation Heatmap": {
        "Open": {"Open": 1.0, "Close": 0.98},
        "Close": {"Open": 0.98, "Close": 1.0}
    },
    "Daily Return Distribution": [5.0, 1.9, -2.1, 3.4]
}
```


<img width="766" alt="image" src="https://github.com/user-attachments/assets/74d74756-ae58-4169-9c0a-b50dd656b5d7" />
