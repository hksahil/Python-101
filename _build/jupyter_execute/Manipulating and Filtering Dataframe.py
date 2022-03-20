#!/usr/bin/env python
# coding: utf-8

# ## Manipulating Dataframe

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.DataFrame({
'Name':['Sahil Choudhary','Sonia Choudhary','Sourav','Vishal'],
'Age':[10,20,30,40],
'Gender':['M','F','M','M'],
'City':['J','K','L','P'],
'Work':[True,False,False,True]
}
)
df


# ### Dataframe Inspection

# In[3]:


df['Age'].mean()


# In[4]:


df['Age'].sum()


# In[5]:


df['Name'].unique()


# In[6]:


df['Name'].nunique()


# In[7]:


df['Name'].value_counts()


# ### Applying Conditions on columns

# #### Condition on one column

# In[8]:


df[df['Age']>10]


# In[9]:


# If you don't want entire dataframe but want only one column
df[df['Age']>10]['Name']


# #### Name contains Choudhary

# In[10]:


df[df['Name'].str.contains('Choudhary')]


# #### Condition on multiple columns

# In[11]:


df[(df['Age']>10) & (df['Gender']=='M')]  # Note: It won't work if you replace & by and


# In[12]:


df[df['Age'].between(10,20)]

