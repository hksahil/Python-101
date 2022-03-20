#!/usr/bin/env python
# coding: utf-8

# ## List of Strings to list of ints

# In[1]:


age=['1','2','3']
age=[int(i) for i in age]
print(age)


# ## List of ints to list of strings

# In[2]:


age=[1,2,3]
age=[str(i) for i in age]
print(age)

