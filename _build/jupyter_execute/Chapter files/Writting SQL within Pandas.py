#!/usr/bin/env python
# coding: utf-8

# ## Running SQL in Pandas

# In[1]:


get_ipython().system('pip install pandasql')
import pandas as pd


# In[2]:


from pandasql import sqldf
pdsql = lambda q: sqldf(q, globals())

# Just write the sql query in the arguments of this pdsql object


# - Pandasql allows you to query pandas DataFrames using SQL syntax
# - Useful for cleaning and filtering

# In[3]:


df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                   'num_wings': [2, 0, 0, 0],
                   'num_specimen_seen': [10, 2, 1, 8]})
df


# In[4]:


df1=pdsql("SELECT * FROM df where num_legs>4")


# In[5]:


df1


# In[ ]:




