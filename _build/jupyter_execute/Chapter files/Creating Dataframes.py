#!/usr/bin/env python
# coding: utf-8

# ## Creating a Dataframe

# In[1]:


import pandas as pd
import numpy as np


# ### Empty Dataframe

# In[2]:


df=pd.DataFrame()  # D and F are capital
print(df)


# ### From Clipboard

# In[3]:


df=pd.read_clipboard()


# ### From List

# In[4]:


Name=['Sahil', 'Sonia', 'Sourav', 'Vishal']
Age=[20, 21, 19, 18]
print(pd.DataFrame(list(zip(Name,Age)))) # Note: If you don't pass columns,it takes col names as 0 1 by default
print()
print(pd.DataFrame(list(zip(Name,Age)),columns=['Name','Age']))


# #### Custom indexes

# In[5]:


df=pd.DataFrame(list(zip(Name,Age)))
df.index=['First','Second','Third','Fourth']
print(df)


# ### From Single Series

# In[6]:


s1=pd.Series(['A','B','C','D'])
print(s1.to_frame()) #col header will be 0,1 by default
print()
print(s1.to_frame(name='Alphabets'))


# ### From Multiple series as columns of dataframe

# In[7]:


s1=pd.Series(['A','B','C','D'])
s2=pd.Series([10,20,30,40])

s1.to_frame(name = 'Name').join(s2.to_frame(name='Age'))


# ### From dictionary

# In[8]:


df=pd.DataFrame({'Name':['Sahil', 'Sonia', 'Sourav', 'Vishal'],
        'Age':[20, 21, 19, 18]})
df


# #### Assigning indexes after declaring the series

# In[9]:


new_indexes=['a','b','c','d']
df.index=new_indexes
df


# ### From csv

# In[10]:


df = pd.read_csv ('https://people.sc.fsu.edu/~jburkardt/data/csv/crash_catalonia.csv')


# In[11]:


df


# #### Import specific columns

# In[12]:


pd.read_csv('https://people.sc.fsu.edu/~jburkardt/data/csv/crash_catalonia.csv', usecols= ['Day of Week'])


# #### Replacing nans

# In[13]:


pd.read_csv('https://people.sc.fsu.edu/~jburkardt/data/csv/crash_catalonia.csv', na_values=['NA','np.nan'])


# #### Read only first n rows

# In[14]:


pd.read_csv('https://people.sc.fsu.edu/~jburkardt/data/csv/crash_catalonia.csv',nrows=3)

