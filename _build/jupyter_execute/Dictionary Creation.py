#!/usr/bin/env python
# coding: utf-8

# ## Dictionary Creation

# In[1]:


dict1={
    'A':1,
    'B':2,
    'C':3
}
dict1


# ### From range function

# In[2]:


{i:i*2 for i in range(4)}


# ### From Lists

# In[3]:


list1=['A','B','C']
list2=[1,2,3]
{x:y for x,y in zip(list1,list2)}

