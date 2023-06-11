# Leopold Gerber - Data Analyst | Data Scientist Portfolio
## About
Hello, I'm Leopold Gerber - but you can call me Leo - and I am a Data Analyst/Data Scientist.

As a data analyst, I've faced many tasks, ranging from generating queries for uploading target groups and automating reports, to creating scripts for competitor analysis and models that calculate the risks of domestic currency conversion.

My portfolio contains work and competition projects. Each project contains a brief description of the task, technical objectives, expected results, comments (if any) and examples of work done. 
I created this repository to showcase my hard skills and track my progress in Data Analytics / Data Science.

</br>

# Content Table
- [1 - Marketing Web Scraping](#1---marketing-web-scraping) (Scraping, EDA, Power BI)
- [2 - Car Price Predict](#2---car-price-predict) (EDA, Feature Engineering, Machine Learning)
- [3 - Report Automation](#3---report-automation) (MySQL, Python)
- [4 - Sales Management](#4---sales-management) (SQL, EDA, Plotly Dash)
- [5 - Recommendation System](#5---recommendation-system) (EDA, Feature Engineering, Machine Learning, Python)

</br>

# Portfolio Projects
## 1 - Marketing Web Scraping 
<code>[Script](1%20-%20Marketing%20Web%20Scraping/Marketing%20Web%20Scraping.py)</code>
<code>[Dashboard](1%20-%20Marketing%20Web%20Scraping/Marketing%20Web%20Scraping%20Power%20BI%20Demo.pbix)</code>

### - Description - 
A parser script that collects data from the Semrush platform without using an API (is an optional service). The script runs on the chrome driver, logs into the platform and parses all the necessary reports. There are 28 reports per domain, including semiannual historical data (separated by months), all the information about the traffic: bounce, splits by devices, traffic source, unique users, conversion percentage, staying duration, search engine hits, backlinks etc.  The total number of reports is ~ 22 400, the output number of reports is 6. The script processes the empty reports, assigns the necessary attributes and generates new ones (missing indicators). The prepared reports are uploaded to the prepared dashboard to visualize all the data.

### - Results - 
Reporting automation. Data visualization. Thanks to parsing of historical data we managed to save on platform fees (monthly expenses for plan + tax and Traffic Analytics API + tax).

### - Skills -
report automation, data parser, data cleaning, feature engineering, data visualization

### - Technology -
Python, Pandas, Numpy, Selenium, Power BI

</br>

[Scroll up](#content-table)

</br>

## 2 - Car Price Predict
<code>[Notebook](2%20-%20Project%20Car%20Price%20Predict/Project%20Car%20Price%20Predict.ipynb)</code>

### - Description - 
Predict the price of the car taking into account the characteristics of the car. The model should improve the speed of car valuation and optimize the acceptance of cars for resale. Three datasets, compiled by different methods (manual and parsing) and in different years (from 2014 to 2021) were received for input. The project includes the following steps: data cleaning and preprocessing, filling in missing values, EDA (exploratory data analysis), hypothesis testing (F-critical, T-critical and p-value), statistical significance analysis (One-Way Anova), feature engineering, data visualization, experiment on five ML models.

### - Skills - 
data cleaning, data analysis, descriptive statistics, central limit theorem, hypothesis testing, data visualization, feature engineering, machine learning.

### - Technology - 
Python, Pandas, Numpy, Scipy Stats, Seaborn, Matplotlib, Statsmodels, Sklearn, CatBoost, RandomForestRegressor, ExtraTreesRegressor, XGBRegressor, StackingRegressor.

### - Results -
A script for optimizing preprocessing. Model for predicting car prices.

</br>

[Scroll up](#content-table)

</br>

## 3 - Report Automation
<code>[V7001 (Py)](3%20-%20Report%20Automation%20Script/V7001.py)</code>
<code>[V7002 (Py)](3%20-%20Report%20Automation%20Script/V7002.py)</code>
<code>[V7003 (Py)](3%20-%20Report%20Automation%20Script/V7003.py)</code>
<code>[V7004 (Py)](3%20-%20Report%20Automation%20Script/V7004.py)</code>
<code>[V7001 (SQL)](3%20-%20Report%20Automation%20Script/v7001_sql.sql)</code>
<code>[V7003 (SQL)](3%20-%20Report%20Automation%20Script/v7003_sql.sql)</code>

### - Description - 
A family of scripts for automating reports on closed and open trades, deposits and withdrawals, and hedge fund information for a national bank. A bot for sending reports to everyone assigned.

### - Skills - 
SQL Query, report automation.

### - Technology - 
Python, Pandas, Numpy, mysql.connector, openpyxl, MySQL.

### - Results -
Creation of a script to automate reporting.

</br>

[Scroll up](#content-table)

</br>

### 4 - Sales Management
<code>[Notebook](4%20-%20Sales%20Management/Sales%20Management.ipynb)</code>
<code>[PlotlyDash (Files)](4%20-%20Sales%20Management/Plotly%20Dash/index.py)</code>
<code>[Power BI](4%20-%20Sales%20Management/Sales%20Management%20Dashboard.pbix)</code>

### - Description - 
To increase profits by prioritizing the placement of goods in the storage area, it is necessary to set the profitability of goods by region. Additionally, the cost of transporting goods is reduced.
For this purpose, a request was formed to unload the data. Collection, analysis and preprocessing was done using the python programming language. Dashboards in Power BI and the created web service were prepared.

### - Skills - 
data cleaning, data analysis, descriptive statistics, central limit theorem, hypothesis testing, data visualization, feature engineering, machine learning.

### - Technology - 
SQL (SSMS, clearing tables), Python (data preprocessing, data preparation for the dashboard, pandas, numpy, seaborn, itertools, matplotlib, dash, plotly.express), Jupyter Lab (creating the plotly dash app)
Power BI (Creating an interactive dashboard), Heroku (Upload the Plotly Dash App)

### - Results - 
Automated data collection, preprocessing of received data, updating dashboards for visualization.

</br>

[Scroll up](#content-table)

</br>

### 5 - Recommendation System
<code>[Notebook 1: Analysis & Preprocessing](5%20-%20Recommendation%20System/1%20-%20Analysis%20&%20Preprocessing.ipynb)</code> <code>[Notebook 2: ML Models](5%20-%20Recommendation%20System/2%20-%20ML%20Models.ipynb)</code>

### - Description - 
The goal of the task is to increase profits (by 20%) by selling additional products on the online store platform. The available files include a dataset with historical events on the platform, hashed product property data and a category tree. To solve the problem the data were analyzed, processed and prepared for ML models. Six models were involved in the experiments.

### - Skills - 
data cleaning, data analysis, descriptive statistics, data visualization, feature engineering, machine learning, web-service, docker container

### - Technology - 
Python (data preprocessing, data preparation, feature engineering, ML models testing, pandas, numpy, matplotlib), Flask (web-service), Docker (containerization)

### - Results - 
Using technical metrics (MAP@K and RMSE), a model was selected for recommendations, and a cold start strategy was created. The model was wrapped in a web service and containerized. The map metric showed a result of 33%. The task is completed.

</br>

[Scroll up](#content-table)
