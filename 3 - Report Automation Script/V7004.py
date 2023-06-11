#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#================ LIBRARIES ================

import mysql.connector
from mysql.connector import Error

import numpy as np
from datetime import datetime 

import json

import pandas as pd
import requests
from xml.etree import ElementTree

from openpyxl import Workbook, load_workbook
from openpyxl.utils import get_column_letter

#================ FUNCTION TO CONNECT TO THE SQL SERVER ================

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

sql_file_reader = open('v7004_sql.sql', 'r')
sql_file = sql_file_reader.read()
sql_file_reader.close()
sql_file = sql_file.replace('\n',' ').replace('\t',' ').split(';')

#================ EXECUTE QUERY ================

for command in sql_file[:-2]:
        try:
            cursor = connection.cursor(dictionary = True)
            try_sql_query = f'''{command}'''
            cursor.execute(try_sql_query)

        except Error as error:
            print('Error:', error)

# Select from table GL_depo_with
try:    
    cursor = connection.cursor(dictionary = True)
    try_sql_query = f'''{sql_file[-2]}'''
    cursor.execute(try_sql_query)
    query_result = cursor.fetchall()

    V7004_select = pd.DataFrame(query_result)

except Error as error:
    print('Error:', error)
    
# Select company settings
try:    
    cursor = connection.cursor(dictionary = True)
    try_sql_query = f'''{sql_file[-1]}'''
    cursor.execute(try_sql_query)
    query_result = cursor.fetchall()

    V7004_settings = pd.DataFrame(query_result)

except Error as error:
    print('Error:', error)
    

#================ PREPROCESSING ================

for col in ['X1', 'X2', 'X3']:
    V7004_select[col] = V7004_select[col].apply(lambda x: '' if str(x) == '0.0' else str(x))
    
# CREATE INDEX
index_list = []
for i in range(1, len(V7004_select) + 1):
    index_list.append(i)
      
# ADD INDEX COLUMN
V7004_select['Index'] = index_list

# CHANGE COLUMN ORDER
cols = V7004_select.columns.tolist()
cols = cols[-1:] + cols[:-1]
V7004_select = V7004_select[cols]

V7004_set_date = V7004_settings['end_date'][0]

date_day = str(pd.to_datetime(V7004_set_date).day)
if len(str(date_day)) == 1:
    date_day = '0' + str(date_day)
    
date_month = str(pd.to_datetime(V7004_set_date).month)
if len(str(date_month)) == 1:
    date_month = '0' + str(date_month)
    
date_year = str(pd.to_datetime(V7004_set_date).year)

branch = str(V7004_settings['branch'][0])
clerk = str(V7004_settings['clerk'][0])
phone = str(V7004_settings['phone'][0])
clerk_post = str(V7004_settings['clerk_post'][0])
phone_post = str(V7004_settings['phone_post'][0])

file_name = 'V7004_'+str(datetime.today().date())

#================ OUTPUT ================

with open("C:/Users/gerber.l/Documents/"+file_name+".txt", "w") as f:
    f.write('#maket "V7004"\n')
    f.write(f'#branch {branch}\n')
    f.write(f'#day {date_day}\n') # Because origin change
    f.write(f'#month {date_month}\n') # Because origin change
    f.write(f'#year {date_year}\n')
    f.write('#version 1\n')
    f.write(f'#clerk "{clerk}"\n')
    f.write(f'#phone "{phone}"\n')
    f.write(f'#clerk_post "{clerk_post}"\n')
    f.write(f'#phone_post "{phone_post}"\n')
    np.savetxt(f, V7004_select, fmt='%s', delimiter = ',')

