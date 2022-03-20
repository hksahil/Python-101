#!/usr/bin/env python
# coding: utf-8

# ## Dictionary Comprehension - Filtering

# In[1]:


dict1={
    'A':1,
    'B':2,
    'C':3,
    'D':4,
    'E':5
}
dict1


# ### Filter based on Values

# In[2]:


{x:y for x,y in dict1.items() if y>3}   # Note: here x:y is returned instead of x,y because of format of dict we need


# ### If else Conditions:

# - Syntax:{ (x if else):(y if else) for x,y in dict1.items()}

# #### on Keys

# In[3]:


# Start by writting normal condition { x:y for x,y in dict1.items()}
{ (x.lower() if x=='C' else x) :y for x,y in dict1.items()}


# #### on Values

# In[4]:


# Start by writting normal condition { x:y for x,y in dict1.items()}
{ x: (y*40 if y==4 else y) for x,y in dict1.items()}

