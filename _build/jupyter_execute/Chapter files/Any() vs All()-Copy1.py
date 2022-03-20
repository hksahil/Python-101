#!/usr/bin/env python
# coding: utf-8

# ## SQL vs Pandas

# In[1]:


SELECT 
sum(total_bill),
avg(size),
min(tip),
FROM 
  tips 
where tip>5
Group by sex,day
Order by total_bill desc,tip asc

