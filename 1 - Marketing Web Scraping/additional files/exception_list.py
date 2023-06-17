#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json 

# Exception list
exception_list = ['domain', 'company', 'month_year', 'traffic_share', 'avg_visit_duration']

# Create and save exception list
with open('exception_list.json', 'w') as output:
    json.dump(exception_list, output)

