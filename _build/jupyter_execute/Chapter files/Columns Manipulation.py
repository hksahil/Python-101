#!/usr/bin/env python
# coding: utf-8

# ## String functions on Columns

# ### EDA   for columns

# - Source: yt/Chares tech

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.DataFrame({
'First Name':['Sahil','Sonia','Sourav','Vishal'],
'Age':[10,20,30,40],
'Gender':['M','F','M','M'],
'City':['J','K','L','P'],
'Place of Work':[True,False,False,True],
}
)
df


# #### Get columns as list

# In[3]:


df.columns.tolist()


# #### Convert column names to series | df:

# In[4]:


df.columns.to_series()


# In[5]:


df.columns.to_frame()


# #### Check if specific column is there or not

# In[6]:


df.columns.str.contains('Name') 


# #### Check if any duplicate column is there

# In[7]:


df.columns.duplicated()


# #### Check methods/attributes of String

# In[8]:


dir(df.columns.str)[0:5]


# #### Make column names to lower case

# In[9]:


df.columns.str.lower()


# #### Make column names to Upper case

# In[10]:


df.columns.str.upper()


# #### Make column names to Title case

# In[11]:


df.columns.str.title()  # Camel Case


# #### Make column names to Capitalize

# In[12]:


df.columns.str.capitalize() # Only first letter big


# #### Replace empty spaces with underscores

# In[13]:


df.columns.str.replace(' ','-')


# #### Rename columns

# In[14]:


df.rename(columns={'oldname':'newname'},inplace=True)


# #### Check total number of columns

# In[15]:


len(df.columns)


# #### Select particular columns

# In[16]:


df.columns.values[0:4]


# #### Get 2nd column and rename it

# In[17]:


df.columns.values[2]='DOB'


# In[18]:


df


# #### Select all columns except one

# In[19]:


df.columns[df.columns!= 'DOB']


# In[20]:


df


# #### Select all columns except multiple

# In[21]:


#?
df.loc[:,-df.columns.isin(['DOB','City']).columns]


# #### Select column names that begins with particular word

# In[48]:


df.columns.str.startswith('First')
# Gives array of booleans


# #### Select group of column names

# In[46]:


df.columns.values[[0,1,2]]


# In[47]:


df.columns[0:3]

