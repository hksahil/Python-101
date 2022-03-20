#!/usr/bin/env python
# coding: utf-8

# ## Dictionary Comprehension

# In[1]:


dict1={
    'A':1,
    'B':2,
    'C':3
}
dict1


# In[2]:


{x:y for x,y in dict1.items()}   # Note: here x:y is returned instead of x,y because of format of dict we need


# In[3]:


{x:y*100 for x,y in dict1.items()}


# In[4]:


{x.lower():y*100 for x,y in dict1.items()}

