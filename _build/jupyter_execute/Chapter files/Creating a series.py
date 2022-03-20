#!/usr/bin/env python
# coding: utf-8

# ## Creating a Series

# In[1]:


import pandas as pd
import numpy as np


# ### Empty Series

# In[2]:


a=pd.Series()
print(a)


# ### From List

# In[3]:


list1=['A','B','C']
print(pd.Series(list1))

# or

print(pd.Series(['A','B','C']))


# #### Custom indexes

# In[4]:


a=pd.Series(['A','B','C','D'],index=['First','Second','Third','Fourth'])
print(a)


# ### From numpy array

# In[5]:


# simple array
data = np.array(['S','A','H','I','L'])
a = pd.Series(data)
print(a)


# ### From dictionary

# In[6]:


b=pd.Series({
    0:'Sahil',
    1:'Sonia',
    2:'Sourav'
})
print(b)


# ### Assigning indexes after declaring the series

# In[7]:


new_indexes=['a','b','c']
b.index=new_indexes
print(b)

