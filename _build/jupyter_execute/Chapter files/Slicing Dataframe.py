#!/usr/bin/env python
# coding: utf-8

# ## Slicing Dataframe using Loc and iLoc

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


# ### Accessing columns by Names

# #### Accessing single column

# In[3]:


df['Name'] # Series


# In[4]:


# Getting the value of column
df['Name'][2]


# In[5]:


df[['Name']] # Dataframe


# In[6]:


df.Name  # Another way


# #### Accessing multiple columns

# In[7]:


df[['Name','Age','Gender']]


# In[8]:


# Another way
list_cols=['Name','Gender']
df[list_cols]


# #### Using loc

# - df.loc[rows,columns] # Note:square brackets are used with loc
#     - all rows or filtered rows
#     - example, df.loc[df['age']>50,'name'] === df[df['age']['name']
#     - df.loc[0,:]
#     - df.loc[[1,2,3],:]
#     - df.loc[[1,2,3]:['Name,'Age','Gender']

# In[9]:


df.loc[:,['Name','Gender']]


# ### Accessing range of columns 

# #### By index

# In[10]:


df.iloc[:,[1,4]]


# #### By Name

# In[11]:


df.loc[:,['Name','Gender']]


# In[12]:


df.iloc[:,1:4]


# In[13]:


df.loc[:,'Name':'Gender']


# #### Give all columns of 0th row

# In[14]:


df.loc[0,:]


# #### Give all columns of first 3 rows

# In[15]:


df.loc[[0,1,2],:]


# ### Notes

# - loc is used to access through names
# - iloc is used to access through indexes
# - , in used to select given columns
# - : is used to select range of columns
# - if you want particular columns during fetching dataframe,use columns=list of columns you want to select

# ![g](https://i2.wp.com/sparkbyexamples.com/wp-content/uploads/2021/10/pandas-difference-loc-vs-iloc.png?resize=840%2C353&ssl=1)

# ### Summary

# In[16]:


# Get first row 
df.loc[0]


# In[17]:


# Get first two rows 
df.loc[0:1] 


# In[18]:


# Get first two rows's specific column
df.loc[0:1].Name


# In[19]:


# Get even numbered rows
df.loc[df.index%2==0]


# In[20]:


# Get odd numbered rows
df.loc[df.index%2!=0]


# In[21]:


# Add steps in rows
# Select every nth row
# df[df.index % n == 0]  # Selects every nth raw starting from 0
df[df.index % 2 == 0]


# In[22]:


# Excludes every nth row
df[df.index % 3 != 0]


# In[ ]:




