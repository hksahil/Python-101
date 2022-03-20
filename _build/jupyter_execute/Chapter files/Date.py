#!/usr/bin/env python
# coding: utf-8

# ## Date

# ### Create a date

# #### Create any date

# In[1]:


import datetime
datetime.date(2021,7,24) 


# #### Create today's date

# In[2]:


d=datetime.date.today()
d


# - If you want to specify timezone,use .now() instead of today()
# - Don't add leading leading zeroes yourself, it will cause syntax error

# #### When date is created, you will need to get its components too

# ### Get Date's components

# In[3]:


d.year


# In[4]:


d.month


# In[5]:


d.day


# In[6]:


d.isoweekday

