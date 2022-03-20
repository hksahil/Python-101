#!/usr/bin/env python
# coding: utf-8

# ## Integer Sequence

# - use range function
# - range creates a sequence of numbers
# - range function returns range object which is iterable
#     - range function returns range object (which is iterable) ⇒convert it to list to see the inside elements

# ### Syntax

# range([start],end[,step])
# - [] means optional
# - start defaults to 0
# - end is exclusive
# - step is 1 by default
# - returns iterable

# ### One argument

# In[1]:


list(range(5))


# #### Use case

# In[2]:


a=[1,2,3,4,5,6]
list(range(len(a)))
# Note: This is like indexes of the sequence you passed if you see it carefully


# ### Two arguments

# In[3]:


list(range(3,8))


# ### Three arguments

# #### Positive Step

# In[4]:


list(range(2,12,3))


# #### Negative Step

# In[5]:


list(range(20,5,-5))

