# Mutual Fund Data Scraper & Basic Forecasting System

## Project Report
### Submitted By
### *Akshya Jangir*

### Technology Used
#### Python, Streamlit, Pandas, BeautifulSoup, Requests, TextBlob

### Academic Year
#### 2024-25
## 1. Project Overview

#### This project is developed to collect mutual fund data from online sources, analyze fund performance, visualize trends, and perform basic forecasting using Python.

#### The system automatically gathers mutual fund information such as NAV, category, returns, and risk level. The collected data is cleaned, analyzed, and used for generating insights and future predictions.

---

## 2. Project Objectives

* #### Learn web scraping using Python
* #### Collect mutual fund data from websites
* #### Store data in CSV format
* #### Perform data cleaning and analysis
* #### Visualize mutual fund performance
* #### Implement basic forecasting techniques
* #### Build a simple dashboard for data presentation

---

## 3. Technologies Used

### Programming Language

* #### Python

### Libraries

* #### Requests
* #### BeautifulSoup
* #### Pandas
* #### NumPy
* #### Matplotlib ####
* #### Scikit-learn
* #### Streamlit

### Development Tools

* #### VS Code
* #### GitHub

---

## 4. Project Architecture

#### The project consists of four major modules:

### 4.1. Data Scraping Module

* #### Collects mutual fund information from online sources.
* #### Extracts fund name, NAV, returns, category, and risk level.
* #### Stores data in CSV format.

### 4.2. Data Analysis Module

* #### Cleans missing and invalid data.
* #### Performs return and risk analysis.
* #### Generates charts and reports.

### 4.3. Forecasting Module

* #### Selects the best-performing mutual fund.
* #### Generates historical NAV trends.
* #### Uses Linear Regression for future prediction.
* #### Predicts NAV for the next 30 days.

### 4.4. Dashboard Module

* #### Displays project statistics.
* #### Shows analysis graphs.
* #### Displays forecasting results.
* #### Provides an interactive interface using Streamlit.

---

## 5. Dataset Information

### Collected Data Fields:

* #### Mutual Fund Name
* #### NAV (Net Asset Value)
* #### Date
* #### Category
* #### 1-Year Return
* #### 3-Year Return
* #### Risk Level

---

## 6. Working Process

### Step 1

#### Run scraper.py

### Output:

* #### mutual_fund_analysis.csv
* #### mutual_funds_report.txt

### Step 2

#### Run analysis.py

### Output:

* #### Cleaned dataset
* #### Analysis graphs
* #### Category analysis

### Step 3

#### Run forecasting.py

### Output:

* #### Historical NAV data
* #### Forecast graph
* #### Forecast report
* #### 30-day prediction CSV

### Step 4

#### Run dashboard.py

### Output:

* #### Interactive dashboard
* #### Visualization and forecast display

---

## 7. Results

### The system successfully:

* #### Scraped mutual fund information
* #### Cleaned and processed the dataset
* #### Identified top-performing funds
* #### Visualized return trends
* #### Generated future NAV predictions
* #### Displayed results through a dashboard

---

## 8. Limitations

* #### Forecasting uses a basic Linear Regression model.
* #### Historical NAV data is simulated for demonstration purposes.
* #### Website structure changes may affect scraping performance.

---

## 9. Future Improvements

* #### Use real historical NAV APIs.
* #### Implement advanced forecasting models such as ARIMA and LSTM.
* #### Add fund recommendation system.
* #### Add real-time updates.
* #### Improve dashboard design and analytics.

---

## 10. Conclusion

#### The Mutual Fund Data Scraper & Basic Forecasting System successfully demonstrates the complete data pipeline from web scraping to forecasting. The project helped in understanding Python programming, data collection, analysis, visualization. It provides a strong foundation for building advanced financial analytics applications in the future.

---
---
# Thanks
--- 