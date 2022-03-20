#!/usr/bin/env python
# coding: utf-8

# ## Random Module

# In[1]:


import random


# ### To check the available methods in this module

# In[2]:


print(dir(random))


# In[3]:


print(random.random())


# - By default,it gives random number between 0 and 1It gives numbers between 0 and 1
#     - 0 is inclusive
#     - 1 is exclusive

# #### Summary

# - Get random number(float) between 0 and 1 (1 being exclusive) - ```random.random()```
# - Get random number(float) between custom range - ```random.uniform(min,max)```
# - Get random integer between a range - ```random.randint(min,max)```
# ```random.choice(list)```

# In[4]:


for i in range(10):
    print(random.random())


# ### Get random numbers between custom range

# - Use uniform()

# In[5]:


# get random numbers from 3 to 7
print(random.uniform(3,7))


# In[6]:


print(random.randint(1,6))


# In[7]:


outcomes=['rock','paper','scissor']
for i in range(5):
    print(random.choice(outcomes))

