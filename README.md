# Walmart Sales Forecasting Project

## 📌 Project Overview
This project implements a time series forecasting model to predict Walmart's weekly sales using historical sales data. The goal is to build a reliable forecasting system that can help with inventory planning and demand management.

## 📊 Dataset
- **Source**: [Walmart Sales Forecast Dataset on Kaggle](https://www.kaggle.com/datasets/aslanahmedov/walmart-sales-forecast)
- **File**: `train.csv`
- **Time Period**: 2010-2012 (weekly data)
- **Key Variables**:
  - `Date`: Weekly date (Fridays)
  - `Weekly_Sales`: Total weekly sales across all stores

## 🛠️ Implementation

### 1. Data Preparation
- Convert date column to datetime format
- Aggregate sales by week
- Set date as index for time series analysis

### 2. Exploratory Data Analysis
- **Time Series Plot** (`ts_plot.png`): Visualize sales trends over time
  ![Time Series Plot](https://github.com/AKDAD9/Demand-Forecasting-/blob/main/Demand%20F/ts%20plot.png?raw=true)
  
- **Seasonal Decomposition** (`Sesonal.png`): Analyze trend, seasonality, and residuals using additive model (period=52 weeks)
  ![Seasonal Decomposition](https://github.com/AKDAD9/Demand-Forecasting-/blob/main/Demand%20F/Sesonal.png?raw=true)
  
- **Stationarity Test**: Augmented Dickey-Fuller test to check data stationarity

### 3. Model Diagnostics
- **Autocorrelation Function (ACF)** (`ACF.png`): Shows correlation between observations at different time lags
  ![ACF Plot](https://github.com/AKDAD9/Demand-Forecasting-/blob/main/Demand%20F/ACF.png?raw=true)
  
- **Partial Autocorrelation Function (PACF)** (`PACF.png`): Shows correlation after removing intermediate observations
  ![PACF Plot](https://github.com/AKDAD9/Demand-Forecasting-/blob/main/Demand%20F/PACF.png?raw=true)

### 4. Model Building
**SARIMAX Model** with parameters:
- Order: (1, 0, 1)
- Seasonal Order: (1, 0, 1, 52)
- 52-week seasonal pattern (annual cycle)

### 5. Forecasting Results
- **Forecast vs Actual Comparison** (`Forecast.png`): Shows model predictions against actual sales data
  ![Forecast Results](https://github.com/AKDAD9/Demand-Forecasting-/blob/main/Demand%20F/Forecast.png?raw=true)
  
- Generate 52-week ahead forecasts
- Calculate 95% confidence intervals
- Export results to Excel for further analysis

## 📈 Key Results

### Statistical Tests
- **ADF Statistic**: -5.908
- **p-value**: 2.68e-07
- **Conclusion**: The time series is stationary (reject null hypothesis of unit root)

### Model Output
- **Forecast Period**: 52 weeks
- **Output File**: `Weekly_Sales_Forecast.xlsx`
- **Columns**: Date, Forecast, Lower_CI, Upper_CI

## 📁 File Structure
