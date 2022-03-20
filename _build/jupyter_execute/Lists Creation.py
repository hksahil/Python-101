#!/usr/bin/env python
# coding: utf-8

# ## List Creation

# In[1]:


list1=[1,2,3,4]
list1


# ### From range function

# In[2]:


[i for i in range(4)]


# ### From dict

# In[3]:


dict1={
    'A':1,
    'B':2,
    'C':3
}
dict1


# ### From keys

# In[4]:


[i for i,j in dict1.items()]


# ### From values

# In[5]:


[j for i,j in dict1.items()]


# ### From dataframe

# In[6]:


import pandas as pd
df = {'Name': ['Sahil', 'Sonia', 'Sourav', 'Deepak'], 'Age': [20, 21, 19, 18]}
pd.DataFrame(df)


# In[7]:


[ i for i in df['Name']]

