#!/usr/bin/env python
# coding: utf-8

# ## TimeDelta

# ### Add to dates to get future dates

# - date+date = timeedelta
# - date+timedelta=date

# In[1]:


import datetime
seven_days=datetime.timedelta(days=7) # 7 dats after date
date=datetime.date(2021,7,24) 


# In[2]:


# date(date)+7day(timedelta)
a=date+seven_days


# In[3]:


a


# In[4]:


print(a)

