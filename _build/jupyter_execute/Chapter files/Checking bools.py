#!/usr/bin/env python
# coding: utf-8

# ## Checking if true or false

# - true is written as True
# - false is written as False

# In[1]:


a=True
if a==True:
    print('do this')


# ### Checking if true:

# In[2]:


# or use this directly:
if a:
    print('do this')


# ### Checking if false:

# - False in python=empty values=(),[],{},0,0.0,"",None
# - Note: space is not false,empty is false

# In[3]:


if not a:
    print('do this')


# ### Note

# - Comparison operators(<,>,==,!=) returns bools
#     - 1<2
#     - 0<=1
#     - 1==2
#     - 1!=0
