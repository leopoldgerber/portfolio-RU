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

sql_file_reader = open('v7003_sql.sql', 'r', encoding='utf8')
sql_file = sql_file_reader.read()
sql_file_reader.close()
sql_file = sql_file.replace('\n',' ').replace('\t',' ').split(';')

#================ EXECUTE QUERY ================

for command in sql_file[:-3]:
        try:
            cursor = connection.cursor(dictionary = True)
            try_sql_query = f'''{command}'''
            cursor.execute(try_sql_query)

        except Error as error:
            print('Error All:', error)
            
# Select from table GL_rep K1
try:    
    cursor = connection.cursor(dictionary = True)
    try_sql_query = f'''{sql_file[-3]}'''
    cursor.execute(try_sql_query)
    query_result = cursor.fetchall()

    V7003_select_1 = pd.DataFrame(query_result)

except Error as error:
    print('Error K1:', error)
    
# Select from table GL_rep K2
try:    
    cursor = connection.cursor(dictionary = True)
    try_sql_query = f'''{sql_file[-2]}'''
    cursor.execute(try_sql_query)
    query_result = cursor.fetchall()

    V7003_select_2 = pd.DataFrame(query_result)

except Error as error:
    print('Error K2:', error)
    
# Select company settings
try:    
    cursor = connection.cursor(dictionary = True)
    try_sql_query = f'''{sql_file[-1]}'''
    cursor.execute(try_sql_query)
    query_result = cursor.fetchall()

    V7003_settings = pd.DataFrame(query_result)

except Error as error:
    print('Error Company:', error)
    
#================ PREPROCESSING ================

# CREATE INDEX - K1 & K2
k1_list = []
k2_list = []
for i in range(1, len(V7003_select_1) + len(V7003_select_2) + 1):
    if i % 2 == 1:
        k1_list.append(i)
    else:
        k2_list.append(i)

# ADD INDEX COLUMN - K1 & K2
V7003_select_1['Index'] = k1_list
V7003_select_2['Index'] = k2_list

# APPEND
V7003_select = V7003_select_1.append(V7003_select_2) 

# CHANGE DELIMETR
X_list = ['X1', 'X2', 'X3', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11']

for i in X_list:
    V7003_select[i] = V7003_select[i].apply(lambda x: str(x) if x % 1 != 0.0 else str(int(x)))
    V7003_select[i] = V7003_select[i].apply(lambda x: '' if str(x) == 'nan' else str(x))
    
# FILLNA
V7003_select = V7003_select.fillna('')

# CHANGE COLUMN ORDER
cols = V7003_select.columns.tolist()
cols = cols[-1:] + cols[:-1]
V7003_select = V7003_select[cols]

# CHANGE & ADD ZERO
def add_zero(line):
    strp_1 = [x for x in line.split('.')][0]
    strp_2 = [x for x in line.split('.')][1]
    if len(strp_2) != 5:
        zero = str(strp_2) + str((5 - len(strp_2)) * '0')
        strp = str(strp_1) + '.' + str(zero)
    else:
        strp = str(strp_1) + '.' + str(strp_2)
        
    return strp
        
for i in ['X4', 'X5']:
    V7003_select[i] = V7003_select[i].astype(str)
    V7003_select[i] = V7003_select[i].apply(add_zero)

date_month = str(pd.to_datetime(V7003_select['D1'].sort_values().iloc[0]).day)
if len(str(date_day)) == 1:
    date_day = '0' + str(date_day)
date_day = pd.to_datetime(V7003_select['D1'].sort_values().iloc[0]).month
if len(str(date_month)) == 1:
    date_month = '0' + str(date_month)
date_year = str(pd.to_datetime(V7003_select['D1'].sort_values().iloc[0]).year)

branch = str(V7003_settings['branch'][0])
clerk = str(V7003_settings['clerk'][0])
phone = str(V7003_settings['phone'][0])
clerk_post = str(V7003_settings['clerk_post'][0])
phone_post = str(V7003_settings['phone_post'][0])

file_name = 'V7003_'+str(datetime.today().date())

#================ OUTPUT ================

with open("C:/PATH_to_file/"+file_name+".txt", "w") as f:
    f.write('#maket "V7003"\n')
    f.write(f'#branch {branch}\n')
    f.write(f'#day {date_day}\n')
    f.write(f'#month {date_month}\n')
    f.write(f'#year {date_year}\n')
    f.write('#version 1\n')
    f.write(f'#clerk "{clerk}"\n')
    f.write(f'#phone "{phone}"\n')
    f.write(f'#clerk_post "{clerk_post}"\n')
    f.write(f'#phone_post "{phone_post}"\n')
    np.savetxt(f, V7003_select, fmt='%s', delimiter = ',')

