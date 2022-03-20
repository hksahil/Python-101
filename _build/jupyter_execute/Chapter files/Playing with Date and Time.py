#!/usr/bin/env python
# coding: utf-8

# ## Playing with Date and Time

# - Python do not has date as datatype
# - Python has datetime library to **create** dates and times

# ### Summary

# In[1]:


import datetime


# - datetime.date() # pass yyyy,m,d
# - datetime.time() # pass h,m,s,ms
# - datetime.datetime() # pass year,month,day,hour,minute,second,ms
# - datetime.timedelta()

# In[2]:


datetime.date(1997,2,19)


# In[3]:


datetime.time(12,22,21,11)


# In[4]:


datetime.datetime(1997,2,19,12,22,21,11)

