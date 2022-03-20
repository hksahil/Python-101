#!/usr/bin/env python
# coding: utf-8

# ## Getting the list of all the files from OS

# In[1]:


import os
import pandas as pd

# Getting the current work directory (cwd)
thisdir = os.getcwd()

# Getting the reqd directory
thatdir='C:\\Users\\Sahil Choudhary\\Book\\Python'

# Traditional way
# r=root, d=directories, f = files

# csv_files=[]
# for r, d, f in os.walk(thisdir):
#     for file in f:
#         if file.endswith(".csv"):
#             csv_files.append(file)


# Single line pythonic way            
csv_files=[ file for r, d, f in os.walk(thisdir) for file in f if file.endswith('.csv')] 
# outer loop first,then inner loop(just like traditional) and then if condition


# In[2]:


csv_files


# In[3]:


# applying some filters if you want
# Lists_list=[i for i in python_files if 'List' in i and 'checkpoint' not in i]


# In[4]:


len(csv_files)


# In[5]:


csv_files


# ### Reading all as CSVs and converting them into single df

# In[6]:


# create empty list
dataframes_list = []

# append datasets into the list
for i in range(len(csv_files)):
    if 'csv' in csv_files[i]:
        temp_df = pd.read_csv(csv_files[i])
        dataframes_list.append(temp_df)


# In[7]:


dataframes_list


# ### Applying operations on multiple dataframes at ones

# In[8]:


def filter(df):
    return df[df.Name=='Graham Chapman']


df1, df2 = [filter(df) for df in dataframes_list]


# In[9]:


df1


# In[10]:


df2

