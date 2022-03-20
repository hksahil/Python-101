#!/usr/bin/env python
# coding: utf-8

# ## Applying functions on Dataframe

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.DataFrame({
'Name':['Sahil Choudhary','Sonia Choudhary','Sourav','Vishal'],
'Age':[10,20,30,40],
'Gender':['M','F','M','M'],
'City':['J','K','L','P'],
'Place of Work':[True,False,False,True]
}
)
df


# In[3]:


def process(x):
    # Here x is series,you have passed entire col
    return 'a'


# In[4]:


df['New']=process(df['Name'])


# In[ ]:




