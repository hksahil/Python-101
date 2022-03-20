#!/usr/bin/env python
# coding: utf-8

# ## Delete Elements

# In[1]:


names=['Sahil','Sonia','Sourav']
age=[10,20,30]


# ### Remove first element

# In[2]:


names.pop(0) # in pop,pass the index


# ### Remove last element

# In[3]:


names.pop()


# In[4]:


names=['Sahil','Sonia','Sourav']


# ### Remove any element based on position

# In[5]:


names.pop(2)


# ### Remove any element based on value

# In[6]:


names.remove('Sahil')

