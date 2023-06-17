#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import psycopg2
import json
import glob
import os
import re

path = r'{}'.format(str(input('Enter the path to the datasets: ')))
path = path.replace('\\', '/') + '/'

# Connect to DB - Choose path to config.json file
config_path = r'{}'.format(str(input('Enter the path to the configuration file: ')))
config_path = config_path.replace('\\', '/') + '/'

# =============== Upload ===============

def upload_files(path):
    # Local path to folder
    local_path = path
    path_list = glob.glob(os.path.join(local_path, f"*.xlsx"))


    df_name_list = []
    df = []

    for file in path_list:
        file = [i for i in file.split('\\')][1] # Get file name
        df_name = [i for i in file.split('.')][0] # Get df name
        df_name_list.append(df_name)
        try:
            df_temp = pd.read_excel(local_path + file) # Upload dataset excel
        except:
            df_temp = pd.read_csv(local_path + file) # Upload dataset csv
        df.append(df_temp)

    temp_dict = {}
    
    # Create key from df name & value as choosen df
    for i, v in enumerate(df_name_list):
        temp_dict[v] = df[i]

    return df_name_list, temp_dict

# Create variable from key that equals the df in value
df_names, df_temp = upload_files(path)
locals().update(df_temp)

# =============== Preprocessing ===============

# Rename df columns
def columns_change_name(df):
    return df.columns.str.lower().str.replace(' ', '_', regex=True) \
                                      .str.replace('/', '', regex=True) \
                                      .str.replace('.', '', regex=True)
# Check for punctuation in column values
def punctuation_search(text):
    result = re.findall(r'[!"\$%&\'()*+,\-.\/:;=#@?\[\\\]^_`{|}~]*', text)
    string="".join(result)
    return list(string)

# Count string type values in column
def columns_punctuation(df):
    df.columns = columns_change_name(df)
    for col in df.columns:
        try:
            temp_var = sum([len(x) for x in df[col].apply(lambda x: punctuation_search(x))])
            temp_dict[col] = temp_var
        except:
            pass

    temp_df = pd.DataFrame(pd.Series(temp_dict, dtype='int64')) \
              .reset_index().rename(columns = {0:'Values'})
    return list(temp_df['index'][temp_df['Values'] > 0])

# Change punctuation in column values (can be modified)
def columns_edit(df):
    choosen_columns = columns_punctuation(df)
    
    try:
        with open('exception_list.json', 'r') as output:
            exception_columns = json.load(output)
    except:
        exception_columns = [str(x).replace(' ','').replace("'", '') \
                             for x in input('Exception columns: ').split(',')]
    for col in choosen_columns:
        # Choose exception
        if col not in exception_columns:
            df[col] = df[col].str.replace(r'[^\w\s]+', ' ', regex=True)

# Start columns_edit and drop unnamed:_0 columns from original dataset

df_list = [globals()[k] for k in df_names]

for i, df in enumerate(df_list):
    temp_dict = {}
    columns_edit(df)
    if 'unnamed:_0' in df.columns:
        df.drop(columns = ['unnamed:_0'], axis = 1, inplace = True)
        
# =============== DB Connection ===============

def db_connect(config_path:str):
    # Open and load DB configuration file
    config_path = config_path.replace('\\', '/')
    db_config_json = open(f'{config_path}')
    db_config = json.load(db_config_json)

    del db_config_json

    # Connect to DB
    connection = psycopg2.connect(user = db_config['user'],
                                 password = db_config['password'],
                                 host = db_config['host'],
                                 port = db_config['port'],
                                 database = db_config['database'])

    connection.autocommit = True
    
    return connection
    
# =============== DB Upload ===============

class Example:
    def __init__(self, df, table_name):
        self.df = df
        self.table_name = table_name
    
    # Declare column type for Table columns type
    type_dict = {'object' : 'text',
                 'int64' : 'integer',
                 'float64' : 'float'}

    # Parse the column type
    def get_column_type(self):
        column_type = {}
        for col in self.df.columns:
            column_type[col] = str(self.df[col].dtype)
        return column_type
    
    # Create Table
    def create_table(self):
        with connection.cursor() as cursor:
            cursor.execute(
            '''
            DROP TABLE IF EXISTS {};
            CREATE TABLE {}()
            '''.format(self.table_name, self.table_name)
        )
    
    # Alter all columns
    def alter_columns(self):
        column_type = self.get_column_type()
        with connection.cursor() as cursor:
            for col in self.df.columns:
                cursor.execute(
                '''
                ALTER TABLE {}
                ADD {} {}
                '''.format(self.table_name, col, self.type_dict[column_type[col]])
            )
    # Insert all rows
    def insert_rows(self):
        with connection.cursor() as cursor:
            for i, v in enumerate(self.df.values):
                cursor.execute("""
                            INSERT INTO {} VALUES (
                            {}
                            );
                        """.format(self.table_name, str(list(v)).replace('[', '').replace(']', '').replace('nan', '0')))


connection = db_connect(r'{}database_config.json'.format(config_path))

for i, df in enumerate(df_list):
    Example(df, f'{df_names[i]}').create_table()
    Example(df, f'{df_names[i]}').alter_columns()
    Example(df, f'{df_names[i]}').insert_rows()
connection.close()

