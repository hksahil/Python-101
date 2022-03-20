#!/usr/bin/env python
# coding: utf-8

# ## String

# - Immutable

# ### List to string

# - 'separator'.join(iterable) 
#     - takes list as input
#     - returns string which is concat of these list elements

# In[1]:


''.join(['Sahil' 'Choudhary'])


# In[2]:


','.join(['A','B','C','D'])


# ### String to List

# - str_var.split('-')
#     - Takes String
#     - Returns List

# In[3]:


'sahil-choudhary'.split('-')


# ### Iterating over Strings

# In[4]:


# For iterations,for loop is not pythonic way,using comprehensions is pythonic way

s='sahil choudhary'
[x for x in s]


# ### Reversing a String

# In[5]:


'sahil'[::-1]


# ### Note
# - input() always takes input as string
#     - convert it to int/float as required
