#!/usr/bin/env python
# coding: utf-8

# ## Sorting in Dataframe

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


# ### Sorting one column

# In[3]:


df.sort_values(by='Age',ascending=False)


# ### Sorting multiple columns

# In[4]:


# Sorting by Two cols means if in age,same values are there,It will look at City
df.sort_values(by=['Age','City'],ascending=False)

