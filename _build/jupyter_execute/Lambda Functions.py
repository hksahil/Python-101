#!/usr/bin/env python
# coding: utf-8

# ## Lambda Functions

# - Anonymous functions

# ### Find 3x+1

# #### Traditional method

# In[1]:


def f(x):
    return 3*x+1

f(2)


# #### Lambda expression

# - Syntax: lambda 0 or more inputs:expression that will be return value
# - Can't be used for multiline functions
# - Only used if functin can be written in 1 line
#     - Common applications are sorting and filtering data

# - lambda : "Hello world"
# - lambda x:x
# - lambda x,y:x+y
# - lambda x,y,z:x+y+z

# In[2]:


g=lambda x:3*x+1  # define
g(2)              # call


# In[3]:


g=lambda x,y:x.strip()+' '+y.strip()
g('sahil','s')

