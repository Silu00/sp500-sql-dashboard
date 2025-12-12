# 📊 S&P 500 SQL Analytics Dashboard

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)
![SQL](https://img.shields.io/badge/Database-PostgresSQL-blue)
![Python](https://img.shields.io/badge/Python-3.9%2B-green)
![ETL](https://img.shields.io/badge/Pipeline-ETL-orange)

An interactive financial dashboard backed by a relational database. This project demonstrates an end-to-end data engineering pipeline: fetching stock market data, modeling it in a SQL database, and visualization.

## Project Overview

Unlike simple CSV-based analysis, this project simulates a production-grade environment where financial data is stored persistently in a SQL database. It focuses on performing heavy data aggregations on the database layer rather than in memory.

**Key Features:**
* **ETL Pipeline:** Python scripts to fetch S&P 500 data (tickers, financials, historical prices) and load them into a normalized SQL database.
* **SQL-Driven Analysis:** Key metrics (Moving Averages, Daily Returns, Volatility) are computed using SQL queries.
* **Data Persistence:** Uses a relational database (SQLite/PostgreSQL) to store historical data.

## Architecture

1.  **Ingestion:** Data is scraped from Wikipedia (constituents) and fetched via APIs (Yahoo Finance).
2.  **Storage:** Data is normalized into relational tables (e.g., `companies`, `stock_prices`, `financials`).
3.  **Processing:** SQL Window Functions and aggregations transform raw data into analytical metrics.

## Database Schema

The project uses a normalized schema to ensure data integrity:

* **`dim_companies`**: Stores static info (Ticker, Name, Sector, Industry, HQ).
* **`fact_prices`**: Time-series data (Date, Open, High, Low, Close, Volume).
* **`fact_fundamentals`**: Quarterly/Annual metrics (P/E, EPS, Dividend Yield).

## Tech Stack

* **Backend & ETL:** Python, SQLAlchemy, Pandas
* **Database:** SQLite (default) or PostgreSQL
* **Frontend:** Streamlit, Plotly (for interactive charts)
* **Data Source:** `yfinance` API

## 🔍 SQL Analysis Example

This project emphasizes SQL proficiency. For example, calculating the **50-day Moving Average** is done directly in the query:

```sql
SELECT 
    date,
    close,
    AVG(close) OVER(
        PARTITION BY symbol 
        ORDER BY date 
        ROWS BETWEEN 49 PRECEDING AND CURRENT ROW
    ) as ma_50
FROM fact_prices
WHERE symbol = 'AAPL';

