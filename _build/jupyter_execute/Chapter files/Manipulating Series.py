#!/usr/bin/env python
# coding: utf-8

# ## Manipulating a Series

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


s1=pd.Series([1,2,3,4,5])


# In[3]:


s1


# ### Series Inspection

# | Syntax      | Description |
# | ----------- | ----------- |
# | Check datatype of series      | s1.dtype       |
# | Convert datatype of series      | pd.Series(['a','b','c'],dtype=np.float)       |
# | Find mean of series   | s1.mean()        |
# | Find sum of series   | s1.sum()        |
# | Find max of series   | s1.max()        |
# | Sort values of series   | s1.sort_values()        |
# | Change the fifth element of series   | s1[2]='d'        |
# | Add 5 to every element of series   | s1+5        |
# | Get elements>3   | s1[s1>3]        |
# | Get negative elements   | s1[s1>=0]        |
# | Get if element is 2 or 3   | s1[(s1==2) or (s1==3)]       (Replace or by pipe) |
# | Find unique values   | pd.unique(series) or df[''].unique       |
# | Convert series to list   | s1.to_list() (earlier it used to be tolist()       |
# 

# In[ ]:




