#!/usr/bin/env python
# coding: utf-8

# ## Remove Duplicates

# In[1]:


names=['Sahil','Sonia','Sourav','Sahil']
age=[10,20,30]


# #1 Using Ordered dict

# In[2]:


from collections import OrderedDict
list(OrderedDict.fromkeys(names))


# #2 Using Set

# In[3]:


names=['Sahil','Sonia','Sourav','Sahil']


# In[4]:


list(set(names))


# #3 Using non pyhonic way

# In[5]:


names=['Sahil','Sonia','Sourav','Sahil']


# In[6]:


new=[]
for i in names:
    if i not in new:
        new.append(i)
new

