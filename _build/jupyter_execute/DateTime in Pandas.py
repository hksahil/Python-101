#!/usr/bin/env python
# coding: utf-8

# ## DateTime in Pandas 

# In[1]:


import pandas as pd
df=pd.DataFrame({
    "Name":['A','B','C'],
    "Dates":['2020-03-22','2020-02-10','2020-07-16']
    
})


# In[2]:


df


# - First step should be to check if column is string or datetime

# In[3]:


df.dtypes


# - If not datetime, do this ```df['datetime column']=pd.to_datetime(df['datetime column'])```

# In[4]:


df['Dates']=pd.to_datetime(df['Dates'])


# In[5]:


df


# In[6]:


df.dtypes


# ### To specify date formats use format property

# - pd.to_datetime(df['datetime column'],format=%d/%m/%Y)
# - pd.to_datetime(df['datetime column'],format=%d-%m-%Y)
# - pd.to_datetime(df['datetime column'],format=%d--%m--%Y)

# ### Note

# - % is used to specify each format code
# - %m → month
# - %d → day
# - %Y → year(4 digits)

# #### If the column type is datetime, you can do these things with that column(just make sure to write .dt before the metric you want)

# - df['Datetime column'].dt.time
# - df['Datetime column'].dt.hour
# - df['Datetime column'].dt.minute
# - df['Datetime column'].dt.dayofyear
# - df['Datetime column'].dt.year
# - df['Datetime column'].dt.month
# - df['Datetime column'].dt.day
# - df['Datetime column'].dt.week
# - df['Datetime column'].dt.weekday
# - df['Datetime column'].dt.weekday_name

# ### Converting string to datetime

# In[7]:


new_date=pd.to_datetime('1/1/2021')
print(new_date)


# In[8]:


df['New date column']=new_date


# In[9]:


df


# In[10]:


df.dtypes

