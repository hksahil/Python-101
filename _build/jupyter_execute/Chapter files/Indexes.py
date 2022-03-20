#!/usr/bin/env python
# coding: utf-8

# ## Indexes

# - Indexes
#     - Identifiers for rows
#     - Unique value for each row
#     - Unnamed column

# In[1]:


import pandas as pd
df=pd.DataFrame(
{
    'name':['sahil','sonia','sourav'],
    'age':[10,20,30],
    'gender':['M','F','M']
})


# In[2]:


df


# ### See the index

# In[3]:


df.index


# ### Set some column as index

# In[4]:


df.set_index('name',inplace=True)
df


# In[5]:


df.index


# In[6]:


# df.loc[0] # earlier with default indexes not intutitive
df.loc['sahil'] # More intuitive
df.loc['sahil','gender']


# In[7]:


df.iloc[0] # Note: iloc will still take integer index.i can only take indexes(in integers)


# ### Resetting Index

# In[8]:


df.reset_index(inplace=True)


# In[9]:


df


# ### Setting indexes directly while loading/creating dataframe

# In[10]:


df=pd.read_csv('demo.csv')


# In[11]:


df


# In[12]:


df=pd.read_csv('demo.csv',index_col="Name")


# In[13]:


df

