#!/usr/bin/env python
# coding: utf-8

# ## Reseting Index of Dataframe

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


# In[3]:


df.reset_index(drop=True)

