#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json

# DB configuration
database_config = {'user' : 'username',
                   'password' : 'password',
                   'host' : 'host',
                   'port' : 1111,
                   'database' : 'database'}

# Create and save DB configuration dict to JSON
with open("database_config.json", "w") as output:
    json.dump(database_config, output)

