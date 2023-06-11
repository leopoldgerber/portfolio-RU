# Leopold Gerber - Data Analyst | Data Scientist Portfolio
## Обо мне
Привет, меня зовут Леопольд Гербер и являюсь Аналитиком данных/Дата сайентистом.

В моей работе на позиции аналитика данных мне встречались различные задачи, начиная от формирование запросов для выгрузки целевых групп и автоматизации отчетов, до создания скриптов для анализа конкурентов, с итоговым выводом расширяемости компании, и моделями для расчета рисков по смене конвертации внутренней валюты.

Портфолио хранит рабочие и соревновательные проекты. Каждый проект содержит краткое описание задачи, технические задачи, ожидаемые результаты, комментарии (при наличии) и примеры проделанных работа. 
Репозиторий был создан для демонстрации моих хард скиллов и для фиксации моего прогресса.

</br>

# Оглавление
- [1 - Marketing Web Scraping](#1---marketing-web-scraping) (Scraping, EDA, Power BI)
- [2 - Car Price Predict](#2---car-price-predict) (EDA, Feature Engineering, Machine Learning)
- [3 - Report Automation](#3---report-automation) (MySQL, Python)
- [4 - Sales Management](#4---sales-management) (SQL, EDA, Plotly Dash)
- [5 - Recommendation System](#5---recommendation-system) (EDA, Feature Engineering, Machine Learning, Python)

</br>

# Проекты в портфолио
## 1 - Marketing Web Scraping 
<code>[Script](1%20-%20Marketing%20Web%20Scraping/Marketing%20Web%20Scraping.py)</code>
<code>[Dashboard](1%20-%20Marketing%20Web%20Scraping/Marketing%20Web%20Scraping%20Power%20BI%20Demo.pbix)</code>

### - Описание - 
Скрипт-парсер, собирающий данные с платформы Semrush без использования API (является дополнительной услугой). Прописанный скрипт под управлением драйвера chrome, совершает авторизацию на платформе и парсит все необходимые отчеты. На 1 domain приходится 28 отчетов, включающийся в себя исторические данные за полгода (разделенные по месяцам), всю информацию о трафике: bounce, разделение на девайсы, источник трафика, уникальные пользователи, процент конверсии, продолжительность прибывание на сайте, переходы по поисковикам, обратные ссылки и т. д.  Общее количество отчетов составляет ~ 22 400, собранных воедино выходное количество отчетов составляет 6. Скрипт обрабатывает пустые отчеты, присваивает необходимые признаки, формирует новые (недостающие показатели). Подготовленные отчеты выгружаются в подготовленный дашборд для визуализации всех данных.

### - Результаты - 
Автоматизация отчетов. Визуализация данных. Благодаря парсингу исторических данных были сокращены убытки компании на оплату подписки (Месячная оплата плана + комиссия и Traffic Analytics API + комиссия).

### - Навыки -
report automation, data parser, data cleaning, feature engineering, data visualization

### - Технологический стек -
Python, Pandas, Numpy, Selenium, Power BI

</br>

[В начало](#content-table)

</br>

## 2 - Car Price Predict
<code>[Notebook](2%20-%20Project%20Car%20Price%20Predict/Project%20Car%20Price%20Predict.ipynb)</code>

### - Описание - 
Predict the price of the car taking into account the characteristics of the car. The model should improve the speed of car valuation and optimize the acceptance of cars for resale. Three datasets, compiled by different methods (manual and parsing) and in different years (from 2014 to 2021) were received for input. The project includes the following steps: data cleaning and preprocessing, filling in missing values, EDA (exploratory data analysis), hypothesis testing (F-critical, T-critical and p-value), statistical significance analysis (One-Way Anova), feature engineering, data visualization, experiment on five ML models.

### - Навыки - 
data cleaning, data analysis, descriptive statistics, central limit theorem, hypothesis testing, data visualization, feature engineering, machine learning.

### - Технологический стек - 
Python, Pandas, Numpy, Scipy Stats, Seaborn, Matplotlib, Statsmodels, Sklearn, CatBoost, RandomForestRegressor, ExtraTreesRegressor, XGBRegressor, StackingRegressor.

### - Результаты -
A script for optimizing preprocessing. Model for predicting car prices.

</br>

[В начало](#content-table)

</br>

## 3 - Report Automation
<code>[V7001 (Py)](3%20-%20Report%20Automation%20Script/V7001.py)</code>
<code>[V7002 (Py)](3%20-%20Report%20Automation%20Script/V7002.py)</code>
<code>[V7003 (Py)](3%20-%20Report%20Automation%20Script/V7003.py)</code>
<code>[V7004 (Py)](3%20-%20Report%20Automation%20Script/V7004.py)</code>
<code>[V7001 (SQL)](3%20-%20Report%20Automation%20Script/v7001_sql.sql)</code>
<code>[V7003 (SQL)](3%20-%20Report%20Automation%20Script/v7003_sql.sql)</code>

### - Описание - 
A family of scripts for automating reports on closed and open trades, deposits and withdrawals, and hedge fund information for a national bank. A bot for sending reports to everyone assigned.

### - Навыки - 
SQL Query, report automation.

### - Технологический стек - 
Python, Pandas, Numpy, mysql.connector, openpyxl, MySQL.

### - Результаты -
Creation of a script to automate reporting.

</br>

[В начало](#content-table)

</br>

### 4 - Sales Management
<code>[Notebook](4%20-%20Sales%20Management/Sales%20Management.ipynb)</code>
<code>[PlotlyDash (Files)](4%20-%20Sales%20Management/Plotly%20Dash/index.py)</code>
<code>[Power BI](4%20-%20Sales%20Management/Sales%20Management%20Dashboard.pbix)</code>

### - Описание - 
To increase profits by prioritizing the placement of goods in the storage area, it is necessary to set the profitability of goods by region. Additionally, the cost of transporting goods is reduced.
For this purpose, a request was formed to unload the data. Collection, analysis and preprocessing was done using the python programming language. Dashboards in Power BI and the created web service were prepared.

### - Навыки - 
data cleaning, data analysis, descriptive statistics, central limit theorem, hypothesis testing, data visualization, feature engineering, machine learning.

### - Технологический стек - 
SQL (SSMS, clearing tables), Python (data preprocessing, data preparation for the dashboard, pandas, numpy, seaborn, itertools, matplotlib, dash, plotly.express), Jupyter Lab (creating the plotly dash app)
Power BI (Creating an interactive dashboard), Heroku (Upload the Plotly Dash App)

### - Результаты - 
Automated data collection, preprocessing of received data, updating dashboards for visualization.

</br>

[В начало](#content-table)

</br>

### 5 - Recommendation System
<code>[Notebook 1: Analysis & Preprocessing](5%20-%20Recommendation%20System/1%20-%20Analysis%20&%20Preprocessing.ipynb)</code> <code>[Notebook 2: ML Models](5%20-%20Recommendation%20System/2%20-%20ML%20Models.ipynb)</code>

### - Описание - 
The goal of the task is to increase profits (by 20%) by selling additional products on the online store platform. The available files include a dataset with historical events on the platform, hashed product property data and a category tree. To solve the problem the data were analyzed, processed and prepared for ML models. Six models were involved in the experiments.

### - Навыки - 
data cleaning, data analysis, descriptive statistics, data visualization, feature engineering, machine learning, web-service, docker container

### - Технологический стек - 
Python (data preprocessing, data preparation, feature engineering, ML models testing, pandas, numpy, matplotlib), Flask (web-service), Docker (containerization)

### - Результаты - 
Using technical metrics (MAP@K and RMSE), a model was selected for recommendations, and a cold start strategy was created. The model was wrapped in a web service and containerized. The map metric showed a result of 33%. The task is completed.

</br>

[В начало](#content-table)
