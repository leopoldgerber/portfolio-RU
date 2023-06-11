# Леопольд Гербер - Data Analyst | Data Scientist Portfolio
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
Предсказание цены автомобиля с учетом характеристик авто. Модель должна улучшить скорость оценки автомобиля и оптимизировать прием авто на перепродажу. На вход получены 3 датасета, составленных разными способами (ручным и пасрингом) и в разные года (с 2014 по 2021 года). Проект включает в себя следующие шаги: очистка и предобработка данных, заполнение недостающих значений, EDA (exploratory data analysis), проверка гипотез (F-критическая, T-критическая и p-value), анализ статистической значимости (One-Way Anova), feature engineering, визуализация данных, эксперимент на пяти моделей МО.

### - Навыки - 
data cleaning, data analysis, descriptive statistics, central limit theorem, hypothesis testing, data visualization, feature engineering, machine learning.

### - Технологический стек - 
Python, Pandas, Numpy, Scipy Stats, Seaborn, Matplotlib, Statsmodels, Sklearn, CatBoost, RandomForestRegressor, ExtraTreesRegressor, XGBRegressor, StackingRegressor.

### - Результаты -
Скрипт для оптимизации предобработки. Модель для предсказаний цен на авто.

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
Скрипты для автоматизации семейства отчетов. Отчетность содержит информацию о закрытых и открытых сделках, пополнениях и снятиях, и информация о хедж-фонде. Отчеты участвуют в рассылке через телеграмм бот всем назначенным и передаются в национальный банк.

### - Навыки - 
SQL Query, report automation.

### - Технологический стек - 
Python, Pandas, Numpy, mysql.connector, openpyxl, MySQL.

### - Результаты -
Сформированные запросы и скрипты для автоматизации отчетов.

</br>

[В начало](#content-table)

</br>

### 4 - Sales Management
<code>[Notebook](4%20-%20Sales%20Management/Sales%20Management.ipynb)</code>
<code>[PlotlyDash (Files)](4%20-%20Sales%20Management/Plotly%20Dash/index.py)</code>
<code>[Power BI](4%20-%20Sales%20Management/Sales%20Management%20Dashboard.pbix)</code>

### - Описание - 
Чтобы увеличить прибыль за счет приоритетного размещения товаров в складской зоне необходимо установить прибыльность товаров по регионам. Дополнительно сокращаются расходы на транспортировку товаров.
Для этого был сформирован запрос для выгрузки данных. Сбор, анализ и предобработка были произведены с помощью языка программирования python. Подготовлены дашборды в Power BI и созданном веб-сервисе. 

### - Навыки - 
data cleaning, data analysis, descriptive statistics, central limit theorem, hypothesis testing, data visualization, feature engineering, machine learning.

### - Технологический стек - 
SQL (SSMS, clearing tables), Python (data preprocessing, data preparation for the dashboard, pandas, numpy, seaborn, itertools, matplotlib, dash, plotly.express), Jupyter Lab (creating the plotly dash app)
Power BI (Creating an interactive dashboard), Heroku (Upload the Plotly Dash App)

### - Результаты - 
Автоматизированный сбор данных, предобработка полученных данных, обновление дашбордов для визуализации.

</br>

[В начало](#content-table)

</br>

### 5 - Recommendation System
<code>[Notebook 1: Analysis & Preprocessing](5%20-%20Recommendation%20System/1%20-%20Analysis%20&%20Preprocessing.ipynb)</code> <code>[Notebook 2: ML Models](5%20-%20Recommendation%20System/2%20-%20ML%20Models.ipynb)</code>

### - Описание - 
Маркетплейс обратился в агентство с задачей увеличить прибыль на 20% за счет продажи дополнительных продуктов на платформе интернет-магазина. Имеющиеся файлы включают набор данных с историческими событиями на платформе, хешированные данные о свойствах товара и дерево категорий. Для решения поставленной задачи данные были проанализированы, обработаны и подготовлены для ML-моделей. В эксперименте было задействовано шесть моделей МО.

### - Навыки - 
data cleaning, data analysis, descriptive statistics, data visualization, feature engineering, machine learning, web-service, docker container

### - Технологический стек - 
Python (data preprocessing, data preparation, feature engineering, ML models testing, pandas, numpy, matplotlib), Flask (web-service), Docker (containerization)

### - Результаты - 
С помощью результатов технических метрик (MAP@K and RMSE) была выбрана модель (из тестируемых). Подготовлена стратегия холодного старта. Модель была обернута в веб-сервис и контейнеризированные. Результат MAP@K метрики составляет 33%.

</br>

[В начало](#content-table)
