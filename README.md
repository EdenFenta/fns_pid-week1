# news-sentiment-price-prediction

## Project Overview
This project analyzes financial news headlines and stock market data to understand how sentiment and technical indicators relate to price movements.

The work is organized into three tasks:
- **Task 1:** News data cleaning and exploratory analysis
- **Task 2:** Technical indicator computation
- **Task 3:** Sentiment analysis and correlation with stock prices

---

## Folder Structure
```
.vscode/               # VSCode settings
.github/workflows/     # CI workflow (unittests.yml)
.gitignore
requirements.txt       # Python dependencies
README.md
src/                   # Source code
- __init__.py
- data_prep.py         # Task 1: News data cleaning
- eda.py               # Task 1: EDA helper functions
- indicators.py        # Task 2: Technical indicators logic
- sentiment.py         # Task 3: Sentiment analysis logic
- correlation.py       # Task 3: Correlation calculations
notebooks/             # Jupyter notebooks
- 01_eda.ipynb
- 02_indicators.ipynb
- 03_sentiment.ipynb
tests/                 # Unit tests
- test_data_prep.py
- test_indicators.py
- test_sentiment.py
data/
- raw/                 # Raw datasets
- processed/           # Processed datasets
outputs/
- figs/                # Saved figures and plots
```

---

## Getting Started

### 1. Clone the Repository
```bash
git clone <your_repo_url>
cd news-sentiment-price-prediction
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Task 1 – News Data Preparation & Exploratory Data Analysis

### Run Data Preparation
```bash
python src/data_prep.py
```

This script:
- Loads raw data from `data/raw/raw_analyst_ratings.csv`
- Cleans and normalizes headlines
- Generates:
  - `headline_length_chars`
  - `headline_length_tokens`
  - `headline_lower`
  - `date_only`
- Output: `data/processed/clean_news.parquet`

### Run EDA Notebook
```bash
jupyter notebook notebooks/01_eda.ipynb
```

This covers:
- Headline length distributions
- Publisher frequency analysis
- Daily headline trends
- Keyword and topic exploration

Figures are saved to: `outputs/figs/`

## Task 2 – Technical Indicators on Stock Prices

### Input Data
Place stock price CSV files in: `data/raw/`

Example files:
- `AAPL.csv`
- `AMZN.csv`
- `GOOG.csv`
- `META.csv`
- `MSFT.csv`
- `NVDA.csv`

### Run Indicator Pipeline
```bash
python src/pipeline.py
```

This pipeline:
- Loads stock data
- Computes:
  - SMA
  - EMA
  - RSI
  - MACD
  - Bollinger Bands
  - Daily Returns
- Saves indicator plots to: `outputs/figs/`

## Task 3 – News Sentiment & Correlation Analysis

### Step 1: Run Sentiment Scoring
```bash
python src/sentiment.py
```

This:
- Loads cleaned news data
- Computes sentiment scores
- Adds:
  - `sentiment_score`
  - `sentiment_label`

### Step 2: Run Correlation Analysis
```bash
python src/correlation.py
```

This:
- Merges news sentiment with stock prices by date
- Computes correlations between:
  - `sentiment_score`
  - `daily_returns`
- Saves correlation heatmaps and plots to: `outputs/figs/`

## Running Tests
```bash
export PYTHONPATH=.  # Mac/Linux
set PYTHONPATH=.     # Windows
pytest tests/
```

## Git Workflow

### Task 1
```bash
git checkout -b task-1
git add .
git commit -m "Task-1: data preparation and EDA"
git push -u origin task-1
```

### Task 2
```bash
git checkout -b task-2
git add .
git commit -m "Task-2: technical indicators and stock pipeline"
git push -u origin task-2
```

### Task 3
```bash
git checkout -b task-3
git add .
git commit -m "Task-3: sentiment analysis and correlation"
git push -u origin task-3
```
