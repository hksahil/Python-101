#!/usr/bin/env python
# coding: utf-8

# ## Removing Falses from List

# In[1]:


names=['Sahil',1,0,False,None,""," "]
[i for i in names if i]


# - The last section if i removes all the false and in python : 0,False,empty strings are considered false

# In[2]:


[i for i in names if i and i!=" "]


# - adding one more condition will remove those spaces also
