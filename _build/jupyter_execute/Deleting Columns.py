#!/usr/bin/env python
# coding: utf-8

# ## Deleting Columns

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.DataFrame({
'Name':['Sahil','Sonia','Sourav','Vishal'],
'Age':[10,20,30,40],
'Gender':['M','F','M','M'],
'City':['J','K','L','P'],
'Work':[True,False,False,True]
}
)
df


# ### .drop() is used to delete cols

# ### Removing one column

# In[3]:


df.drop('Work',axis=1,inplace=True)


# In[4]:


df


# ### Removing multiple columns

# In[5]:


cols=['Age','City']
df.drop(cols,axis=1,inplace=True)


# In[6]:


df

