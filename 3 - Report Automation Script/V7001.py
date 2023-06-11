#!/usr/bin/env python
# coding: utf-8

# In[4]:


#================ LIBRARIES ================

import mysql.connector
from mysql.connector import Error

from datetime import date
import json

import pandas as pd
import requests
from xml.etree import ElementTree

from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter

#================ FUNCTION TO CONNECT TO THE SQL SERVER ================

# Configuration file
with open("database_config.json") as config:
    database_config = json.load(config)
    
def mysql_conncetion(host_name, port_name, user_name, user_password, database_name = None):
    database_connection = None
    try:
        database_connection = mysql.connector.connect(
            host = host_name,
            port = port_name,
            user = user_name,
            password = user_password,
            database = database_name
        )
        print("================ CONNECTED")
    except Error as db_connection_error:
        print(db_connection_error)
    return database_connection

#================ SQL SERVER CONNECTION - CONFIG CHECK ================

connection = mysql_conncetion(database_config['host'],
                              database_config['port'],
                              database_config['user'],
                              database_config['password'])


#================ SQL READER ================

sql_file_reader = open('v7001_sql.sql', 'r', encoding='utf8')
sql_file = sql_file_reader.read()
sql_file_reader.close()
sql_file = sql_file.replace('\n',' ').replace('\t',' ').split(';')

#================ EXECUTE QUERY ================

V7001_1 = pd.DataFrame()
V7001_2_4 = pd.DataFrame()
V7001_5 = pd.DataFrame()
V7001_6 = pd.DataFrame()

var_list = [V7001_1, V7001_2_4, V7001_5, V7001_6]

for command in enumerate(sql_file):
    try:    
        cursor = connection.cursor(dictionary = True)
        try_sql_query = f'''{sql_file[-3]}'''
        cursor.execute(try_sql_query)
        query_result = cursor.fetchall()

        var_list[0] = pd.DataFrame(query_result)

    except Error as error:
        print('Error K1:', error)
        
cursor.close()
connection.close()

#================ CONNECT TO NBRB ================

response = requests.get("https://www.nbrb.by/api/exrates/currencies", verify=False)
json = response.json()

dataset = pd.DataFrame.from_dict(pd.json_normalize(json), orient = 'columns')


#================ PREPROCESSING ================

# Create unique symbols from V7001_6
currency = set()

for symbol in V7001_6['currency']: 
    currency.add(symbol)

# Create temporary dictionary
temp = []

for symbol in currency:
    temp.append(requests.get(
        "https://www.nbrb.by/api/exrates/rates/" + symbol + "?parammode=2", verify=False).json())

# Prepare dataset   
data = pd.DataFrame(temp).rename(columns={'Cur_Abbreviation':'currency'})

data.columns = data.columns.str.lower()

usd_curr = float(data[data['currency'] == 'USD']['cur_officialrate'])

df = data.drop(['cur_id', 'date', 'cur_name'], axis = 1)

# Merge 
V7001_6 = V7001_6.merge(df, on = ['currency'])

# Create converted tables
V7001_6['BYN'] = round(V7001_6.sum_amount * (V7001_6.cur_officialrate / V7001_6.cur_scale), 2)

V7001_6['USD'] = round(V7001_6.BYN / list(dict(
    requests.get("https://www.nbrb.by/api/exrates/rates/usd?parammode=2", verify=False).json()).values())[-1], 2)

# Feature enginnering
V7001_6['multiplier'] = V7001_6['instrument_group'].apply(lambda x: 20 if str(x) == '4.0' else (20 if str(x) == 'nan' else 100))

V7001_6['feature_usd'] = V7001_6['USD'] * V7001_6['multiplier']
V7001_6['feature_byn'] = V7001_6['feature_usd'] * usd_curr
V7001_6.drop(columns = ['multiplier', 'instrument_group', 'size_of_the_contract'], inplace = True)

V7001_6.full_symbol = V7001_6.full_symbol.apply(lambda x : str(x).replace('#',''))

#================ DATAFRAMES TO EXCEL ================

def dataframes_to_excel(df_list, sheets, file_name, spaces): 
    writer = pd.ExcelWriter(file_name,engine='xlsxwriter')  
    data = V7001_6.to_excel(writer, sheet_name = 'Лист 1', index = False)
    row = 0 
    for dataframe in df_list: 
        dataframe.to_excel(writer,sheet_name=sheets,startrow=row , startcol=0, index = False)    
        row = row + len(dataframe.index) + spaces + 1 
        writer.sheets['Лист 1'].set_column(0,7,13)
        writer.sheets['Лист 2'].set_column(0,4,28)
    writer.save() 
    
dataframes = [V7001_1, V7001_2_4, V7001_5]  

dataframes_to_excel(dataframes, 'Лист 2', 'C:/PATH' + str(date.today()) +'.xlsx', 1)

print('================ FINISH')


# In[ ]:




