#!/usr/bin/env python
# coding: utf-8

# ## Cleaning Columns

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.DataFrame({
'First Name':['Sahil','Sonia','Sourav','Vishal'],
'Age^':[10,20,30,40],
'Ge%nder%':['M','F','M','M'],
'City':['J','K','L','P'],
'Place of      Work':[True,False,False,True],
 'Place-of-Work':[True,False,False,True]
}
)
df


# ### Remove spaces from names

# In[3]:


df2=df.copy(deep=True)


# In[4]:


df2.columns=df2.columns.str.replace(' +','_')


# In[5]:


df2


# ### Remove Special Characters from Names

# In[6]:


df2=df.copy(deep=True)


# In[7]:


df2


# In[8]:



# df2.columns = df2.columns.str.replace(' +', '_') # + means n numbers

# Rename specific columns explicitly if needed
df2.rename({'Ge%nder%':'Gender'},axis=1,inplace=True)

# If you want to do this step only if column of this name exists,then wrap it in if condition:
if 'Ge%nder%' in df2.columns:
    df2.rename({'Ge%nder%':'Gender'},axis=1,inplace=True)


# In[9]:


df2


# In[10]:


df2.columns=df2.columns.str.replace('[^A-Za-z]+', '_')


# In[11]:


df2


# In[12]:


df2.columns = df2.columns.str.strip('_')    # used to remve specific characters from first and last position 


# In[13]:


df2


# #### Patterns

# - [^A-Za-z]+ - If you just want to ignore A-Z or a-z alphabets
# - [^A-Za-z\s]+ - If you just want to ignore A-Z or a-z alphabets and spaces
# - [^A-Za-z0-9]+ If you wantto ignore alphabets + numbers

# #### Note

# - All the string functions (like replace) can be chained as well
#     - df['col'].str.replace('%','_').str.replace('$','_')

# In[ ]:




