#!/usr/bin/env python
# coding: utf-8

# ## Update Elements

# In[1]:


names=['Sahil','Sonia','Sourav']
age=[10,20,30]


# ### Update based on position of element

# In[2]:


names[0]='Sahil Choudhary'
names


# ### Update based on value of elements

# In[3]:


for index,x in enumerate(names):
    if "Sonia" in names:
        names[index]='Sonia Choudhary'
names

