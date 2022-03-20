#!/usr/bin/env python
# coding: utf-8

# ## DateTime

# ### Create a DateTime

# In[1]:


import datetime
dt=datetime.datetime(2016,7,12,2,30,45,1400)
dt


# #### Get Date

# In[2]:


a=dt.date()


# In[3]:


a


# In[4]:


print(a)


# #### Get Time 

# In[5]:


b=dt.time()


# In[6]:


b


# In[7]:


print(b)

