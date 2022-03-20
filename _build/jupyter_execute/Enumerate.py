#!/usr/bin/env python
# coding: utf-8

# ## Enumerate

# - Adds number to the list
# - Counter
# - Used when you need counter or positions or Indexes

# ### Syntax

# - enumerate(list)
#     - Takes list
#     - Returns tupple by default (iterable so has to be converted explicitly)

# In[1]:


list1=['a','b']


# In[2]:


enumerate(list1) # returns iterable obj <> which is tuple by default but can be converted to list as well


# In[3]:


print([i for i in enumerate(list1)])  # by default returns tupple we just returned i

print([(i,j) for i,j in enumerate(list1)]) # this is same thing as above

#print([i,j for i,j in enumerate(list1)])   # this will give error because you are explicitly returning two vars

print([[i,j] for i,j in enumerate(list1)]) # can be converted to list as well


# ## Use case

# In[4]:


#All the if conditions can be applied since it is list comprehension


# ### Getting even indexed values
# - Note:It is based on index not actual values

# In[5]:


list=[11,13,12,14,15,76,89]


# ### Get the index only if index==even

# In[6]:


[(i,j) for i,j in enumerate(list) if i%2==0]


# ### Get the index only if value= 76

# In[7]:


[i for i,j in enumerate(list) if j==76]

