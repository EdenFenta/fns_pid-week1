# Exploratory Data Analysis (EDA) Summary

## 1. Overview
This document summarizes the exploratory data analysis performed on the stock market and news sentiment dataset. The goal was to understand the structure of the data, identify trends, and detect any anomalies before sentiment and correlation analysis.

## 2. Stock Price Data Insights
The stock price dataset includes:
- Open price
- Close price
- High price
- Low price
- Volume

### Key Findings:
- Most stocks show clear daily price fluctuations.
- Some stocks display strong upward or downward trends.
- Trading volume spikes often align with large price movements.

## 3. News Data Insights
The news dataset contains:
- Headlines
- Publication dates
- Associated stock tickers

### Key Findings:
- News volume varies significantly by stock.
- Certain stocks receive more coverage during volatile periods.
- Headlines tend to cluster around earnings reports, product releases, and major corporate events.

## 4. Data Cleaning Steps
The following preprocessing steps were applied:
- Conversion of date columns to proper datetime format
- Removal of missing and duplicate records
- Filtering news data to match stock trading dates

## 5. Initial Observations
- There is visible temporal alignment between spikes in news activity and stock price volatility.
- Some news-heavy days do not always correspond to price movements, indicating noisy signals.

## 6. Conclusion
The EDA process provided a strong foundation for sentiment analysis and correlation modeling by ensuring data consistency and reliability.
