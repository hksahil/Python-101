#!/usr/bin/env python
# coding: utf-8

# ### Working with CSV files

# ### How does  a csv file looks?

# Name,Hire Date,Salary,Sick Days remaining
# 
# Graham Chapman,03/15/14,50000.00,10
# 
# John Cleese,06/01/15,65000.00,8
# 
# Eric Idle,05/12/14,45000.00,10
# 
# Terry Jones,11/01/13,70000.00,3
# 
# Terry Gilliam,08/12/14,48000.00,7
# 
# Michael Palin,05/23/13,66000.00,8

# Functions to play with csvs are present in Pandas,so import pandas

# In[1]:


import pandas as pd


# ### Reading a csv file into dataframe

# In[2]:


df = pd.read_csv('demo.csv')
print(df)


# ### Skip the number of lines at the start of the file

# In[3]:


pd.read_csv("demo.csv", skiprows = 1)


# ### Getting only some columns while importing

# In[4]:


pd.read_csv('demo.csv',usecols=['Name','Salary']) # you can also use indexes as 0,1,2,3


# ### Specifying the data type explictly while importing

# In[5]:


df=pd.read_csv('demo.csv',dtype={'Salary': float,'Name': str})
print(df.dtypes)


# ### Parsing date columns as dates instead of objects(which is the default behaviour)

# In[6]:


df = pd.read_csv('demo.csv', parse_dates=['Hire Date'])
df.dtypes


# ### Saving the Dataframe as csv

# In[7]:


df.to_csv('demo2.csv',index=False) # The index false removes the first column of 0,1,2,3 that was added by default

