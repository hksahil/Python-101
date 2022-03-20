#!/usr/bin/env python
# coding: utf-8

# ## Renaming Columns

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


# ### Use df.rename function and pass dict of oldname:newname

# In[3]:


df.rename({
'Name':'First Name',
'City':'Place'
},axis=1,inplace=True)  # Note:you can pass axis=columns too
# 0=rows
# 1=columns


# In[4]:


df


# In[ ]:




